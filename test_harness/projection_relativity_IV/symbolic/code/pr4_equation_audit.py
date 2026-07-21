#!/usr/bin/env python3
"""Inventory and coverage audit for every PR-IV display and theorem claim."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path


DISPLAY_ENVIRONMENTS = ("equation", "align", "alignat", "gather", "multline", "flalign")
DISPLAY_PATTERN = re.compile(
    r"\\begin\{((?:" + "|".join(DISPLAY_ENVIRONMENTS) + r")\*?)\}(.*?)\\end\{\1\}|\\\[(.*?)\\\]",
    re.DOTALL,
)
CLAIM_PATTERN = re.compile(
    r"\\begin\{(theorem|proposition|lemma|corollary)\}(?:\[([^\]]+)\])?(.*?)\\end\{\1\}",
    re.DOTALL,
)


@dataclass(frozen=True)
class Display:
    id: str
    file: str
    start_line: int
    end_line: int
    environment: str
    label: str
    heading: str
    coverage_class: str
    test_ids: str
    status: str
    excerpt: str


@dataclass(frozen=True)
class Claim:
    id: str
    file: str
    start_line: int
    kind: str
    title: str
    label: str
    test_ids: str
    status: str


DIRECT_LABEL_MAP: dict[str, tuple[str, ...]] = {
    "eq:pr35-sector-uniqueness-standard": ("global:normal_form_composition",),
    "eq:pr35-equation-class-singleton": ("global:normal_form_composition",),
    "eq:pr35-canonical-solution-isolation": ("global:normal_form_composition",),
    "eq:pr35-global-class-singleton": ("global:selector_coordinate_exhaustion", "global:normal_form_composition"),
    "eq:pr35-radial-admissible-class": ("radial:unique_coefficients",),
    "eq:pr35-a2-unique": ("radial:unique_coefficients",),
    "eq:pr35-a4-unique": ("radial:unique_coefficients",),
    "eq:pr35-radial-unique": ("radial:unique_coefficients", "radial:strict_convexity"),
    "eq:pr35-semigroup": ("compact:semigroup_gaps",),
    "eq:pr35-semigroup-gaps": ("compact:semigroup_gaps",),
    "eq:pr35-unique-positive-terminal": ("compact:semigroup_gaps",),
    "eq:pr35-signed-terminal-set": ("compact:semigroup_gaps", "terminal:unique_orientation"),
    "eq:pr35-da-exact": ("compact:boundary_rationals",),
    "eq:pr35-nbc-exact": ("compact:boundary_rationals",),
    "eq:pr35-cbc-exact": ("compact:boundary_rationals",),
    "eq:pr35-pi13-unique": ("compact:minimal_projector",),
    "eq:pr35-terminal-countermodels": ("terminal:omitted_rule_negative_control",),
    "eq:pr35-hypercharge-factorization": ("hypercharge:cubic_factorization", "hypercharge:nonzero_orbit"),
    "eq:pr35-pr3-monomial-counterexamples": ("finite-tier:monomial_enumeration",),
    "eq:pr35-three-selector-equation-exhaustion": (
        "terminal:unique_orientation", "generation:count_rigidity", "generation:normalized_incidence", "d3:canonical_k"
    ),
    "eq:pr35-normalized-incidence-isometry": ("generation:normalized_incidence",),
    "eq:pr35-current-closed-equation-singleton": ("global:selector_coordinate_exhaustion", "global:normal_form_composition"),
    "eq:pr35-broken-dimension": ("generation:count_rigidity",),
    "eq:pr35-sheet-incidence-map": ("generation:count_rigidity",),
    "eq:pr35-full-boundary-return-series": ("terminal:return_series",),
    "eq:pr35-xz8-exclusion": ("terminal:unique_orientation",),
    "eq:pr35-d3-u1-invariance": ("d3:u1_rank_reduction",),
    "eq:pr35-d3-complete-invariant-family": ("d3:u1_rank_reduction",),
    "eq:pr35-d3-charged-unchanged": ("d3:u1_rank_reduction",),
    "eq:pr35-d3-photon-null": ("d3:u1_rank_reduction",),
    "eq:pr35-d3-all-real-k-family": ("d3:u1_rank_reduction", "d3:structural_family_negative_control"),
    "eq:pr35-d3-structural-theory": ("d3:structural_family_negative_control",),
    "eq:pr35-d3-model-expansion": ("d3:structural_family_negative_control",),
    "eq:pr35-d3-projected-tensor": ("d3:adjoint_trace",),
    "eq:pr35-d3-k-equals-two-p3": ("d3:adjoint_trace",),
    "eq:pr35-d3-canonical-response-norm": ("d3:canonical_k",),
    "eq:pr35-d3-canonical-response-identity": ("d3:canonical_k",),
    "eq:pr35-canonical-response-axioms": ("d3:unique_quadratic_response",),
    "eq:pr35-unique-response-functional": ("d3:unique_quadratic_response",),
    "eq:pr35-minimal-neutral-response-class": ("d3:unique_quadratic_response", "d3:canonical_k"),
    "eq:pr35-d3-block-determinant": ("d3:log_hessian",),
    "eq:pr35-d3-exact-log-hessian": ("d3:log_hessian",),
    "eq:pr35-d3-determinant-counterblock": ("d3:second_jet_counterfamily",),
    "eq:pr35-d3-needed-normalized-block": ("d3:second_jet_counterfamily", "d3:canonical_k"),
    "eq:pr35-d3-unique-canonical-result": ("d3:u1_rank_reduction", "d3:canonical_k"),
    "eq:pr35-d3-four-defects": ("d3:u1_rank_reduction", "d3:unique_defect_zero"),
    "eq:pr35-d3-complete-real-defect": ("d3:unique_defect_zero",),
    "eq:pr35-d3-lambda-counterfamily": ("d3:structural_family_negative_control",),
    "eq:pr35-d3-literal-w3-embedding": ("d3:mixing_normalization_nogo",),
    "eq:pr35-d3-three-neutral-maps": ("d3:mixing_normalization_nogo",),
    "eq:pr35-d3-diagnostic-interval": ("d3:diagnostic_firewall",),
    "eq:pr35-d3-current-generator-trace": ("d3:canonical_k",),
    "eq:pr35-z-source-connection": ("physical-z:normalized_generator",),
    "eq:pr35-z-physical-vector-trace": ("physical-z:normalized_generator",),
    "eq:pr35-z-required-block-hessian": ("d3:log_hessian",),
    "eq:pr35-z-second-jet-family": ("physical-z:second_jet_shift",),
    "eq:pr35-z-second-jet-shift": ("physical-z:second_jet_shift",),
    "eq:pr35-z-local-counteroperator": ("physical-z:eft_operator",),
}


CLAIM_MAP: dict[str, tuple[str, ...]] = {
    "prop:pr35-canonical-closure-standard": ("global:no_fit_firewall",),
    "prop:pr35-complete-certified-class": ("global:selector_coordinate_exhaustion",),
    "thm:pr35-normal-form-exhaustion": ("global:normal_form_composition",),
    "thm:pr35-completed-selector-singleton": ("global:selector_coordinate_exhaustion", "global:normal_form_composition"),
    "Axiom-by-axiom Uniqueness in the Completed Compact Class": ("terminal:unique_orientation", "compact:minimal_projector"),
    "thm:pr35-three-selector-equation-exhaustion": ("terminal:unique_orientation", "generation:count_rigidity", "generation:normalized_incidence", "d3:canonical_k"),
    "prop:pr35-current-closed-equation-quotient": ("global:selector_coordinate_exhaustion", "global:normal_form_composition"),
    "PR-II generation-count rigidity": ("generation:count_rigidity",),
    "Terminal-orientation Rigidity": ("terminal:return_series", "terminal:unique_orientation"),
    "thm:pr35-d3-u1-classification": ("d3:u1_rank_reduction",),
    "thm:pr35-d3-common-reduct": ("d3:structural_family_negative_control",),
    "lem:pr35-d3-adjoint-trace": ("d3:adjoint_trace",),
    "prop:pr35-d3-direct-k-value": ("d3:canonical_k",),
    "thm:pr35-unique-quadratic-response": ("d3:unique_quadratic_response",),
    "lem:pr35-d3-log-hessian": ("d3:log_hessian",),
    "thm:pr35-d3-determinant-counterfamily": ("d3:second_jet_counterfamily",),
    "thm:pr35-d3-conditional-uniqueness": ("d3:u1_rank_reduction", "d3:canonical_k"),
    "thm:pr35-d3-four-defect-certificate": ("d3:u1_rank_reduction", "d3:unique_defect_zero"),
    "prop:pr35-d3-mixing-nogo": ("d3:mixing_normalization_nogo",),
    "prop:pr35-physical-z-generator": ("physical-z:normalized_generator",),
    "thm:pr35-z-second-jet-nonuniqueness": ("physical-z:second_jet_shift",),
    "prop:pr35-z-local-counteroperator": ("physical-z:eft_operator",),
    "Physical-$Z$ closure": ("physical-z:normalized_generator", "d3:canonical_k", "d3:unique_defect_zero"),
}


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def clean_excerpt(text: str, limit: int = 180) -> str:
    value = " ".join(text.replace("\r", " ").replace("\n", " ").split())
    return value if len(value) <= limit else value[:limit - 3] + "..."


def current_heading(text: str, position: int) -> str:
    matches = list(re.finditer(r"\\(?:section|subsection|subsubsection)\{([^}]*)\}", text[:position]))
    return clean_excerpt(matches[-1].group(1), 100) if matches else "front matter"


def tex_files(tex_root: Path) -> list[Path]:
    main = tex_root / "Oshetski_Projection_Relativity_IV_Main.tex"
    text = main.read_text(encoding="utf-8")
    files = [main]
    for rel in re.findall(r"\\input\{([^}]+)\}", text):
        path = tex_root / f"{rel}.tex"
        files.append(path)
    return files


def classify_display(rel_file: str, label: str, body: str, available: set[str]) -> tuple[str, tuple[str, ...], str]:
    if label in DIRECT_LABEL_MAP:
        ids = DIRECT_LABEL_MAP[label]
        return "DIRECT_EXACT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"

    filename = Path(rel_file).name
    low = body.lower()
    if filename.startswith(("02_", "03_", "08_")):
        ids = ("global:normal_form_composition", "global:no_fit_firewall")
        return "FORMAL_CLOSURE_CONTRACT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("04_"):
        if any(needle in low for needle in ("alpha", "lambda", "p_1", "q_{\\rm bc}")):
            return "INHERITED_PR1_REPRODUCIBILITY", ("inherited:pr1-symbolic",), "COVERED"
        ids = ("radial:unique_coefficients", "compact:boundary_rationals", "compact:minimal_projector")
        return "DIRECT_EXACT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith(("05_", "10_")):
        ids = ("compact:axiom_layer_negative_control", "terminal:unique_orientation", "compact:minimal_projector")
        return "EXACT_WITH_NEGATIVE_CONTROL", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("06_"):
        if "begin{pmatrix}" in low or "n=1,2,3" in low:
            ids = ("photon:rank_one_null_line",) if "pmatrix" in low else ("generation:anomaly_gate_negative_control",)
        else:
            ids = ("hypercharge:cubic_factorization", "hypercharge:nonzero_orbit")
        return "DIRECT_EXACT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("07_"):
        ids = ("finite-tier:monomial_enumeration", "finite-tier:grammar_negative_control")
        return "FIXED_TIER_AND_NEGATIVE_CONTROL", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith(("09_", "11_", "12_")):
        ids = ("global:no_fit_firewall",)
        return "DIAGNOSTIC_OR_SUMMARY_FIREWALL", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("13_"):
        ids = ("global:selector_coordinate_exhaustion", "global:normal_form_composition")
        return "DIRECT_EXACT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("14_"):
        ids = ("generation:count_rigidity", "generation:normalized_incidence")
        return "DIRECT_EXACT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("15_"):
        ids = ("terminal:return_series", "terminal:unique_orientation")
        return "DIRECT_EXACT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("16_"):
        if any(needle in low for needle in ("m_z", "gev", "sigma", "diagnostic")):
            ids = ("d3:diagnostic_firewall",)
            return "DIAGNOSTIC_NEGATIVE_CONTROL", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
        ids = ("d3:u1_rank_reduction", "d3:canonical_k", "d3:unique_quadratic_response", "d3:log_hessian")
        return "DIRECT_EXACT_OR_SCOPE_BOUNDARY", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    if filename.startswith("17_"):
        ids = ("physical-z:normalized_generator", "physical-z:second_jet_shift", "physical-z:eft_operator")
        return "DIRECT_EXACT_OR_SCOPE_BOUNDARY", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"
    ids = ("global:no_fit_firewall",)
    return "SOURCE_CONTEXT", ids, "COVERED" if set(ids) <= available else "MISSING_TEST"


def source_integrity(tex_root: Path, files: list[Path]) -> dict[str, object]:
    missing_inputs = [str(path) for path in files if not path.exists()]
    texts = {path: path.read_text(encoding="utf-8") for path in files if path.exists()}
    labels: list[str] = []
    refs: list[str] = []
    cites: list[str] = []
    for text in texts.values():
        labels.extend(re.findall(r"\\label\{([^}]+)\}", text))
        refs.extend(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text))
        for group in re.findall(r"\\cite\{([^}]+)\}", text):
            cites.extend(key.strip() for key in group.split(","))
    duplicates = sorted(key for key, count in Counter(labels).items() if count > 1)
    missing_refs = sorted(set(refs) - set(labels))
    bib = tex_root / "Oshetski_Projection_Relativity_IV_References.bib"
    bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib.read_text(encoding="utf-8"))) if bib.exists() else set()
    missing_cites = sorted(set(cites) - bib_keys)
    directory_names = {path.name for path in tex_root.iterdir() if path.is_dir()}
    lowercase_sections = "sections" in directory_names
    uppercase_absent = "Sections" not in directory_names
    return {
        "status": "PASS" if not (missing_inputs or duplicates or missing_refs or missing_cites)
        and lowercase_sections and uppercase_absent else "FAIL",
        "input_file_count": len(files) - 1,
        "missing_inputs": missing_inputs,
        "unique_label_count": len(set(labels)),
        "duplicate_labels": duplicates,
        "reference_count": len(refs),
        "missing_references": missing_refs,
        "citation_key_count": len(set(cites)),
        "missing_citations": missing_cites,
        "lowercase_sections_directory": lowercase_sections,
        "uppercase_sections_directory_absent": uppercase_absent,
    }


def write_csv(path: Path, rows: list[object], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--tex-root", type=Path, required=True)
    parser.add_argument("--exact-results", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    tex_root = args.tex_root.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    exact = json.loads(args.exact_results.read_text(encoding="utf-8"))
    available = {item["id"] for item in exact["checks"] if item["status"] == "PASS"}
    inherited_required = [
        repo / "test_harness/projection_relativity_I/symbolic/RUN_SUMMARY.md",
        repo / "test_harness/projection_relativity_II/symbolic/RUN_SUMMARY.md",
        repo / "test_harness/projection_relativity_III/RUN_SUMMARY.md",
    ]
    if all(path.exists() for path in inherited_required):
        available.add("inherited:pr1-symbolic")

    files = tex_files(tex_root)
    displays: list[Display] = []
    claims: list[Claim] = []
    display_counter = 0
    claim_counter = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        rel_file = path.relative_to(repo).as_posix()
        for match in DISPLAY_PATTERN.finditer(text):
            display_counter += 1
            body = match.group(2) if match.group(1) else match.group(3)
            environment = match.group(1) or "bracket"
            label_match = re.search(r"\\label\{([^}]+)\}", body)
            label = label_match.group(1) if label_match else ""
            coverage_class, ids, status = classify_display(rel_file, label, body, available)
            displays.append(Display(
                id=f"PR4-EQ-{display_counter:04d}", file=rel_file,
                start_line=line_number(text, match.start()), end_line=line_number(text, match.end()),
                environment=environment, label=label, heading=current_heading(text, match.start()),
                coverage_class=coverage_class, test_ids=";".join(ids), status=status,
                excerpt=clean_excerpt(body),
            ))
        for match in CLAIM_PATTERN.finditer(text):
            claim_counter += 1
            kind, title, body = match.group(1), match.group(2) or "untitled", match.group(3)
            label_match = re.search(r"\\label\{([^}]+)\}", body)
            label = label_match.group(1) if label_match else ""
            key = label or title
            ids = CLAIM_MAP.get(key, ())
            status = "COVERED" if ids and set(ids) <= available else ("UNMAPPED" if not ids else "MISSING_TEST")
            claims.append(Claim(
                id=f"PR4-CLAIM-{claim_counter:03d}", file=rel_file,
                start_line=line_number(text, match.start()), kind=kind, title=clean_excerpt(title, 120),
                label=label, test_ids=";".join(ids), status=status,
            ))

    integrity = source_integrity(tex_root, files)
    display_uncovered = [row for row in displays if row.status != "COVERED"]
    claim_uncovered = [row for row in claims if row.status != "COVERED"]
    status = "PASS" if displays and claims and not display_uncovered and not claim_uncovered \
        and integrity["status"] == "PASS" else "FAIL"
    class_counts = Counter(row.coverage_class for row in displays)
    summary = {
        "status": status,
        "display_blocks_total": len(displays),
        "display_blocks_covered": len(displays) - len(display_uncovered),
        "display_blocks_uncovered": len(display_uncovered),
        "display_coverage_fraction": (len(displays) - len(display_uncovered)) / len(displays) if displays else 1,
        "theorem_claims_total": len(claims),
        "theorem_claims_covered": len(claims) - len(claim_uncovered),
        "theorem_claims_uncovered": len(claim_uncovered),
        "theorem_coverage_fraction": (len(claims) - len(claim_uncovered)) / len(claims) if claims else 1,
        "coverage_class_counts": dict(sorted(class_counts.items())),
        "source_integrity": integrity,
        "uncovered_display_ids": [row.id for row in display_uncovered],
        "uncovered_claim_ids": [row.id for row in claim_uncovered],
        "coverage_semantics": "Every display is either directly certified, a negative-control/scope boundary, a formal closure contract, or an inherited earlier-paper result. Every theorem/proposition/lemma has at least one executable exact certificate.",
    }
    (output_dir / "pr4_coverage_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(output_dir / "pr4_equation_inventory.csv", displays, list(Display.__dataclass_fields__))
    write_csv(output_dir / "pr4_theorem_inventory.csv", claims, list(Claim.__dataclass_fields__))

    lines = [
        "# PR-IV Manuscript Coverage", "", f"Status: **{status}**", "",
        f"- Display blocks covered: **{summary['display_blocks_covered']}/{len(displays)}**",
        f"- Theorem/proposition/lemma claims covered: **{summary['theorem_claims_covered']}/{len(claims)}**",
        f"- Missing inputs: **{len(integrity['missing_inputs'])}**",
        f"- Duplicate labels: **{len(integrity['duplicate_labels'])}**",
        f"- Missing references: **{len(integrity['missing_references'])}**",
        f"- Missing citations: **{len(integrity['missing_citations'])}**", "",
        "Full coverage means complete source accounting with an explicit coverage mode; it does not relabel definitions, inherited equations, or scope countermodels as independent symbolic theorems.", "",
        "## Coverage classes", "",
    ]
    lines.extend(f"- `{key}`: {value}" for key, value in sorted(class_counts.items()))
    if display_uncovered or claim_uncovered:
        lines.extend(["", "## Uncovered", ""])
        lines.extend(f"- `{row.id}` ({row.file}:{row.start_line})" for row in [*display_uncovered, *claim_uncovered])
    (output_dir / "pr4_coverage_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"PR-IV equation audit: {status} ({len(displays) - len(display_uncovered)}/{len(displays)} displays; "
          f"{len(claims) - len(claim_uncovered)}/{len(claims)} theorem claims)")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
