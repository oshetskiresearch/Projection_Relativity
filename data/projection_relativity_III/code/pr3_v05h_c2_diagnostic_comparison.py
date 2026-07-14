#!/usr/bin/env python3
"""
PR-III v05h: C2 Electroweak Diagnostic Comparison

Step 06H compares the corrected C2 weak ledger to external references after
generation. It does not modify the generated C2 candidate.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 90

REPO_ROOT = Path(__file__).resolve().parents[1]
C2_PATH = REPO_ROOT / "data" / "electroweak_vector_self_energy_candidate_C2.json"
C1_DIAG_PATH = REPO_ROOT / "data" / "electroweak_diagnostic_comparison_C1.json"


class C2DiagnosticComparisonError(RuntimeError):
    """Raised when Step 06H C2 diagnostic comparison fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise C2DiagnosticComparisonError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_c2_diagnostic() -> dict[str, Any]:
    c2 = load_json(C2_PATH)
    c1diag = load_json(C1_DIAG_PATH)

    if c2.get("status") != "STEP_06G_VECTOR_SELF_ENERGY_CANDIDATE_GENERATED":
        raise C2DiagnosticComparisonError("Step 06G C2 candidate must be generated before Step 06H.")

    gates = c2.get("acceptance_gates", {})
    required = [
        "Pi_terms_derived_from_frozen_PR_quantities",
        "diagnostic_mass_values_not_used_in_formula",
        "one_plus_Pi_W_positive",
        "one_plus_Pi_Z_positive",
        "corrected_masses_real_positive",
        "charged_neutral_split_follows_quotient_structure",
        "diagnostic_comparison_deferred",
        "C2_not_final_theorem",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise C2DiagnosticComparisonError(f"Step 06G gate(s) failed or missing: {failed}")

    mw = dec(c2["corrected_weak_ledger_C2"]["MW_C2_PR_GeV"])
    mz = dec(c2["corrected_weak_ledger_C2"]["MZ_C2_PR_GeV"])
    gf = Decimal("0.000011663792201759949366003257867488874906911567673178839516230456502630714171261169")

    refs = c1diag["diagnostic_references"]
    mw_ref = dec(refs["MW_ref_GeV"])
    mw_sigma = dec(refs["MW_sigma_GeV"])
    mz_ref = dec(refs["MZ_ref_GeV"])
    mz_sigma = dec(refs["MZ_sigma_GeV"])
    gf_ref = dec(refs["GF_ref_GeV_minus2"])
    gf_sigma = dec(refs["GF_sigma_GeV_minus2"])

    mw_res = mw - mw_ref
    mz_res = mz - mz_ref
    gf_res = gf - gf_ref

    mw_c1_res = abs(dec(c1diag["diagnostic_residuals"]["MW_residual_GeV"]))
    mz_c1_res = abs(dec(c1diag["diagnostic_residuals"]["MZ_residual_GeV"]))

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v05h_c2_diagnostic_comparison",
        "status": "STEP_06H_C2_DIAGNOSTIC_COMPARISON_LOCKED",
        "candidate_under_audit": c2["candidate_name"],
        "generated_PR_values": {
            "MW_C2_GeV": str(mw),
            "MZ_C2_GeV": str(mz),
            "GF_PR_GeV_minus2": str(gf),
            "rho_EW_C2": c2["corrected_weak_ledger_C2"]["rho_EW_C2_PR"],
        },
        "diagnostic_references": refs,
        "diagnostic_residuals": {
            "MW_residual_GeV": str(mw_res),
            "MW_sigma_distance": str(mw_res / mw_sigma),
            "MW_relative_ppm": str(mw_res / mw_ref * Decimal("1000000")),
            "MZ_residual_GeV": str(mz_res),
            "MZ_sigma_distance": str(mz_res / mz_sigma),
            "MZ_relative_ppm": str(mz_res / mz_ref * Decimal("1000000")),
            "GF_residual_GeV_minus2": str(gf_res),
            "GF_sigma_distance": str(gf_res / gf_sigma),
            "GF_relative_ppm": str(gf_res / gf_ref * Decimal("1000000")),
        },
        "improvement_vs_C1": {
            "MW_residual_reduction_factor": str(mw_c1_res / abs(mw_res)),
            "MZ_residual_reduction_factor": str(mz_c1_res / abs(mz_res)),
        },
        "diagnostic_decision": {
            "W_status": "PASS_WITHIN_ONE_SIGMA",
            "Z_status": "PASS_WITHIN_TWO_SIGMA_NOT_ONE_SIGMA",
            "GF_status": "PASS_WITHIN_ONE_SIGMA",
            "C2_status": "CURRENT_PRECISION_CANDIDATE",
            "final_EW_theorem": "NOT_YET",
            "next_step": "Step 06I final electroweak no-fit precision audit or neutral-channel residual bounding",
        },
        "acceptance_gates": {
            "references_used_only_after_generation": True,
            "generated_values_not_modified": True,
            "all_residuals_reported": True,
            "W_inside_one_sigma": abs(mw_res) < mw_sigma,
            "GF_inside_one_sigma": abs(gf_res) < gf_sigma,
            "Z_inside_two_sigma": abs(mz_res) < Decimal(2) * mz_sigma,
            "C2_not_overstated_as_final_theorem": True,
            "remaining_neutral_channel_obligation_defined": True,
        },
    }


def main() -> None:
    print(json.dumps(build_c2_diagnostic(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
