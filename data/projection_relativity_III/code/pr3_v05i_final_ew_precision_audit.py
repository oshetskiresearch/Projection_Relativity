#!/usr/bin/env python3
"""
PR-III v05i: Final Electroweak Precision Audit

Step 06I assigns current-precision closure status for the C2 weak ledger. It
adds no correction and does not modify generated values.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
C2_DIAG_PATH = REPO_ROOT / "data" / "electroweak_diagnostic_comparison_C2.json"


class FinalEWPrecisionAuditError(RuntimeError):
    """Raised when Step 06I final audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FinalEWPrecisionAuditError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_final_ew_audit() -> dict[str, Any]:
    c2 = load_json(C2_DIAG_PATH)
    if c2.get("status") != "STEP_06H_C2_DIAGNOSTIC_COMPARISON_LOCKED":
        raise FinalEWPrecisionAuditError("Step 06H C2 diagnostic comparison must be locked before Step 06I.")

    gates = c2.get("acceptance_gates", {})
    required = [
        "references_used_only_after_generation",
        "generated_values_not_modified",
        "all_residuals_reported",
        "W_inside_one_sigma",
        "GF_inside_one_sigma",
        "Z_inside_two_sigma",
        "C2_not_overstated_as_final_theorem",
        "remaining_neutral_channel_obligation_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise FinalEWPrecisionAuditError(f"Step 06H gate(s) failed or missing: {failed}")

    neutral_residual_gev = c2["diagnostic_residuals"]["MZ_residual_GeV"]
    neutral_residual_mev = str(Decimal(str(neutral_residual_gev)) * Decimal("1000"))

    return {
        "project": "Projection Relativity III",
        "dataset": "electroweak_final_precision_audit",
        "status": "STEP_06I_FINAL_EW_PRECISION_AUDIT_LOCKED",
        "candidate_under_audit": c2["candidate_under_audit"],
        "input_policy": {
            "references_used_after_generation_only": True,
            "generation_values_modified": False,
            "candidate_not_exact_theorem": True,
            "current_precision_status_assigned": True,
        },
        "generated_PR_values": c2["generated_PR_values"],
        "diagnostic_status": {
            "MW_residual_GeV": c2["diagnostic_residuals"]["MW_residual_GeV"],
            "MW_sigma_distance": c2["diagnostic_residuals"]["MW_sigma_distance"],
            "MW_status": "CLOSED_TO_ONE_SIGMA_DIAGNOSTIC_PRECISION",
            "MZ_residual_GeV": neutral_residual_gev,
            "MZ_sigma_distance": c2["diagnostic_residuals"]["MZ_sigma_distance"],
            "MZ_status": "CLOSED_TO_TWO_SIGMA_DIAGNOSTIC_PRECISION_NOT_ONE_SIGMA",
            "GF_residual_GeV_minus2": c2["diagnostic_residuals"]["GF_residual_GeV_minus2"],
            "GF_sigma_distance": c2["diagnostic_residuals"]["GF_sigma_distance"],
            "GF_status": "CLOSED_TO_ONE_SIGMA_DIAGNOSTIC_PRECISION",
        },
        "no_fit_provenance": {
            "allowed_generation_inputs": [
                "alpha_PR(0) from Step 05H",
                "q_bc_HR",
                "c_bc",
                "Delta_EW_HR",
                "N_gen_PR",
                "sin2thetaW_PR",
                "v_EW_PR",
                "C1 weak masses generated from PR transport",
            ],
            "excluded_generation_inputs": [
                "diagnostic W mass",
                "diagnostic Z mass",
                "diagnostic Fermi constant",
                "fitted kappa_W or kappa_Z",
                "external oblique parameters",
                "observed mixing matrices",
            ],
        },
        "closure_status_decision": {
            "EW_candidate_status": "CURRENT_PRECISION_LOCKED",
            "W_status": "closed_to_one_sigma_diagnostic_precision",
            "Z_status": "closed_to_two_sigma_diagnostic_precision",
            "GF_status": "closed_to_one_sigma_diagnostic_precision",
            "PR2_EW_obligation": "satisfied_to_current_diagnostic_precision",
            "final_exact_EW_theorem": "not_claimed",
            "step_06_status": "COMPLETE",
        },
        "remaining_obligation": {
            "neutral_channel_residual_GeV": neutral_residual_gev,
            "neutral_channel_residual_MeV": neutral_residual_mev,
            "status": "inside_two_sigma_but_outside_one_sigma",
            "future_routes": [
                "next-order neutral-vector correction",
                "scheme or matching-scale uncertainty audit",
                "weak-angle transport term coupled to C2",
                "mode-resolved neutral self-energy kernel",
                "all-orders weak-sector uncertainty theorem",
            ],
        },
        "acceptance_gates": {
            "C2_candidate_remains_no_fit": True,
            "diagnostic_references_used_only_after_generation": True,
            "W_inside_one_sigma": True,
            "GF_inside_one_sigma": True,
            "Z_inside_two_sigma": True,
            "remaining_neutral_channel_residual_reported": True,
            "current_precision_locked_not_exact_theorem": True,
            "next_stage_defined": True,
        },
        "next_step": "Step 07: neutrino branch radiative stability",
    }


def main() -> None:
    print(json.dumps(build_final_ew_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
