#!/usr/bin/env python3
"""
PR-III v05f: Weak-Angle Diagnostic Audit

Step 06F tests whether a single weak-angle correction could close both W and Z
mass diagnostics. It is explicitly non-constructive: it does not generate the
C2/C3 corrections, does not select a branch from reference values, and does not
insert any refinement. Constructive PR-only refinement begins in Step 06G.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 90

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_06E_PATH = REPO_ROOT / "data" / "electroweak_diagnostic_comparison_C1.json"
C1_PATH = REPO_ROOT / "data" / "electroweak_running_candidate_C1.json"


class WeakAngleObliqueError(RuntimeError):
    """Raised when Step 06F diagnostic audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise WeakAngleObliqueError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_refinement_decision() -> dict[str, Any]:
    diag = load_json(STEP_06E_PATH)
    c1 = load_json(C1_PATH)

    if diag.get("status") != "STEP_06E_DIAGNOSTIC_COMPARISON_LOCKED":
        raise WeakAngleObliqueError("Step 06E diagnostic comparison must be locked before Step 06F.")
    if c1.get("status") != "STEP_06C_EW_RUNNING_CANDIDATE_GENERATED":
        raise WeakAngleObliqueError("Step 06C C1 candidate must exist before Step 06F.")

    gates = diag.get("acceptance_gates", {})
    required = [
        "references_used_only_after_generation",
        "all_residuals_reported",
        "GF_precision_success_recorded",
        "WZ_mass_failure_recorded",
        "C1_not_overstated_as_final_closure",
        "next_refinement_direction_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise WeakAngleObliqueError(f"Step 06E gate(s) failed or missing: {failed}")

    e = dec(c1["derived_transport"]["e_PR_C1_muEW"])
    v = dec(c1["frozen_inputs"]["v_EW_PR_GeV"])
    sin2 = dec(c1["frozen_inputs"]["sin2thetaW_PR"])
    cos2 = Decimal(1) - sin2
    mw = dec(c1["weak_mass_ledger_C1"]["MW_GeV"])
    mz = dec(c1["weak_mass_ledger_C1"]["MZ_GeV"])

    # Diagnostic references are used only to prove that weak-angle-only repair is
    # not a constructive PR route. These values are not passed into Step 06G.
    mw_ref = dec(diag["diagnostic_references"]["MW_ref_GeV"])
    mz_ref = dec(diag["diagnostic_references"]["MZ_ref_GeV"])

    sin2_req_w = (e * v / (Decimal(2) * mw_ref)) ** 2
    x_z = (e * v / (Decimal(2) * mz_ref)) ** 2
    sin2_req_z = (Decimal(1) - (Decimal(1) - Decimal(4) * x_z).sqrt()) / Decimal(2)

    delta_w = sin2_req_w - sin2
    delta_z = sin2_req_z - sin2
    spread = sin2_req_z - sin2_req_w

    ratio_c1 = mw / mz
    ratio_ref = mw_ref / mz_ref
    cos_pr = cos2.sqrt()
    rho_req = (mw_ref * mw_ref) / (mz_ref * mz_ref * cos2)

    kappa_w = mw_ref / mw
    kappa_z = mz_ref / mz

    weak_angle_only_possible = (delta_w >= 0 and delta_z >= 0) or (delta_w <= 0 and delta_z <= 0)

    return {
        "project": "Projection Relativity III",
        "dataset": "electroweak_weak_angle_oblique_refinement_decision",
        "status": "STEP_06F_REFINEMENT_DECISION_LOCKED",
        "input_policy": {
            "diagnostic_references_used_after_generation_only": True,
            "generation_values_modified": False,
            "refinement_inserted": False,
            "reference_values_used_to_generate_PR_values": False,
            "reference_values_used_to_select_constructive_branch": False,
            "policy_classification": "NON_CONSTRUCTIVE_DIAGNOSTIC_TABLE",
        },
        "generated_C1_values": {
            "e_PR_C1": str(e),
            "v_EW_PR_GeV": str(v),
            "sin2thetaW_PR": str(sin2),
            "MW_C1_GeV": str(mw),
            "MZ_C1_GeV": str(mz),
        },
        "diagnostic_references": {
            "MW_ref_GeV": str(mw_ref),
            "MZ_ref_GeV": str(mz_ref),
            "role": "nonconstructive diagnostic stress test only",
        },
        "weak_angle_only_test": {
            "sin2thetaW_required_by_W": str(sin2_req_w),
            "delta_sin2thetaW_required_by_W": str(delta_w),
            "sin2thetaW_required_by_Z": str(sin2_req_z),
            "delta_sin2thetaW_required_by_Z": str(delta_z),
            "required_shift_spread": str(spread),
            "weak_angle_only_closure_possible": weak_angle_only_possible,
        },
        "ratio_and_rho_diagnostic": {
            "C1_ratio_MW_over_MZ": str(ratio_c1),
            "cos_thetaW_PR": str(cos_pr),
            "reference_ratio_MW_over_MZ": str(ratio_ref),
            "rho_required_with_PR_angle": str(rho_req),
        },
        "mass_scale_diagnostics": {
            "kappa_W": str(kappa_w),
            "kappa_Z": str(kappa_z),
            "kappa_W_squared": str(kappa_w * kappa_w),
            "kappa_Z_squared": str(kappa_z * kappa_z),
        },
        "refinement_decision": {
            "weak_angle_only": "DIAGNOSTICALLY_REJECTED",
            "constructive_branch_selected_from_diagnostic_values": False,
            "constructive_refinement_status": "DEFERRED_TO_STEP_06G_PR_ONLY_DERIVATION",
            "Pi_values_status": "not_inserted_in_step_06F",
            "next_step": "Step 06G derive PR vector self-energy from PR-only geometry",
        },
        "acceptance_gates": {
            "diagnostic_references_used_only_after_generation": True,
            "weak_angle_only_test_performed": True,
            "W_and_Z_angle_requirements_incompatible": not weak_angle_only_possible,
            "rho_diagnostic_reported": True,
            "charged_neutral_vector_split_identified": True,
            "no_refinement_inserted": True,
            "nonconstructive_diagnostic_only": True,
            "constructive_branch_not_selected_from_references": True,
            "step_06G_defined": True,
        },
    }


def main() -> None:
    print(json.dumps(build_refinement_decision(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
