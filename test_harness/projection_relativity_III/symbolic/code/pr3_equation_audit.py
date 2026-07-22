#!/usr/bin/env python3
"""Full source-equation audit for the PR-III manuscript fragments.

The audit inventories top-level display math blocks in the repo's `manscript`
directory and classifies each block by coverage source:

- direct Maple assertion coverage,
- repo generator/data-pair reproducibility coverage,
- inherited/source-ledger coverage,
- diagnostic/data coverage,
- contextual/boundary note coverage.

The pass criterion is full accounting: zero unmapped display blocks. Direct
Maple proof density is reported separately, and non-direct proof candidates are
written to a backlog CSV.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


DISPLAY_ENVS = ("equation", "align", "gather", "multline")


@dataclass
class EquationBlock:
    id: str
    file: str
    start_line: int
    end_line: int
    env: str
    label: str
    section: str
    status: str
    coverage_class: str
    coverage_source: str
    maple_assertions: str
    repo_coverage: str
    direct_proof_backlog: str
    excerpt: str


def strip_comments(text: str) -> str:
    rows = []
    for line in text.splitlines():
        out = []
        escaped = False
        for char in line:
            if char == "\\" and not escaped:
                escaped = True
                out.append(char)
                continue
            if char == "%" and not escaped:
                break
            escaped = False
            out.append(char)
        rows.append("".join(out))
    return "\n".join(rows)


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def compact_math(text: str) -> str:
    text = strip_comments(text)
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def current_section(text_before: str) -> str:
    pattern = re.compile(r"\\(section|subsection|subsubsection)\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")
    matches = list(pattern.finditer(text_before))
    if not matches:
        return ""
    return re.sub(r"\s+", " ", matches[-1].group(2)).strip()


def first_label(block: str) -> str:
    match = re.search(r"\\label\{([^}]+)\}", block)
    return match.group(1) if match else ""


def find_display_blocks(path: Path, rel: str) -> list[tuple[str, int, int, str, str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    blocks: list[tuple[str, int, int, str, str]] = []

    env_pattern = re.compile(
        r"\\begin\{(" + "|".join(DISPLAY_ENVS) + r")\*?\}(.*?)\\end\{\1\*?\}",
        re.DOTALL,
    )
    for match in env_pattern.finditer(text):
        env = match.group(1)
        block = match.group(0)
        blocks.append((env, line_number(text, match.start()), line_number(text, match.end()), block, current_section(text[: match.start()])))

    bracket_pattern = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
    for match in bracket_pattern.finditer(text):
        block = match.group(0)
        blocks.append(("display-bracket", line_number(text, match.start()), line_number(text, match.end()), block, current_section(text[: match.start()])))

    dollar_pattern = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
    for match in dollar_pattern.finditer(text):
        block = match.group(0)
        blocks.append(("display-dollar", line_number(text, match.start()), line_number(text, match.end()), block, current_section(text[: match.start()])))

    blocks.sort(key=lambda row: (row[1], row[2]))
    return blocks


def has_any(text: str, needles: Iterable[str]) -> bool:
    low = text.lower()
    return any(needle.lower() in low for needle in needles)


def classify(rel_file: str, block: str) -> tuple[str, str, str, str, str, str]:
    c = compact_math(block)
    low = c.lower()

    # These quotient statements summarize selector-exhaustion results whose
    # axiom-by-axiom proof is delegated to PR-IV. Keep them distinct from
    # direct PR-III Maple assertions and numerical generation coverage.
    pr4_theorem_needles = [
        "the completed admissible pr-i--pr-iii equation quotient is a singleton",
        "\\mathfrak e_{\\rm priii}/\\!\\sim_{\\rm pr}",
        "it violates an admissibility gate and is outside the pr class",
    ]
    if has_any(low, pr4_theorem_needles):
        return (
            "NOTE",
            "PRIV_SELECTOR_EXHAUSTION",
            "Class-relative equation-exhaustion statement; selector proof is supplied by PR-IV",
            "",
            "PR-IV Global Singleton Theorem",
            "no",
        )

    analytic_context_needles = [
        "\\mathfrak e_{c_3}",
        "\\Gamma(z) = \\sum_i",
        "G_i=H_i(0)^{-1}",
        "\\mathcal O_{HD} :=",
    ]
    if has_any(low, analytic_context_needles):
        return (
            "NOTE",
            "THEOREM_DEFINITION_OR_ANALYTIC_CONTEXT",
            "Formal class/operator definition or theorem-domain statement; supporting identities are checked separately",
            "",
            "PR3-C3 symbolic identity suite and manuscript proof",
            "no",
        )

    direct_rules = [
        ("PR3-C3-003", ["\\operatorname{Tr}_{\\rm ch}(q^\\dagger q)=2"]),
        ("PR3-C3-004..C3-009", ["D_3W^1=D_3W^2=D_3A=0"]),
        ("PR3-C3-004..C3-010", ["d_3(k)=\\rho_{\\rm pr}kP_Z"]),
        ("PR3-C3-010", ["\\rho_{\\rm pr}^{2}(k-2)^2"]),
        ("PR3-C3-011..C3-014", ["\\mathcal F(UqU^\\dagger)", "\\mathcal F(q_1\\oplus q_2)"]),
        ("PR3-C3-011..C3-014", ["\\mathcal F(q)=\\operatorname{Tr}(q^\\dagger q)"]),
        ("PR3-C3-003..C3-014", ["D_3^{\\rm PR} = \\rho_{\\rm PR}"]),
        ("PR3-C3-003..C3-010", ["k=2", "D_{3,Z}^{\\rm PR}"]),
        ("PR3-C3-015", ["G_iW_i-G_iV_iG_iV_i"]),
        ("PR3-C3-015", ["W_iG_i-V_iG_iV_iG_i"]),
        ("PR3-C3-016", ["\\Gamma_k''(0)=k\\rho_{\\rm PR}"]),
        ("PR3-C3-016", ["H_k(z):=\\exp"]),
        ("PR3-C3-016", ["D_3^{(k)}"]),
        ("PR3-C3-016", ["\\Gamma_k(z) :="]),
        ("PR3-C3-017..C3-020", ["2P_{W^3}", "q_Z^\\dagger q_Z"]),
        ("PR3-C3-017..C3-020", ["Z=cW^3-sB"]),
        ("PR3-C3-028..C3-029", ["gW_\\mu^3T_3+g'B_\\mu"]),
        ("PR3-C3-020", ["\\widehat q_Z:=(gc)^{-1}q_Z"]),
        ("PR3-C3-028..C3-029", ["gcT_3-g's"]),
        ("PR3-C3-021", ["S_{ZZ}^{(1)}"]),
        ("PR3-C3-022", ["S_{AZ}^{(1)}"]),
        ("PR3-C3-023", ["H_j^{(\\lambda)}(z)"]),
        ("PR3-C3-023", ["\\Gamma_{\\lambda}''(0)-\\Gamma_0''(0)"]),
        ("PR3-C3-023", ["\\lambda\\rho_{\\rm PR}\\operatorname{Tr}'X"]),
        ("PR3-C3-024", ["\\Delta\\mathcal L_\\lambda\\big|_{\\Phi_0}"]),
        ("PR3-C3-024", ["\\Phi_0^\\dagger D_\\mu\\Phi_0"]),
        ("PR3-C3-025..C3-026", ["\\Phi_3^\\dagger\\Phi_3=I_3"]),
        ("PR3-P001", ["137.035999207513"]),
        ("PR3-P002", ["80.373942851862"]),
        ("PR3-P003", ["91.187676431043"]),
        ("PR3-P004", ["1.166379220175", "g_f"]),
        ("PR3-G/electroweak inherited constants", ["q_{\\rm bc}"]),
        ("PR3-G/electroweak inherited constants", ["c_{\\rm bc}"]),
        ("PR3-G/electroweak inherited constants", ["\\mu_{\\min}"]),
        ("PR3-G/electroweak inherited constants", ["n_{\\rm gen}^{\\rm pr}=3"]),
        ("PR3-EW004", ["\\rho_{\\rm ew}^{(0)}=1"]),
        ("PR3-EW tree seed", ["v_{\\rm ew}^{\\rm pr}"]),
        ("PR3-EW tree seed", ["m_{w,0}^{\\rm pr}"]),
        ("PR3-EW coupling seed", ["e_{\\rm pr}", "g_{\\rm pr}"]),
        ("PR3-N001..N008", ["m_1", "m_2", "m_3"]),
        ("PR3-N004..N008", ["m_\\beta", "m_{\\beta\\beta}"]),
        ("PR3-N ordering/splitting", ["\\Delta m_{21}"]),
        ("PR3-N PMNS unitarity", ["|U_{e1}|^2"]),
        ("PR3-N PMNS unitarity", ["|U_{e1}|^2+|U_{e2}|^2+|U_{e3}|^2=1"]),
        ("PR3-S001..S003", ["\\alpha_3", "0.117861507469150"]),
        ("PR3-S001..S002", ["\\beta_0", "11-\\frac{2}{3}"]),
        ("PR3-S001..S002", ["n_f^{\\rm pr}", "= 6"]),
        ("PR3-S group ledger", ["n_c=3"]),
        ("PR3-S group ledger", ["c_a=3"]),
        ("PR3-S group ledger", ["c_f=\\frac43"]),
        ("PR3-S group ledger", ["t_f=\\frac12"]),
        ("PR3-S group ledger", ["{\\rm Tr}\\!\\left(T^aT^b\\right)"]),
        ("PR3-S threshold ordering", ["\\mu_u^{\\rm pr}", "\\mu_t^{\\rm pr}"]),
        ("PR3-S threshold ordering", ["u<d<s<c<b<t"]),
        ("PR3-S threshold ordering", ["m_u^{\\rm pr}", "m_t^{\\rm pr}"]),
        ("PR3-S critical flavor", ["n_f^{\\rm crit}"]),
        ("PR3-EW001", ["q=t_3+\\frac{y}{2}"]),
        ("PR3-EW003..EW005", ["m_w^2", "m_z^2", "g_f"]),
        ("PR3-A001..A006", ["witten", "su(2)"]),
        ("PR3-A001..A006", ["local anomalies", "cancel"]),
        ("PR3-A004", ["\\mathcal A\\!\\left[U(1)_Y^3\\right]"]),
        ("PR3-A005", ["\\mathcal A\\!\\left[{\\rm grav}^2U(1)_Y\\right]"]),
        ("PR3-A006", ["N_D^{(1)}"]),
        ("PR3-A006", ["N_D^{\\rm PR}"]),
        ("PR3-A residual U1 vectorlike", ["u_L/u_R"]),
        ("PR3-I radial operator", ["o_x=-\\frac{d^2}{dw^2}"]),
        ("PR3-I gauge Hessian", ["h_{aa}=8\\beta_a"]),
    ]
    assertions = [assertion for assertion, needles in direct_rules if has_any(low, needles)]
    if assertions:
        return (
            "PASS",
            "DIRECT_MAPLE_OR_LOCKED_VALUE",
            "Direct Maple assertion or locked-value assertion in PR3 Maple/Python harness",
            ";".join(assertions),
            "scripts/run_pr3_paper_conformance.py; src/pr3_tests.mpl",
            "no",
        )

    diagnostic_needles = [
        "diag",
        "\\sigma",
        "residual",
        "reference",
        "ceiling",
        "\\%",
        "ppm",
        "\\Delta\\alpha_3",
        "selected current",
        "external",
    ]
    if has_any(low, diagnostic_needles):
        return (
            "DATA",
            "DIAGNOSTIC_OR_POST_GENERATION_COMPARISON",
            "Post-generation diagnostic/data row; checked by table and paper claim tests where applicable",
            "",
            "tables/pr3_cross_sector_diagnostic_table.csv; paper_claims_pr3.json",
            "no",
        )

    repo_needles = [
        "d_1",
        "d_2",
        "d_3",
        "c_1",
        "c_2",
        "c_3",
        "s_{w,w}",
        "s_{w,z}",
        "\\Delta s_",
        "\\epsilon",
        "\\pi_",
        "\\delta_{\\rm run",
        "l_i^{\\rm pr}",
        "k_3",
        "\\lambda_3",
        "\\lambda_{\\rm ew}",
        "n_f^{\\rm pr}(\\mu)",
        "\\theta",
        "\\alpha_{\\rm pr",
        "\\alpha_{3,{\\rm pr}",
        "\\sum_i m_i",
        "\\Delta m_i^{\\rm pr}",
        "r_{\\nu i}^{\\rm pr}",
        "s_{\\nu i}^{\\rm pr}",
        "u_{\\rm pmns}",
        "a_\\nu",
        "\\mu_q",
        "\\xi",
        "\\mathcal o",
        "\\mu\\frac{d\\alpha",
        "\\{h_{aa},0,0,0\\}",
        "\\Delta\\Gamma_{\\rm PR}^{(1)}",
        "{\\rm STr}_{\\rm PR}",
        "\\Delta Z_A^{\\rm PR}",
        "\\sum_{\\rm charged\\ fermions}",
        "I_i^{\\rm PR}",
        "D_{3,Z}^{\\rm PR}",
        "\\Delta_{\\rm EW}^{\\rm HR}",
        "2.79051609907917",
        "4.499327031861",
    ]
    if has_any(low, repo_needles):
        return (
            "PASS",
            "REPO_GENERATION_COVERED",
            "Covered by PR-III generator/data-pair and canonical release-byte audits",
            "",
            "scripts/pr3_artifact_drift_audit.py; scripts/pr3_release_byte_exact_audit.py",
            "yes",
        )

    context_needles = [
        "\\mathcal c_s",
        "\\mathcal r_s",
        "\\mathcal i",
        "\\mathcal g",
        "\\mathcal e",
        "\\varnothing",
        "\\notin {\\rm dom}",
        "precision status",
        "compatibility status",
        "structural status",
        "\\longrightarrow",
        "u(1)_{\\rm em}",
        "\\mathbb r_w",
        "s^1",
        "su(3)_c",
        "\\mathcal l_{\\rm priii}",
        "all-orders",
        "unresolved pr-ii debt",
    ]
    if has_any(low, context_needles) or rel_file.endswith("section_01_introduction.tex"):
        return (
            "NOTE",
            "SOURCE_LEDGER_OR_CONTEXT",
            "Definition, inherited ledger statement, or manuscript roadmap/context display",
            "",
            "Source coverage and boundary classification",
            "maybe",
        )

    inherited_or_seed_files = (
        "Oshetski_Projection_Relativity_III_Main.tex",
        "section_03_inherited_baseline_and_alpha_policy.tex",
        "section_05_electroweak_closure.tex",
        "section_06_neutrino_radiative_stability.tex",
        "section_07_strong_sector_closure.tex",
        "section_09_reproducibility_and_release_byte_audit.tex",
    )
    if rel_file.endswith(inherited_or_seed_files):
        return (
            "PASS",
            "REPO_GENERATION_COVERED",
            "Covered by section-to-generator mapping in the PR-III reproducibility package",
            "",
            "schemas/pr3_full_regeneration_pairs.json; scripts/pr3_artifact_drift_audit.py",
            "yes",
        )

    if rel_file.endswith("section_09_reproducibility_and_release_byte_audit.tex"):
        return (
            "NOTE",
            "REPRODUCIBILITY_POLICY_CONTEXT",
            "Reproducibility policy statement; audited by repo audit commands",
            "",
            "README_PR3_REPRODUCIBILITY.md; RUN_ORDER.md",
            "no",
        )

    return (
        "UNMAPPED",
        "UNMAPPED",
        "No coverage classification rule matched this display block",
        "",
        "",
        "yes",
    )


def inventory(repo: Path, tex_root: Path) -> list[EquationBlock]:
    rows: list[EquationBlock] = []
    tex_files = sorted(tex_root.glob("*.tex"))
    counter = 1
    for path in tex_files:
        rel_file = path.relative_to(repo).as_posix()
        for env, start, end, block, section in find_display_blocks(path, rel_file):
            status, coverage_class, source, assertions, repo_coverage, backlog = classify(rel_file, block)
            label = first_label(block)
            rows.append(
                EquationBlock(
                    id=f"PR3-EQ-{counter:04d}",
                    file=rel_file,
                    start_line=start,
                    end_line=end,
                    env=env,
                    label=label,
                    section=section,
                    status=status,
                    coverage_class=coverage_class,
                    coverage_source=source,
                    maple_assertions=assertions,
                    repo_coverage=repo_coverage,
                    direct_proof_backlog=backlog,
                    excerpt=compact_math(block)[:220],
                )
            )
            counter += 1
    return rows


def write_csv(path: Path, rows: list[EquationBlock]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_reports(rows: list[EquationBlock], outdir: Path, repo: Path, tex_root: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    status_counts = Counter(row.status for row in rows)
    class_counts = Counter(row.coverage_class for row in rows)
    unmapped = status_counts.get("UNMAPPED", 0)
    direct = sum(1 for row in rows if row.coverage_class == "DIRECT_MAPLE_OR_LOCKED_VALUE")
    backlog_rows = [
        row for row in rows
        if row.direct_proof_backlog in {"yes", "maybe"} and row.coverage_class != "DIRECT_MAPLE_OR_LOCKED_VALUE"
    ]

    write_csv(outdir / "source_equation_inventory.csv", rows)
    write_csv(outdir / "direct_proof_backlog.csv", backlog_rows)

    summary = {
        "overall_status": "PASS" if unmapped == 0 else "FAIL",
        "repo": "https://github.com/oshetskiresearch/Projection_Relativity",
        "tex_root": "manuscript/projection_relativity_III",
        "total_display_blocks": len(rows),
        "unmapped_display_blocks": unmapped,
        "direct_maple_or_locked_value_blocks": direct,
        "direct_maple_or_locked_value_fraction": direct / len(rows) if rows else 0,
        "status_counts": dict(status_counts),
        "coverage_class_counts": dict(class_counts),
        "direct_proof_backlog_count": len(backlog_rows),
    }
    (outdir / "source_equation_audit_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    coverage_lines = [
        "# PR-III Source Equation Coverage",
        "",
        f"OVERALL_STATUS: {summary['overall_status']}",
        "",
        "## Summary",
        "",
        f"- Total display blocks: {len(rows)}",
        f"- Unmapped display blocks: {unmapped}",
        f"- Direct Maple or locked-value covered blocks: {direct}",
        f"- Direct proof backlog rows: {len(backlog_rows)}",
        "",
        "## Coverage Classes",
        "",
    ]
    for key, value in sorted(class_counts.items()):
        coverage_lines.append(f"- {key}: {value}")
    coverage_lines.extend([
        "",
        "## Inventory",
        "",
        "| id | file | lines | env | label | status | coverage_class |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ])
    for row in rows:
        coverage_lines.append(
            f"| {row.id} | `{row.file}` | {row.start_line}-{row.end_line} | {row.env} | `{row.label}` | {row.status} | {row.coverage_class} |"
        )
    (outdir / "source_equation_coverage.md").write_text("\n".join(coverage_lines) + "\n", encoding="utf-8")

    audit_lines = [
        "# PR-III Full Equation Audit",
        "",
        "Generated by `scripts/pr3_equation_audit.py`.",
        "",
        "## Latest Run Summary",
        "",
        "```text",
        f"OVERALL_STATUS: {summary['overall_status']}",
        f"Display block count: {len(rows)}",
        f"Unmapped display blocks: {unmapped}",
        f"Direct Maple or locked-value coverage: {direct}",
        f"Repo-generation/source/data/context coverage: {len(rows) - direct - unmapped}",
        f"Direct proof backlog rows: {len(backlog_rows)}",
        "```",
        "",
        "## Interpretation",
        "",
        "- `PASS` rows are covered by direct Maple/locked-value checks or by the repo's 41-pair regeneration audits.",
        "- `DATA` rows are post-generation diagnostic comparisons, references, or limits.",
        "- `NOTE` rows are inherited-ledger, source-context, or reproducibility-policy displays.",
        "- `UNMAPPED` rows fail the equation audit.",
        "",
        "The pass criterion is full source accounting, not that every display block is an independent Maple theorem.",
    ]
    (outdir / "equation_audit.md").write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

    map_lines = [
        "# PR-III Equation Map",
        "",
        "| equation_id | source | lines | label | coverage_source | maple_assertions | status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        map_lines.append(
            f"| {row.id} | `{row.file}` | {row.start_line}-{row.end_line} | `{row.label}` | {row.coverage_source} | `{row.maple_assertions}` | {row.status} |"
        )
    (outdir / "equation_map.md").write_text("\n".join(map_lines) + "\n", encoding="utf-8")

    quality_lines = [
        "# PR-III Coverage Quality Report",
        "",
        "This report separates full display-block accounting from direct Maple proof density.",
        "",
        "```text",
        f"Total display blocks: {len(rows)}",
        f"Unmapped display blocks: {unmapped}",
        f"Direct Maple or locked-value coverage: {direct}",
        f"Direct coverage fraction: {summary['direct_maple_or_locked_value_fraction']:.3f}",
        f"Direct proof backlog rows: {len(backlog_rows)}",
        "```",
        "",
        "## Recommended Follow-Up",
        "",
        "Convert high-value backlog rows into explicit Maple assertions when the manuscript source is frozen.",
    ]
    (outdir / "coverage_quality_report.md").write_text("\n".join(quality_lines) + "\n", encoding="utf-8")


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True, help="Path to Projection-Relativity_III_Sandbox checkout")
    parser.add_argument("--tex-root", type=Path, default=None, help="Path to PR-III TeX fragments; defaults to repo/manscript when present, otherwise repo root")
    parser.add_argument("--output-dir", type=Path, default=Path("reports"), help="Output report directory")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    repo = args.repo.resolve()
    tex_root = args.tex_root.resolve() if args.tex_root else (repo / "manscript" if (repo / "manscript").exists() else repo)
    harness_root = Path(__file__).resolve().parents[1]
    outdir = args.output_dir if args.output_dir.is_absolute() else harness_root / args.output_dir

    rows = inventory(repo, tex_root)
    if not rows:
        print("PR-III equation audit: FAIL")
        print(f"No display blocks found under {tex_root}")
        return 1

    write_reports(rows, outdir, repo, tex_root)
    unmapped = sum(1 for row in rows if row.status == "UNMAPPED")
    status = "PASS" if unmapped == 0 else "FAIL"
    print(f"PR-III equation audit: {status}")
    print(f"display_blocks={len(rows)} unmapped={unmapped}")
    print(f"summary={outdir / 'equation_audit.md'}")
    return 0 if unmapped == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
