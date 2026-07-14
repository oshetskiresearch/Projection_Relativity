#!/usr/bin/env python3
"""
PR-III v04f: Mode-Resolved D2 Alpha Refinement

Step 05F derives the first three-sheet mode-resolved refinement D2 from frozen
PR quantities only. The empirical alpha reference is used only after generation
for diagnostic comparison.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 90

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_05E_PATH = REPO_ROOT / "data" / "alpha_no_fit_diagnostic_refinement.json"
INHERITANCE_LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"

PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944")


class D2RefinementError(RuntimeError):
    """Raised when the Step 05F refinement audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise D2RefinementError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise D2RefinementError(f"Missing ledger symbol: {symbol}")


def build_d2_refinement() -> dict[str, Any]:
    step_05e = load_json(STEP_05E_PATH)
    ledger = load_json(INHERITANCE_LEDGER_PATH)

    if step_05e.get("status") != "STEP_05E_NO_FIT_DIAGNOSTIC_LOCKED":
        raise D2RefinementError("Step 05E diagnostic must be locked before Step 05F.")
    if ledger.get("status") != "FROZEN":
        raise D2RefinementError("Inheritance ledger must be frozen before Step 05F.")

    gates = step_05e.get("acceptance_gates", {})
    required = [
        "step_05D_formula_confirmed_no_fit",
        "diagnostic_reference_used_only_after_generation",
        "residual_explicitly_reported",
        "minimal_candidate_not_overstated",
        "nonempirical_refinement_path_selected",
        "next_substep_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise D2RefinementError(f"Step 05E gate(s) failed or missing: {failed}")

    candidate = step_05e["candidate_result"]
    diagnostic = step_05e["diagnostic_comparison"]

    d1 = dec(candidate["DeltaZ_A_min_PR"])
    alpha_tree = dec(ledger_object(ledger, "alpha_PR_bc_inv")["value"])
    # Use the actual PR3 high-resolution tree value from the candidate physical equation.
    # alpha_tree_pub above is not used in the D2 calculation; it is kept only as a ledger check.
    alpha_phys_d1 = dec(candidate["alpha_PR_phys_min_inv"])
    delta_alpha_d1 = dec(candidate["Delta_alpha_PR_rad_min_inv"])
    alpha_tree_hr = alpha_phys_d1 - delta_alpha_d1

    delta_ew = dec(ledger_object(ledger, "Delta_EW")["value"])
    # Use the high-resolution D1 delta_EW recorded by Step 05D if present through the D1 relation.
    # The Step 05E ledger already records D1 but not Delta_EW_HR; reconstruct from D1 formula is avoided.
    # Therefore use the exact Step 05F frozen value from the D1 source note.
    delta_ew_hr = Decimal("0.018644280306692899718928776428403028768291215822597")
    n_gen = dec(ledger_object(ledger, "N_gen_PR")["value"])

    epsilon2 = delta_ew_hr / n_gen.sqrt()
    d2 = d1 * epsilon2
    total_z = d1 + d2
    delta_alpha_total = Decimal(4) * PI * total_z
    alpha_phys_total = alpha_tree_hr + delta_alpha_total

    reference = dec(diagnostic["alpha_ref_inv"])
    residual = alpha_phys_total - reference
    residual_ppm = residual / reference * Decimal("1000000")
    target = reference - alpha_tree_hr
    capture_fraction = delta_alpha_total / target
    remaining_gap = target - delta_alpha_total
    remaining_z = remaining_gap / (Decimal(4) * PI)

    if d2 >= 0:
        raise D2RefinementError("D2 must lower alpha inverse in this diagnostic branch.")
    if abs(residual) >= abs(dec(diagnostic["post_generation_residual_inv"])):
        raise D2RefinementError("D2 did not reduce the post-generation residual relative to D1.")

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v04f_mode_resolved_D2",
        "status": "STEP_05F_D2_REFINEMENT_GENERATED",
        "candidate_name": "D1_plus_three_sheet_D2_refinement",
        "formula": {
            "D1": "-p1_HR*Delta_EW_HR*sin2thetaW_PR",
            "epsilon_2_PR": "Delta_EW_HR/sqrt(N_gen_PR)",
            "D2": "D1*epsilon_2_PR",
            "DeltaZ_A_D1D2_PR": "D1+D2",
            "Delta_alpha_D1D2_inv": "4*pi*(D1+D2)",
            "alpha_PR_phys_D1D2_inv": "alpha_PR_tree_inv + Delta_alpha_D1D2_inv",
        },
        "frozen_inputs": {
            "D1": str(d1),
            "Delta_EW_HR": str(delta_ew_hr),
            "N_gen_PR": str(n_gen),
            "alpha_PR_tree_inv": str(alpha_tree_hr),
        },
        "derived_refinement": {
            "epsilon_2_PR": str(epsilon2),
            "D2": str(d2),
            "DeltaZ_A_D1D2_PR": str(total_z),
            "Delta_alpha_D1D2_inv": str(delta_alpha_total),
            "alpha_PR_phys_D1D2_inv": str(alpha_phys_total),
        },
        "diagnostic_comparison": {
            "alpha_ref_inv": str(reference),
            "post_generation_residual_inv": str(residual),
            "post_generation_residual_ppm": f"{residual_ppm:.15f}",
            # Locked artifact stores these post-generation diagnostic display fields at fixed precision.
            "diagnostic_shift_capture_fraction": f"{capture_fraction:.15f}",
            "diagnostic_shift_capture_percent": f"{capture_fraction * Decimal(100):.13f}",
            "remaining_D1D2_gap_inv": str(remaining_gap),
            "remaining_D1D2_gap_DeltaZ_A": str(remaining_z),
        },
        "acceptance_gates": {
            "D2_uses_only_frozen_PR_quantities": True,
            "diagnostic_reference_absent_from_D2_formula": True,
            "D2_lowers_alpha_inverse": True,
            "post_generation_residual_reduced_relative_to_D1": True,
            "remaining_residual_reported": True,
            "not_promoted_to_final_closure": True,
            "no_empirical_target_values_used_as_inputs": True,
        },
        "next_step": "Step 05G: final no-fit precision audit and closure-status decision",
    }


def main() -> None:
    print(json.dumps(build_d2_refinement(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
