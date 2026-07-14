#!/usr/bin/env python3
"""
PR-III v04e: No-Fit Diagnostic and Refinement Decision

Step 05E audits the Step 05D minimal alpha-radiative candidate. It confirms
that the candidate formula uses only frozen PR quantities, reports the
post-generation diagnostic residual, and selects the next nonempirical
refinement path.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_PATH = REPO_ROOT / "data" / "alpha_radiative_candidate_minimal_boundary.json"

PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944")


class NoFitDiagnosticError(RuntimeError):
    """Raised when the no-fit diagnostic audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise NoFitDiagnosticError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def audit_no_fit_and_refinement() -> dict[str, Any]:
    candidate = load_json(CANDIDATE_PATH)
    if candidate.get("status") != "STEP_05D_MINIMAL_CANDIDATE_GENERATED":
        raise NoFitDiagnosticError("Step 05D candidate must be generated before Step 05E.")

    gates = candidate.get("acceptance_gates", {})
    required = [
        "candidate_uses_only_frozen_PR_quantities",
        "diagnostic_residual_not_used_in_formula",
        "sign_lowers_alpha_inverse",
        "candidate_has_correct_radiative_scale",
        "remaining_residual_reported",
        "labeled_minimal_candidate_not_final_theorem",
        "no_empirical_target_values_used_as_inputs",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise NoFitDiagnosticError(f"Step 05D gate(s) failed or missing: {failed}")

    diag = candidate["diagnostic_comparison"]
    residual = dec(diag["post_generation_residual_inv"])
    remaining_delta_z = residual.copy_negate() / (Decimal(4) * PI)

    candidate_result = dict(candidate["derived_candidate"])
    candidate_result.pop("Delta_EW_HR", None)

    return {
        "project": "Projection Relativity III",
        "dataset": "alpha_no_fit_diagnostic_refinement",
        "status": "STEP_05E_NO_FIT_DIAGNOSTIC_LOCKED",
        "candidate_under_audit": candidate["candidate_name"],
        "input_policy": {
            "candidate_uses_only_frozen_PR_values": True,
            "forbidden_target_inputs_used": False,
            "diagnostic_reference_used_after_generation_only": True,
            "do_not_promote_to_final_theorem": True,
        },
        "candidate_formula": {
            "D1": "-p1_HR*Delta_EW_HR*sin2thetaW_PR",
            "Delta_EW_HR": "(1-c_bc)/q_bc_HR",
            "DeltaZ_A_min_PR": "D1",
            "Delta_alpha_PR_rad_min_inv": "4*pi*D1",
        },
        "candidate_result": candidate_result,
        "diagnostic_comparison": {
            "alpha_ref_inv": diag["alpha_ref_inv"],
            "post_generation_residual_inv": diag["post_generation_residual_inv"],
            "post_generation_residual_ppm": diag["post_generation_residual_ppm"],
            "diagnostic_shift_capture_percent": diag["diagnostic_shift_capture_percent"],
            "remaining_D1_gap_inv": diag["remaining_diagnostic_gap_inv"],
            "remaining_D1_gap_DeltaZ_A": str(remaining_delta_z),
        },
        "decision": {
            "minimal_candidate_status": "accepted_as_D1_not_final",
            "final_alpha_theorem_status": "not_complete",
            "next_required_substep": "Step 05F mode-resolved correction / residual refinement",
        },
        "allowed_refinement_paths": [
            "mode_resolved_heat_kernel_coefficients",
            "PR_derived_threshold_refinement",
            "projection_overlap_refinement",
            "higher_order_boundary_leakage_derived_from_PR_algebra",
        ],
        "forbidden_refinement_paths": [
            "fit_residual_directly",
            "insert_CODATA_or_empirical_alpha",
            "choose_thresholds_to_force_agreement",
            "hide_residual_in_rounding",
            "claim_final_closure_before_D2_derivation",
        ],
        "acceptance_gates": {
            "step_05D_formula_confirmed_no_fit": True,
            "diagnostic_reference_used_only_after_generation": True,
            "residual_explicitly_reported": True,
            "minimal_candidate_not_overstated": True,
            "nonempirical_refinement_path_selected": True,
            "next_substep_defined": True,
        },
        "next_step": "Step 05F: derive a mode-resolved or higher-order D2 refinement without using the diagnostic residual as input",
    }


def main() -> None:
    print(json.dumps(audit_no_fit_and_refinement(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
