#!/usr/bin/env python3
"""Run the complete public PR-IV symbolic and manuscript coverage gate."""

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


def run(arguments: list[str]) -> None:
    process = subprocess.run(
        [sys.executable, *arguments], cwd=REPO, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    if process.stdout:
        print(process.stdout.rstrip())
    if process.returncode:
        raise SystemExit(process.returncode)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manuscript_commit() -> str:
    try:
        process = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", str(TEX_ROOT.relative_to(REPO))],
            cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
        )
    except FileNotFoundError:
        return "unavailable (git not on PATH)"
    return process.stdout.strip() if process.returncode == 0 else "unavailable"


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    exact_path = RESULTS / "pr4_exact_results.json"
    run([str(CODE / "pr4_exact_harness.py"), "--output-dir", str(RESULTS)])
    run([
        str(CODE / "pr4_equation_audit.py"),
        "--repo", str(REPO), "--tex-root", str(TEX_ROOT),
        "--exact-results", str(exact_path), "--output-dir", str(RESULTS),
    ])

    exact = json.loads(exact_path.read_text(encoding="utf-8"))
    coverage = json.loads((RESULTS / "pr4_coverage_summary.json").read_text(encoding="utf-8"))
    status = "PASS" if exact["status"] == coverage["status"] == "PASS" else "FAIL"
    payload = {
        "status": status,
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
        "selector_coordinates": [
            "minimal radial coefficients", "minimal required-channel projector",
            "terminal boundary orientation", "nonzero-ledger hypercharge orbit",
            "photon null line", "normalized generation incidence", "normalized neutral D3 response",
        ],
        "interpretation": "The corrected completed admissible class is singleton. Broader P1-P7/common-reduct alternatives are retained and passed as negative controls, not counted as admissible PR branches.",
    }
    (RESULTS / "PR4_RUN_SUMMARY.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "# Projection Relativity IV Harness Run", "", f"Status: **{status}**", "",
        f"- Exact symbolic checks: **{exact['passed']}/{exact['total']}**",
        f"- Display-math coverage: **{coverage['display_blocks_covered']}/{coverage['display_blocks_total']}**",
        f"- Theorem/proposition/lemma coverage: **{coverage['theorem_claims_covered']}/{coverage['theorem_claims_total']}**",
        f"- Unresolved references: **{len(coverage['source_integrity']['missing_references'])}**",
        f"- Unresolved citations: **{len(coverage['source_integrity']['missing_citations'])}**",
        f"- Manuscript source commit: `{payload['manuscript_commit']}`",
        f"- Main TeX SHA-256: `{payload['main_tex_sha256']}`",
        f"- Main PDF SHA-256: `{payload['main_pdf_sha256']}`", "",
        "All seven adjustable equation-selection coordinates are covered by exact certificates. "
        "The broader-class survivors are exercised as negative controls and are excluded only by the final manuscript's declared, target-independent canonical-closure rules.", "",
        "Full display coverage is accounting coverage: definitions, inherited PR-I--PR-III relations, diagnostics, and outside-class countermodels retain explicit coverage labels rather than being misrepresented as independent symbolic theorems.",
    ]
    summary_text = "\n".join(lines) + "\n"
    (RESULTS / "PR4_RUN_SUMMARY.md").write_text(summary_text, encoding="utf-8")
    (HARNESS / "RUN_SUMMARY.md").write_text(summary_text, encoding="utf-8")
    print(f"PR-IV full public harness: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
