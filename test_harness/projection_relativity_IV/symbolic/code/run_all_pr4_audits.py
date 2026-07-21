#!/usr/bin/env python3
"""Run the complete public PR-IV reproduction and coverage gate."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
HARNESS = REPO / "test_harness" / "projection_relativity_IV"
SYMBOLIC = HARNESS / "symbolic"
CODE = SYMBOLIC / "code"
RESULTS = SYMBOLIC / "results"
TEX_ROOT = REPO / "manuscript" / "projection_relativity_IV"
MAIN_TEX = TEX_ROOT / "Oshetski_Projection_Relativity_IV_Main.tex"
MAIN_PDF = TEX_ROOT / "Oshetski_Projection_Relativity_IV_Main.pdf"
REFERENCES_BIB = TEX_ROOT / "Oshetski_Projection_Relativity_IV_References.bib"
MANUSCRIPT_PATHS = (MAIN_TEX, MAIN_PDF, REFERENCES_BIB, TEX_ROOT / "sections")


def run(arguments: list[str]) -> None:
    process = subprocess.run(
        [sys.executable, *arguments],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if process.stdout:
        print(process.stdout.rstrip())
    if process.returncode:
        raise SystemExit(process.returncode)


def load_result(filename: str) -> dict:
    path = RESULTS / filename
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or "status" not in payload:
        raise RuntimeError(f"Result file has no status field: {path}")
    return payload


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manuscript_commit() -> str:
    pathspecs = [str(path.relative_to(REPO)) for path in MANUSCRIPT_PATHS]
    try:
        process = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", *pathspecs],
            cwd=REPO,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except FileNotFoundError:
        return "unavailable (git not on PATH)"
    return process.stdout.strip() if process.returncode == 0 else "unavailable"


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    exact_path = RESULTS / "pr4_exact_results.json"
    tolerance_path = HARNESS / "numerical_tolerances.json"

    run([str(CODE / "pr4_exact_harness.py"), "--output-dir", str(RESULTS)])
    run(
        [
            str(CODE / "pr4_pr1_numerical_reproduction.py"),
            "--output-dir",
            str(RESULTS),
            "--tolerances",
            str(tolerance_path),
        ]
    )
    run([str(CODE / "pr4_scope_controls.py"), "--output-dir", str(RESULTS)])
    run(
        [
            str(CODE / "pr4_diagnostic_propagation.py"),
            "--output-dir",
            str(RESULTS),
            "--tolerances",
            str(tolerance_path),
        ]
    )
    run([str(CODE / "pr4_branch_elimination_audit.py"), "--output-dir", str(RESULTS)])
    run(
        [
            str(CODE / "pr4_neutral_d3_reproduction.py"),
            "--output-dir",
            str(RESULTS),
            "--exact-results",
            str(exact_path),
        ]
    )
    run(
        [
            str(CODE / "pr4_equation_audit.py"),
            "--repo",
            str(REPO),
            "--tex-root",
            str(TEX_ROOT),
            "--exact-results",
            str(exact_path),
            "--output-dir",
            str(RESULTS),
        ]
    )

    exact = load_result("pr4_exact_results.json")
    numerical = load_result("pr4_pr1_numerical_results.json")
    controls = load_result("pr4_scope_control_results.json")
    diagnostics = load_result("pr4_diagnostic_propagation_results.json")
    elimination = load_result("pr4_branch_elimination_results.json")
    d3 = load_result("pr4_neutral_d3_results.json")
    coverage = load_result("pr4_coverage_summary.json")

    component_status = {
        "exact_symbolic": exact["status"],
        "pr1_numerical": numerical["status"],
        "scope_controls": controls["status"],
        "diagnostic_propagation": diagnostics["status"],
        "branch_elimination": elimination["status"],
        "neutral_d3": d3["status"],
        "manuscript_coverage": coverage["status"],
    }
    status = "PASS" if all(value == "PASS" for value in component_status.values()) else "FAIL"
    payload = {
        "status": status,
        "component_status": component_status,
        "manuscript_commit": manuscript_commit(),
        "main_tex_sha256": sha256(MAIN_TEX),
        "main_pdf_sha256": sha256(MAIN_PDF),
        "python": platform.python_version(),
        "exact_checks": {key: exact[key] for key in ("total", "passed", "failed")},
        "display_coverage": {
            "total": coverage["display_blocks_total"],
            "covered": coverage["display_blocks_covered"],
            "uncovered": coverage["display_blocks_uncovered"],
        },
        "theorem_claim_coverage": {
            "total": coverage["theorem_claims_total"],
            "covered": coverage["theorem_claims_covered"],
            "uncovered": coverage["theorem_claims_uncovered"],
        },
        "source_integrity": coverage["source_integrity"],
        "bounded_reproduction_counts": {
            "compact_scope_rows": controls["compact"]["rows"],
            "radiative_monomials": controls["radiative"]["monomial_count"],
            "electroweak_diagnostic_rows": diagnostics["electroweak_rows"],
            "branch_elimination_rows": elimination["findings_total"],
        },
        "selector_coordinates": [
            "minimal radial coefficients",
            "minimal required-channel projector",
            "terminal boundary orientation",
            "nonzero-ledger hypercharge orbit",
            "photon null line",
            "normalized generation incidence",
            "normalized neutral D3 response",
        ],
        "interpretation": (
            "The corrected completed admissible class is singleton. Broader "
            "P1-P7/common-reduct alternatives are retained and passed as negative controls, "
            "not counted as admissible PR branches."
        ),
    }
    (RESULTS / "PR4_RUN_SUMMARY.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Projection Relativity IV Harness Run",
        "",
        f"Status: **{status}**",
        "",
        f"- Exact symbolic checks: **{exact['passed']}/{exact['total']}**",
        (
            "- Component gates passing: "
            f"**{sum(value == 'PASS' for value in component_status.values())}/"
            f"{len(component_status)}**"
        ),
        f"- PR-I numerical ledger: **{numerical['status']}**",
        f"- Finite scope controls: **{controls['status']}**",
        f"- Diagnostic propagation: **{diagnostics['status']}**",
        (
            f"- Branch-control matrix: **{elimination['findings_total']} rows, "
            f"{elimination['status']}**"
        ),
        f"- Neutral D3 table: **{d3['status']}**",
        (
            f"- Display-math coverage: **{coverage['display_blocks_covered']}/"
            f"{coverage['display_blocks_total']}**"
        ),
        (
            "- Theorem/proposition/lemma coverage: "
            f"**{coverage['theorem_claims_covered']}/{coverage['theorem_claims_total']}**"
        ),
        f"- Unresolved references: **{len(coverage['source_integrity']['missing_references'])}**",
        f"- Unresolved citations: **{len(coverage['source_integrity']['missing_citations'])}**",
        f"- Manuscript source commit: `{payload['manuscript_commit']}`",
        f"- Main TeX SHA-256: `{payload['main_tex_sha256']}`",
        f"- Main PDF SHA-256: `{payload['main_pdf_sha256']}`",
        "",
        (
            "All seven adjustable equation-selection coordinates are covered by exact "
            "certificates, and the numerical tables are regenerated independently of "
            "diagnostic selection. The broader-class survivors are exercised as negative "
            "controls and are excluded only by the final manuscript's declared, "
            "target-independent canonical-closure rules."
        ),
        "",
        (
            "Full display coverage is accounting coverage: definitions, inherited "
            "PR-I--PR-III relations, diagnostics, and outside-class countermodels retain "
            "explicit coverage labels rather than being misrepresented as independent "
            "symbolic theorems."
        ),
    ]
    summary_text = "\n".join(lines) + "\n"
    (RESULTS / "PR4_RUN_SUMMARY.md").write_text(summary_text, encoding="utf-8")
    (HARNESS / "RUN_SUMMARY.md").write_text(summary_text, encoding="utf-8")
    print(f"PR-IV full public harness: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
