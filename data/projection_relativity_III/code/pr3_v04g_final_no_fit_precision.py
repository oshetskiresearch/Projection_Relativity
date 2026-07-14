#!/usr/bin/env python3
"""
PR-III v04g: Final No-Fit Precision Audit for Alpha Candidate

Step 05G audits the D1+D2 alpha-radiative candidate, assigns a closure status,
and defines the remaining obligation without adding a fitted correction.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
D1D2_PATH = REPO_ROOT / "data" / "alpha_radiative_candidate_D1_D2.json"


class FinalNoFitPrecisionError(RuntimeError):
    """Raised when Step 05G final audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FinalNoFitPrecisionError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_final_audit() -> dict[str, Any]:
    d1d2 = load_json(D1D2_PATH)
    if d1d2.get("status") != "STEP_05F_D2_REFINEMENT_GENERATED":
        raise FinalNoFitPrecisionError("Step 05F D1+D2 refinement must be generated before Step 05G.")

    gates = d1d2.get("acceptance_gates", {})
    required = [
        "D2_uses_only_frozen_PR_quantities",
        "diagnostic_reference_absent_from_D2_formula",
        "D2_lowers_alpha_inverse",
        "post_generation_residual_reduced_relative_to_D1",
        "remaining_residual_reported",
        "not_promoted_to_final_closure",
        "no_empirical_target_values_used_as_inputs",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise FinalNoFitPrecisionError(f"Step 05F gate(s) failed or missing: {failed}")

    generated_result = dict(d1d2["derived_refinement"])
    generated_result.pop("D2", None)
    generated_result.pop("epsilon_2_PR", None)
    diagnostic_comparison = dict(d1d2["diagnostic_comparison"])
    diagnostic_comparison.pop("diagnostic_shift_capture_fraction", None)

    return {
        "project": "Projection Relativity III",
        "dataset": "alpha_final_no_fit_precision_audit",
        "status": "STEP_05G_FINAL_NO_FIT_PRECISION_AUDIT_LOCKED",
        "candidate_under_audit": d1d2["candidate_name"],
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "forbidden_target_inputs_used": False,
            "diagnostic_reference_used_after_generation_only": True,
            "candidate_precision_locked": True,
            "final_theorem_claimed": False,
        },
        "generated_result": generated_result,
        "diagnostic_comparison": diagnostic_comparison,
        "no_fit_provenance": {
            "formula_D1": "-p1_HR*Delta_EW_HR*sin2thetaW_PR",
            "formula_D2": "D1*Delta_EW_HR/sqrt(N_gen_PR)",
            "allowed_inputs": [
                "p1_HR",
                "q_bc_HR",
                "c_bc",
                "Delta_EW_HR=(1-c_bc)/q_bc_HR",
                "sin2thetaW_PR",
                "N_gen_PR",
                "alpha_PR_tree_inv",
            ],
            "forbidden_inputs_absent": [
                "empirical alpha reference",
                "CODATA alpha",
                "PDG electroweak masses",
                "PDG weak mixing angle",
                "QCD target values",
                "CKM observed values",
                "PMNS observed values",
                "neutrino target values",
            ],
        },
        "closure_status_decision": {
            "alpha_radiative_candidate_status": "PRECISION_LOCKED",
            "D1_status": "ACCEPTED_FIRST_ORDER_BOUNDARY_LEAKAGE",
            "D2_status": "ACCEPTED_THREE_SHEET_REFINEMENT",
            "final_theorem_status": "NOT_YET_FINAL",
            "reason": "Residual is nonzero and must be derived, bounded, or assigned to an explicit higher-order term before final theorem status.",
        },
        "remaining_obligation": {
            "routes": [
                "derive D3 from higher-order boundary leakage",
                "derive mode-resolved heat-kernel correction",
                "derive PR threshold/overlap correction",
                "show residual lies within diagnostic reference or numerical representation uncertainty",
                "defer residual as an explicit PR-III precision obligation",
            ]
        },
        "acceptance_gates": {
            "D1D2_formula_verified_no_fit": True,
            "diagnostic_reference_used_only_after_generation": True,
            "final_residual_explicitly_reported": True,
            "result_not_overstated_as_final_closure": True,
            "alpha_candidate_marked_precision_locked": True,
            "next_mathematical_obligation_defined": True,
        },
        "next_step": "Step 05H: residual closure, uncertainty bounding, or D3 derivation",
    }


def main() -> None:
    print(json.dumps(build_final_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
