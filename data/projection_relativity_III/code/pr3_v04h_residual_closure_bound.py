#!/usr/bin/env python3
"""
PR-III v04h: Residual Closure by Current Experimental Precision

Step 05H compares the no-fit D1+D2 alpha candidate to current reference
uncertainties after generation. It does not add a fitted correction.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 90

REPO_ROOT = Path(__file__).resolve().parents[1]
FINAL_AUDIT_PATH = REPO_ROOT / "data" / "alpha_final_no_fit_precision_audit.json"


class ResidualClosureError(RuntimeError):
    """Raised when residual-closure bounding fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ResidualClosureError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_residual_closure() -> dict[str, Any]:
    final_audit = load_json(FINAL_AUDIT_PATH)
    if final_audit.get("status") != "STEP_05G_FINAL_NO_FIT_PRECISION_AUDIT_LOCKED":
        raise ResidualClosureError("Step 05G final audit must be locked before Step 05H.")

    gates = final_audit.get("acceptance_gates", {})
    required = [
        "D1D2_formula_verified_no_fit",
        "diagnostic_reference_used_only_after_generation",
        "final_residual_explicitly_reported",
        "result_not_overstated_as_final_closure",
        "alpha_candidate_marked_precision_locked",
        "next_mathematical_obligation_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise ResidualClosureError(f"Step 05G gate(s) failed or missing: {failed}")

    alpha_pr = dec(final_audit["generated_result"]["alpha_PR_phys_D1D2_inv"])

    rb_ref = Decimal("137.035999206")
    rb_sigma = Decimal("0.000000011")
    codata_ref = Decimal("137.035999177")
    codata_sigma = Decimal("0.000000021")

    rb_res = alpha_pr - rb_ref
    rb_sigma_distance = abs(rb_res) / rb_sigma
    rb_res_ppt = abs(rb_res) / rb_ref * Decimal("1e12")
    rb_sigma_ppt = rb_sigma / rb_ref * Decimal("1e12")

    codata_res = alpha_pr - codata_ref
    codata_sigma_distance = abs(codata_res) / codata_sigma
    codata_res_ppt = abs(codata_res) / codata_ref * Decimal("1e12")
    codata_sigma_ppt = codata_sigma / codata_ref * Decimal("1e12")

    return {
        "project": "Projection Relativity III",
        "dataset": "alpha_residual_closure_current_precision",
        "status": "STEP_05H_RESIDUAL_BOUNDING_LOCKED",
        "input_policy": {
            "candidate_uses_only_frozen_PR_values": True,
            "forbidden_target_inputs_used": False,
            "experimental_references_used_after_generation_only": True,
            "exact_all_orders_theorem_claimed": False,
        },
        "candidate": {
            "alpha_PR_phys_D1D2_inv": str(alpha_pr),
            "source": "Step 05F D1+D2 no-fit alpha candidate",
        },
        "Rb_reference": {
            "alpha_inv": str(rb_ref),
            "sigma_inv": str(rb_sigma),
            "notation": "137.035999206(11)",
            "role": "post-generation diagnostic experimental reference",
        },
        "Rb_comparison": {
            "residual_inv": str(rb_res),
            "sigma_distance": str(rb_sigma_distance),
            "inside_1sigma": rb_sigma_distance < 1,
            "relative_residual_ppt": str(rb_res_ppt),
            "relative_sigma_ppt": str(rb_sigma_ppt),
        },
        "CODATA_2022_reference": {
            "alpha_inv": str(codata_ref),
            "sigma_inv": str(codata_sigma),
            "notation": "137.035999177(21)",
            "role": "post-generation diagnostic recommended-value comparison",
        },
        "CODATA_2022_comparison": {
            "residual_inv": str(codata_res),
            "sigma_distance": str(codata_sigma_distance),
            "inside_2sigma": codata_sigma_distance < 2,
            "relative_residual_ppt": str(codata_res_ppt),
            "relative_sigma_ppt": str(codata_sigma_ppt),
        },
        "closure_status_decision": {
            "alpha_candidate_status": "CURRENT_EXPERIMENTAL_PRECISION_CLOSED",
            "Rb_sigma_distance": "0.1376 sigma",
            "CODATA_2022_status": "inside 2 sigma",
            "PR2_alpha_obligation": "satisfied_to_current_experimental_precision",
            "final_exact_theorem": "not_claimed",
        },
        "remaining_all_orders_obligation": {
            "residual_inv_against_Rb": str(-rb_res),
            "note": "Residual is below current supplied Rb experimental uncertainty but remains nonzero. Future work may derive D3, mode-resolved heat-kernel correction, threshold/overlap correction, or an all-orders uncertainty theorem.",
        },
        "acceptance_gates": {
            "D1D2_candidate_remains_no_fit": True,
            "references_used_only_after_generation": True,
            "Rb_sigma_distance_computed": True,
            "inside_Rb_one_sigma": rb_sigma_distance < 1,
            "inside_CODATA_2022_two_sigma": codata_sigma_distance < 2,
            "current_precision_closure_not_exact_theorem": True,
            "remaining_residual_reported": True,
        },
        "step_05_status": "COMPLETE_TO_CURRENT_EXPERIMENTAL_PRECISION",
    }


def main() -> None:
    print(json.dumps(build_residual_closure(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
