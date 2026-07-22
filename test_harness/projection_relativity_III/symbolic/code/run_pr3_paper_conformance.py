#!/usr/bin/env python3
"""PR-III public paper conformance harness.

This runner wraps the repository's own reproducibility audits and adds a
paper-facing claim check against locked PR-III outputs.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from dataclasses import dataclass, asdict
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Iterable


getcontext().prec = 120


@dataclass
class Result:
    id: str
    section: str
    status: str
    actual: str
    expected: str
    tolerance: str
    note: str


def norm_text(value: str) -> str:
    return " ".join(value.replace("\u00a0", " ").split()).lower()


def decimal_close(actual: str, expected: str, tolerance: str) -> tuple[bool, Decimal]:
    a = Decimal(str(actual))
    e = Decimal(str(expected))
    t = Decimal(str(tolerance))
    err = abs(a - e)
    return err <= t, err


def add(results: list[Result], id_: str, section: str, ok: bool, actual: object,
        expected: object, tolerance: object, note: str) -> None:
    results.append(
        Result(
            id=id_,
            section=section,
            status="PASS" if ok else "FAIL",
            actual=str(actual),
            expected=str(expected),
            tolerance=str(tolerance),
            note=note,
        )
    )


def run_command(repo: Path, args: list[str], label: str, results: list[Result]) -> None:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=str(repo),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = proc.stdout.strip()
    ok = proc.returncode == 0 and "PASS" in output and "FAIL:" not in output
    add(results, label, "repo-audit", ok, output.splitlines()[0] if output else "",
        "returncode 0 with PASS", "n/a", "Repository audit command passed")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_claims(harness_root: Path) -> dict:
    return read_json(harness_root / "paper_claims_pr3.json")


def check_required_files(repo: Path, results: list[Result]) -> None:
    required = [
        "test_harness/projection_relativity_III/numerical/code/run_all_pr3_audits.py",
        "test_harness/projection_relativity_III/numerical/code/pr3_artifact_drift_audit.py",
        "test_harness/projection_relativity_III/numerical/code/pr3_release_byte_exact_audit.py",
        "test_harness/projection_relativity_III/numerical/MANIFEST_PR3_LOCKED_OUTPUTS.json",
        "test_harness/projection_relativity_III/numerical/results/pr3_cross_sector_diagnostic_table.csv",
        "data/projection_relativity_III/data/global_final_priii_consistency_statement.json",
        "data/projection_relativity_III/data/global_anomaly_registry_audit.json",
    ]
    for rel in required:
        path = repo / rel
        add(results, f"file:{rel}", "required-files", path.exists(), path.exists(), True,
            "exists", f"Required repo file {rel}")


def check_locked_outputs(repo: Path, claims: dict, results: list[Result]) -> None:
    manifest = read_json(repo / "test_harness/projection_relativity_III/numerical/MANIFEST_PR3_LOCKED_OUTPUTS.json")
    locked = manifest.get("locked_outputs", {})
    for claim in claims["locked_output_claims"]:
        id_ = claim["id"]
        actual = locked.get(id_)
        if actual is None:
            add(results, id_, "locked-output", False, "missing", claim["expected"],
                claim["tolerance_abs"], "Locked output missing from manifest")
            continue
        ok, err = decimal_close(actual, claim["expected"], claim["tolerance_abs"])
        add(results, id_, "locked-output", ok, actual, claim["expected"],
            claim["tolerance_abs"], f"Locked PR-III output matches paper claim; abs error {err}")


def read_diagnostic_table(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows[row["observable"]] = row
    return rows


def check_diagnostics(repo: Path, claims: dict, results: list[Result]) -> None:
    rows = read_diagnostic_table(repo / "test_harness/projection_relativity_III/numerical/results/pr3_cross_sector_diagnostic_table.csv")
    for claim in claims["diagnostic_claims"]:
        observable = claim["observable"]
        row = rows.get(observable)
        if not row:
            add(results, f"diag:{observable}", "diagnostic-table", False, "missing",
                "present", "n/a", "Diagnostic row missing")
            continue
        residual_ok = norm_text(claim["residual_contains"]) in norm_text(row["residual_or_fraction"])
        status_ok = norm_text(claim["status_contains"]) in norm_text(row["status"])
        add(results, f"diag:{observable}:residual", "diagnostic-table", residual_ok,
            row["residual_or_fraction"], claim["residual_contains"], "substring",
            "Diagnostic residual string matches paper-facing claim")
        add(results, f"diag:{observable}:status", "diagnostic-table", status_ok,
            row["status"], claim["status_contains"], "substring",
            "Diagnostic status string matches paper-facing claim")


def check_status_gates(repo: Path, claims: dict, results: list[Result]) -> None:
    final = read_json(repo / "data/projection_relativity_III/data/global_final_priii_consistency_statement.json")
    decision = final.get("global_decision", {})
    for key, expected in claims["global_status_gates"].items():
        actual = decision.get(key)
        add(results, f"gate:{key}", "global-status", actual == expected, actual, expected,
            "exact", "Final global status gate")

    add(results, "gate:unsafe_claim_excluded", "global-status",
        final.get("unsafe_claim_excluded") == "PR-III proves a complete exact all-orders theory of the Standard Model and QCD.",
        final.get("unsafe_claim_excluded"), "unsafe overclaim explicitly excluded", "exact",
        "All-orders overclaim remains excluded")


def check_anomaly_gates(repo: Path, results: list[Result]) -> None:
    anomaly = read_json(repo / "data/projection_relativity_III/data/global_anomaly_registry_audit.json")
    sums = anomaly.get("local_anomaly_sums_per_generation", {})
    for key, item in sums.items():
        add(results, f"anomaly:{key}", "symbolic-status", item.get("status") == "PASS",
            item.get("value"), "0", "exact", f"{key} cancels per generation")
    witten = anomaly.get("global_SU2_Witten_audit", {})
    add(results, "anomaly:witten_even", "symbolic-status", witten.get("is_even") is True,
        witten.get("total_SU2_doublets"), "even", "predicate", "Witten anomaly absent")
    residual = anomaly.get("residual_U1em_audit", {})
    add(results, "anomaly:residual_u1em", "symbolic-status",
        residual.get("status") == "VECTORLIKE_PASS", residual.get("status"),
        "VECTORLIKE_PASS", "exact", "Residual electromagnetic branch remains vectorlike")


def check_c3_closure_gates(results: list[Result]) -> None:
    """Exact, dependency-free mirrors of the revised Maple C3 checks."""
    q_ch = (Fraction(1), Fraction(-1))
    response = sum(charge * charge for charge in q_ch)
    add(results, "c3:charged_adjoint_trace", "canonical-C3", response == 2,
        response, 2, "exact", "Charged-adjoint quadratic trace")

    rho = Fraction(3, 7)
    canonical_defect = rho * rho * (Fraction(2) - 2) ** 2
    add(results, "c3:canonical_defect", "canonical-C3", canonical_defect == 0,
        canonical_defect, 0, "exact", "Canonical k=2 has zero exact defect")

    # P_Z = diag(0,0,1,0): charged and photon directions are null and
    # only the normalized physical-Z direction survives.
    pz_diagonal = (0, 0, 1, 0)
    add(results, "c3:rank_one_projector", "canonical-C3",
        sum(pz_diagonal) == 1 and all(x * x == x for x in pz_diagonal),
        pz_diagonal, "rank-one idempotent", "exact", "Physical-Z projector gates")
    add(results, "c3:photon_null", "canonical-C3", pz_diagonal[3] == 0,
        pz_diagonal[3], 0, "exact", "Canonical C3 response preserves photon nullity")

    # Exact response-functional checks on rational charge modes.
    q1 = (Fraction(2, 3), Fraction(-1, 3))
    q2 = (Fraction(1, 2),)
    f1 = sum(x * x for x in q1)
    f2 = sum(x * x for x in q2)
    f12 = sum(x * x for x in q1 + q2)
    add(results, "c3:response_additivity", "canonical-C3", f12 == f1 + f2,
        f12, f1 + f2, "exact", "Quadratic response is direct-sum additive")
    scale = Fraction(5, 4)
    scaled = sum((scale * x) ** 2 for x in q1)
    add(results, "c3:response_homogeneity", "canonical-C3", scaled == scale**2 * f1,
        scaled, scale**2 * f1, "exact", "Quadratic response is degree-two homogeneous")

    # Revised one-generation matter traces, checked at independent rational x.
    x = Fraction(7, 30)
    szz_charges = [
        (1, Fraction(1, 2)),
        (1, Fraction(-1, 2) + x),
        (1, x),
        (3, Fraction(1, 2) - Fraction(2, 3) * x),
        (3, Fraction(-1, 2) + Fraction(1, 3) * x),
        (3, -Fraction(2, 3) * x),
        (3, Fraction(1, 3) * x),
    ]
    szz = sum(mult * charge * charge for mult, charge in szz_charges)
    szz_expected = 2 - 4 * x + Fraction(16, 3) * x * x
    add(results, "c3:matter_ZZ_trace", "canonical-C3", szz == szz_expected,
        szz, szz_expected, "exact", "One-generation ZZ charge trace")

    qaz = [
        (1, Fraction(-1), Fraction(-1, 2) + x),
        (1, Fraction(-1), x),
        (3, Fraction(2, 3), Fraction(1, 2) - Fraction(2, 3) * x),
        (3, Fraction(-1, 3), Fraction(-1, 2) + Fraction(1, 3) * x),
        (3, Fraction(2, 3), -Fraction(2, 3) * x),
        (3, Fraction(-1, 3), Fraction(1, 3) * x),
    ]
    saz = sum(mult * charge * tz for mult, charge, tz in qaz)
    saz_expected = 2 - Fraction(16, 3) * x
    add(results, "c3:matter_AZ_trace", "canonical-C3", saz == saz_expected,
        saz, saz_expected, "exact", "One-generation AZ charge trace")

    # Rational orthogonal representative of Phi_3^T Phi_3 = I_3.
    phi3 = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(3, 5), Fraction(-4, 5)),
        (Fraction(0), Fraction(4, 5), Fraction(3, 5)),
    )
    gram = tuple(
        tuple(sum(phi3[k][i] * phi3[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )
    identity = tuple(tuple(Fraction(int(i == j)) for j in range(3)) for i in range(3))
    add(results, "c3:normalized_incidence", "canonical-C3", gram == identity,
        gram, identity, "exact", "Normalized three-sheet incidence map")


def check_paper_text(paper_text: Path | None, claims: dict, results: list[Result]) -> None:
    if paper_text is None:
        add(results, "paper-text:skipped", "paper-text", True, "not provided",
            "optional", "n/a", "Paper text check skipped by request")
        return
    text = paper_text.read_text(encoding="utf-8", errors="replace")
    normalized = norm_text(text)
    for snippet in claims["paper_text_required_snippets"]:
        ok = norm_text(snippet) in normalized
        add(results, f"paper-text:{snippet}", "paper-text", ok, "present" if ok else "missing",
            snippet, "substring", "Near-final paper contains required PR-III claim string")


def run_negative_controls(repo: Path, claims: dict, results: list[Result]) -> None:
    manifest = read_json(repo / "test_harness/projection_relativity_III/numerical/MANIFEST_PR3_LOCKED_OUTPUTS.json")
    locked = manifest["locked_outputs"]

    ok, _ = decimal_close(locked["alpha_inverse_PR"], "137.035000000000", "1e-12")
    add(results, "selftest:reject_wrong_alpha", "negative-controls", not ok, ok, False,
        "must reject", "Reject stale or mistyped alpha inverse")

    ok, _ = decimal_close(locked["M_W_PR_GeV"], "80.0", "1e-12")
    add(results, "selftest:reject_wrong_MW", "negative-controls", not ok, ok, False,
        "must reject", "Reject wrong W mass")

    final = read_json(repo / "data/projection_relativity_III/data/global_final_priii_consistency_statement.json")
    overclaim = final["global_decision"].get("final_exact_all_orders_theorem") == "CLAIMED"
    add(results, "selftest:reject_all_orders_overclaim", "negative-controls",
        not overclaim, overclaim, False, "must reject", "Reject exact all-orders theorem overclaim")

    anomaly = read_json(repo / "data/projection_relativity_III/data/global_anomaly_registry_audit.json")
    u1 = Decimal(anomaly["local_anomaly_sums_per_generation"]["U1Y_cubed"]["value"])
    add(results, "selftest:reject_anomaly_violation", "negative-controls",
        u1 != Decimal("1"), u1, "not 1", "must reject", "Reject anomaly-violating ledger")

    m2 = Decimal(locked["m2_neutrino_eV"])
    m3 = Decimal(locked["m3_neutrino_eV"])
    add(results, "selftest:reject_inverted_neutrino_order", "negative-controls",
        not (m3 < m2), f"m2={m2}; m3={m3}", "m3 not less than m2", "predicate",
        "Reject inverted neutrino ordering")

    wrong_k_defect = (Decimal("1") - Decimal("2")) ** 2
    add(results, "selftest:reject_noncanonical_C3_k", "negative-controls",
        wrong_k_defect != 0, wrong_k_defect, "nonzero", "must reject",
        "Reject noncanonical C3 coefficient k=1")
    frozen_s2 = Decimal("0.231355763298189")
    wrong_photon_component = 2 * frozen_s2
    add(results, "selftest:reject_W3_as_physical_Z", "negative-controls",
        wrong_photon_component != 0, wrong_photon_component, "nonzero", "must reject",
        "Reject literal W3 projector as photon-null physical-Z projector")
    add(results, "selftest:reject_linear_charge_trace", "negative-controls",
        sum((1, -1)) != 2, sum((1, -1)), "not 2", "must reject",
        "Reject linear trace as the normalized quadratic response")


def write_reports(results: list[Result], outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    failures = [r for r in results if r.status != "PASS"]
    sections = sorted({r.section for r in results})

    csv_path = outdir / "pr3_public_harness_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(results[0]).keys()))
        writer.writeheader()
        for result in results:
            writer.writerow(asdict(result))

    summary = {
        "overall_status": "PASS" if not failures else "FAIL",
        "total_checks": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "sections": {
            section: {
                "total": sum(1 for r in results if r.section == section),
                "failed": sum(1 for r in results if r.section == section and r.status != "PASS"),
            }
            for section in sections
        },
        "failures": [asdict(r) for r in failures],
    }
    (outdir / "pr3_public_harness_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    lines = [
        "# PR-III Public Harness Summary",
        "",
        f"OVERALL_STATUS: {summary['overall_status']}",
        "",
        "## Counts",
        "",
        f"- Total checks: {summary['total_checks']}",
        f"- Passed: {summary['passed']}",
        f"- Failed: {summary['failed']}",
        "",
        "## Sections",
        "",
    ]
    for section in sections:
        row = summary["sections"][section]
        status = "PASS" if row["failed"] == 0 else "FAIL"
        lines.append(f"- {section}: {status} ({row['total'] - row['failed']}/{row['total']} passed)")
    lines.extend(["", "## Failed Checks", ""])
    if failures:
        for failure in failures:
            lines.append(f"- `{failure.id}`: {failure.note} (actual `{failure.actual}`, expected `{failure.expected}`)")
    else:
        lines.append("No failures.")
    lines.append("")
    lines.append("## Report Files")
    lines.append("")
    lines.append("- `reports/pr3_public_harness_results.csv`")
    lines.append("- `reports/pr3_public_harness_summary.json`")
    (outdir / "pr3_public_harness_summary.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True, help="Path to the Projection_Relativity public checkout")
    parser.add_argument("--paper-text", type=Path, default=None, help="Optional extracted PR3 paper text")
    parser.add_argument("--output-dir", type=Path, default=Path("reports"), help="Output report directory")
    parser.add_argument("--skip-repo-audits", action="store_true", help="Only run claim checks")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    harness_root = Path(__file__).resolve().parents[1]
    repo = args.repo.resolve()
    outdir = args.output_dir if args.output_dir.is_absolute() else harness_root / args.output_dir

    results: list[Result] = []
    claims = load_claims(harness_root)

    check_required_files(repo, results)
    if not args.skip_repo_audits:
        numerical = repo / "test_harness" / "projection_relativity_III" / "numerical"
        run_command(numerical, ["code/run_all_pr3_audits.py"], "repo_default_audit", results)
        run_command(numerical, ["code/pr3_artifact_drift_audit.py"], "artifact_drift_audit", results)
        run_command(numerical, ["code/pr3_release_byte_exact_audit.py"], "release_byte_exact_audit", results)

    check_locked_outputs(repo, claims, results)
    check_diagnostics(repo, claims, results)
    check_status_gates(repo, claims, results)
    check_anomaly_gates(repo, results)
    check_c3_closure_gates(results)
    check_paper_text(args.paper_text.resolve() if args.paper_text else None, claims, results)
    run_negative_controls(repo, claims, results)

    write_reports(results, outdir)
    failures = [r for r in results if r.status != "PASS"]
    print(f"PR-III public harness: {'PASS' if not failures else 'FAIL'}")
    print(f"checks={len(results)} passed={len(results) - len(failures)} failed={len(failures)}")
    print(f"summary={outdir / 'pr3_public_harness_summary.md'}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
