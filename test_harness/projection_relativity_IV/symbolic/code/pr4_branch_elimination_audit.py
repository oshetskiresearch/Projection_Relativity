#!/usr/bin/env python3
"""Classify the bounded PR-IV diagnostic controls without fitting."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    sector: str
    candidate: str
    test: str
    outcome: str
    reason: str
    no_fit: bool = True


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(); args.output_dir.mkdir(parents=True, exist_ok=True)
    findings: list[Finding] = []
    compact = read_csv(args.output_dir / "pr4_compact_branch_outputs.csv")
    for row in compact:
        candidate, passed = row["model_id"], row["inside_Rb_1sigma"] == "True"
        findings.append(Finding(
            "PR-I compact", candidate, "locked Rb alpha^-1 (1 sigma)",
            "SURVIVES" if passed else "REJECTED_PHYSICAL",
            f"alpha^-1={row['alpha_D1D2_inverse']}; distance={row['alpha_sigma_distance']} sigma"))
        if row["channels"] == "1,3":
            findings.extend([
                Finding("PR-I compact", candidate, "quasar residual sign", "NON_DISCRIMINATING",
                        "The published diagnostic contains no sigma8, c_bc, or projector selector."),
                Finding("PR-I compact", candidate, "Kerr residual-suppression bound", "NON_DISCRIMINATING",
                        "Changing sigma8 at fixed Pi13 leaves the radial spectral gap unchanged."),
                Finding("PR-I compact", candidate, "magnetic area/Faraday residual", "NON_DISCRIMINATING",
                        "The projected source area is not independently fixed by this diagnostic."),
            ])
    radiative = read_csv(args.output_dir / "pr4_radiative_monomial_outputs.csv")
    for index, row in enumerate(radiative, 1):
        if row["published_role"] in {"D1", "D2"}:
            continue
        passed = row["inside_Rb_1sigma"] == "True"
        findings.append(Finding(
            "PR-III electromagnetic", f"monomial_{index}", "locked Rb alpha^-1 (1 sigma)",
            "SURVIVES" if passed else "REJECTED_PHYSICAL",
            f"exponents={row['exponents_p_Delta_sin2_G']}; distance={row['Rb_sigma_distance']} sigma"))
    ew = read_csv(args.output_dir / "pr4_electroweak_coefficient_outputs.csv")
    for row in ew:
        candidate = "(a,b,k)=({},{},{})".format(row["C2_charged_coefficient"], row["C2_neutral_coefficient"], row["D3_neutral_coefficient"])
        passed = row["both_inside_1sigma"] == "True"
        findings.append(Finding(
            "PR-III electroweak", candidate, "locked MW and MZ gates (both 1 sigma)",
            "SURVIVES" if passed else "REJECTED_PHYSICAL",
            f"MW distance={row['MW_sigma_distance']} sigma; MZ distance={row['MZ_sigma_distance']} sigma"))
    findings.extend([
        Finding("PR-II hypercharge", "t=0 vectorlike singlet family", "fixed nonzero charge ledger",
                "REJECTED_DERIVED", "The branch has a zero charged-fermion ledger."),
        Finding("PR-II generations", "N_gen != 3 complete replicas", "observed generation count",
                "REJECTED_PHYSICAL_CONDITIONAL", "Physical exclusion follows after the manuscript's sheet-to-generation identification."),
        Finding("PR-II generations", "N_gen=1,2,3,...", "local anomalies plus Witten parity", "SURVIVES",
                "This broader reduct omits the completed-class completeness/nonredundancy closure."),
    ])
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.outcome] = counts.get(finding.outcome, 0) + 1
    expected = {"SURVIVES": 8, "NON_DISCRIMINATING": 9, "REJECTED_PHYSICAL": 84,
                "REJECTED_DERIVED": 1, "REJECTED_PHYSICAL_CONDITIONAL": 1}
    status = "PASS" if len(findings) == 103 and counts == expected else "FAIL"
    payload = {
        "status": status, "findings_total": len(findings), "outcome_counts": counts,
        "expected_outcome_counts": expected,
        "policy": {"candidate_generation_uses_diagnostics": False, "coefficient_fitting": False,
                   "best_residual_is_selection_rule": False},
        "interpretation": "The matrix reproduces bounded diagnostic behavior. The exact PR-IV theorem is decided by completed-class closure, not residual ranking.",
        "findings": [asdict(item) for item in findings],
    }
    (args.output_dir / "pr4_branch_elimination_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with (args.output_dir / "pr4_branch_elimination_matrix.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(Finding.__dataclass_fields__))
        writer.writeheader(); writer.writerows(asdict(item) for item in findings)
    print(f"PR-IV branch-elimination control matrix: {status} ({len(findings)} rows)")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
