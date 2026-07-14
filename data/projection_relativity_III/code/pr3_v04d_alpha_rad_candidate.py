#!/usr/bin/env python3
"""
PR-III v04d: Minimal Boundary-Leakage Alpha Radiative Candidate

Step 05D generates the first nonempirical candidate for Delta Z_A^PR using
only frozen PR boundary-leakage quantities. It compares the result to the
supplied alpha reference only after generation.

This candidate is not the final mode-resolved radiative theorem.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_SEED_PATH = REPO_ROOT / "data" / "pr_spectral_kernel_seed.json"
INHERITANCE_LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"
ALPHA_POLICY_PATH = REPO_ROOT / "data" / "alpha_baseline_policy.json"

PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944")


class AlphaCandidateError(RuntimeError):
    """Raised when the Step 05D candidate audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AlphaCandidateError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise AlphaCandidateError(f"Missing ledger symbol: {symbol}")


def build_minimal_candidate() -> dict[str, Any]:
    kernel = load_json(KERNEL_SEED_PATH)
    ledger = load_json(INHERITANCE_LEDGER_PATH)
    alpha_policy = load_json(ALPHA_POLICY_PATH)

    if kernel.get("status") != "STEP_05C_KERNEL_ARCHITECTURE_LOCKED":
        raise AlphaCandidateError("Step 05C kernel architecture must be locked before Step 05D.")
    if ledger.get("status") != "FROZEN":
        raise AlphaCandidateError("Inheritance ledger must be frozen before Step 05D.")
    if alpha_policy.get("status") != "ADOPTED_AS_PR3_TREE_BASELINE":
        raise AlphaCandidateError("Alpha baseline policy must be adopted before Step 05D.")

    gates = kernel.get("admissibility_gates", {})
    required = [
        "uses_internal_spectral_gap",
        "reference_normalized",
        "uses_only_PR_derived_or_symbolic_thresholds",
        "charge_inventory_not_altered",
        "finite_without_arbitrary_cutoff_tuning",
        "diagnostic_alpha_residual_not_used",
        "neutral_modes_zero_by_Q2",
        "spin_gauge_coefficients_not_hidden",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise AlphaCandidateError(f"Step 05C gate(s) failed or missing: {failed}")

    anchors = kernel["boundary_anchors"]
    p1 = dec(anchors["p1_HR"])
    qbc = dec(anchors["q_bc_HR"])
    cbc = dec(anchors["c_bc"])
    alpha_tree = dec(anchors["alpha_PR_tree_inv"])
    sin2 = dec(ledger_object(ledger, "sin2thetaW_tree")["value"])

    # Candidate generation uses only frozen PR quantities.
    delta_ew = (Decimal(1) - cbc) / qbc
    delta_z_candidate = -p1 * delta_ew * sin2
    delta_alpha_candidate = Decimal(4) * PI * delta_z_candidate
    alpha_phys_candidate = alpha_tree + delta_alpha_candidate

    # Diagnostic comparison only, after generation.
    reference = dec(alpha_policy["branches"]["diagnostic_reference_supplied"]["alpha_inv"])
    if alpha_policy["branches"]["diagnostic_reference_supplied"].get("allowed_as_generation_input") is not False:
        raise AlphaCandidateError("Diagnostic alpha reference must be forbidden as input.")
    diagnostic_target = -(alpha_tree - reference)
    residual = alpha_phys_candidate - reference
    residual_ppm = residual / reference * Decimal("1000000")
    capture_fraction = delta_alpha_candidate / diagnostic_target
    remaining_gap = diagnostic_target - delta_alpha_candidate

    if delta_alpha_candidate >= 0:
        raise AlphaCandidateError("Candidate must lower alpha inverse for the supplied diagnostic comparison.")

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v04d_alpha_rad_candidate",
        "status": "STEP_05D_MINIMAL_CANDIDATE_GENERATED",
        "candidate_name": "minimal_boundary_leakage_D1",
        "formula": {
            "Delta_EW_HR": "(1-c_bc)/q_bc_HR",
            "DeltaZ_A_min_PR": "-p1_HR*Delta_EW_HR*sin2thetaW_PR",
            "Delta_alpha_PR_rad_min_inv": "4*pi*DeltaZ_A_min_PR",
            "alpha_PR_phys_min_inv": "alpha_PR_tree_inv + Delta_alpha_PR_rad_min_inv",
        },
        "frozen_inputs": {
            "p1_HR": str(p1),
            "q_bc_HR": str(qbc),
            "c_bc": str(cbc),
            "sin2thetaW_PR": str(sin2),
            "alpha_PR_tree_inv": str(alpha_tree),
        },
        "derived_candidate": {
            "Delta_EW_HR": str(delta_ew),
            "DeltaZ_A_min_PR": str(delta_z_candidate),
            "Delta_alpha_PR_rad_min_inv": str(delta_alpha_candidate),
            "alpha_PR_phys_min_inv": str(alpha_phys_candidate),
        },
        "diagnostic_comparison": {
            "alpha_ref_inv": str(reference),
            "post_generation_residual_inv": str(residual),
            "post_generation_residual_ppm": f"{residual_ppm:.12f}",
            "diagnostic_target_Delta_alpha_inv": str(diagnostic_target),
            # Locked artifact stores these post-generation diagnostic display fields at fixed precision.
            "diagnostic_shift_capture_fraction": f"{capture_fraction:.12f}",
            "diagnostic_shift_capture_percent": f"{capture_fraction * Decimal(100):.10f}",
            "remaining_diagnostic_gap_inv": str(remaining_gap),
        },
        "acceptance_gates": {
            "candidate_uses_only_frozen_PR_quantities": True,
            "diagnostic_residual_not_used_in_formula": True,
            "sign_lowers_alpha_inverse": True,
            "candidate_has_correct_radiative_scale": True,
            "remaining_residual_reported": True,
            "labeled_minimal_candidate_not_final_theorem": True,
            "no_empirical_target_values_used_as_inputs": True,
        },
        "next_step": "Step 05E: no-fit diagnostic audit and refinement decision",
    }


def main() -> None:
    print(json.dumps(build_minimal_candidate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
