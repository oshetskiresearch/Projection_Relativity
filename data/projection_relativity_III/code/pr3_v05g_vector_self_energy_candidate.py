#!/usr/bin/env python3
"""
PR-III v05g: Vector Self-Energy / Oblique Candidate C2

Step 06G derives the first PR charged/neutral vector self-energy split from
frozen PR quantities only. Diagnostic mass references are deferred to Step 06H.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 90

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_06F_PATH = REPO_ROOT / "data" / "electroweak_weak_angle_oblique_refinement_decision.json"
STEP_06C_PATH = REPO_ROOT / "data" / "electroweak_running_candidate_C1.json"
LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"
KERNEL_SEED_PATH = REPO_ROOT / "data" / "pr_spectral_kernel_seed.json"


class VectorSelfEnergyCandidateError(RuntimeError):
    """Raised when Step 06G candidate generation fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise VectorSelfEnergyCandidateError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise VectorSelfEnergyCandidateError(f"Missing ledger symbol: {symbol}")


def build_c2_candidate() -> dict[str, Any]:
    step06f = load_json(STEP_06F_PATH)
    c1 = load_json(STEP_06C_PATH)
    ledger = load_json(LEDGER_PATH)
    kernel = load_json(KERNEL_SEED_PATH)

    if step06f.get("status") != "STEP_06F_REFINEMENT_DECISION_LOCKED":
        raise VectorSelfEnergyCandidateError("Step 06F refinement decision must be locked before Step 06G.")
    if c1.get("status") != "STEP_06C_EW_RUNNING_CANDIDATE_GENERATED":
        raise VectorSelfEnergyCandidateError("Step 06C C1 candidate must exist before Step 06G.")

    gates = step06f.get("acceptance_gates", {})
    required = [
        "diagnostic_references_used_only_after_generation",
        "weak_angle_only_test_performed",
        "W_and_Z_angle_requirements_incompatible",
        "rho_diagnostic_reported",
        "charged_neutral_vector_split_identified",
        "no_refinement_inserted",
        "step_06G_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise VectorSelfEnergyCandidateError(f"Step 06F gate(s) failed or missing: {failed}")

    delta_ew = (Decimal(1) - dec(kernel["boundary_anchors"]["c_bc"])) / dec(kernel["boundary_anchors"]["q_bc_HR"])
    n_gen = dec(ledger_object(ledger, "N_gen_PR")["value"])
    mw_c1 = dec(c1["weak_mass_ledger_C1"]["MW_GeV"])
    mz_c1 = dec(c1["weak_mass_ledger_C1"]["MZ_GeV"])
    sin2 = dec(ledger_object(ledger, "sin2thetaW_tree")["value"])
    cos2 = Decimal(1) - sin2

    epsilon_v = delta_ew / n_gen.sqrt()
    pi_w = (Decimal(2) / n_gen) * epsilon_v
    pi_z = -(Decimal(1) / n_gen) * epsilon_v

    if Decimal(1) + pi_w <= 0 or Decimal(1) + pi_z <= 0:
        raise VectorSelfEnergyCandidateError("Vector self-energy branch produced nonpositive mass factor.")

    mw_c2 = mw_c1 * (Decimal(1) + pi_w).sqrt()
    mz_c2 = mz_c1 * (Decimal(1) + pi_z).sqrt()
    rho_c2 = (mw_c2 * mw_c2) / (mz_c2 * mz_c2 * cos2)

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v05g_vector_self_energy_candidate",
        "status": "STEP_06G_VECTOR_SELF_ENERGY_CANDIDATE_GENERATED",
        "candidate_name": "C2_three_sheet_vector_self_energy_split",
        "formula": {
            "epsilon_V_PR": "Delta_EW_HR/sqrt(N_gen_PR)",
            "Pi_W_PR": "(2/N_gen_PR)*epsilon_V_PR",
            "Pi_Z_PR": "-(1/N_gen_PR)*epsilon_V_PR",
            "MW_C2_PR": "MW_C1_PR*sqrt(1+Pi_W_PR)",
            "MZ_C2_PR": "MZ_C1_PR*sqrt(1+Pi_Z_PR)",
            "rho_EW_C2_PR": "MW_C2_PR^2/(MZ_C2_PR^2*cos2thetaW_PR)",
        },
        "frozen_inputs": {
            "Delta_EW_HR": str(delta_ew),
            "N_gen_PR": str(n_gen),
            "MW_C1_PR_GeV": str(mw_c1),
            "MZ_C1_PR_GeV": str(mz_c1),
            "sin2thetaW_PR": str(sin2),
            "cos2thetaW_PR": str(cos2),
        },
        "derived_vector_self_energy": {
            "epsilon_V_PR": str(epsilon_v),
            "Pi_W_PR": str(pi_w),
            "Pi_Z_PR": str(pi_z),
        },
        "corrected_weak_ledger_C2": {
            "MW_C2_PR_GeV": str(mw_c2),
            "MZ_C2_PR_GeV": str(mz_c2),
            "rho_EW_C2_PR": str(rho_c2),
        },
        "acceptance_gates": {
            "Pi_terms_derived_from_frozen_PR_quantities": True,
            "diagnostic_mass_values_not_used_in_formula": True,
            "one_plus_Pi_W_positive": True,
            "one_plus_Pi_Z_positive": True,
            "corrected_masses_real_positive": True,
            "charged_neutral_split_follows_quotient_structure": True,
            "diagnostic_comparison_deferred": True,
            "C2_not_final_theorem": True,
        },
        "next_step": "Step 06H: diagnostic comparison of corrected C2 weak ledger",
    }


def main() -> None:
    print(json.dumps(build_c2_candidate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
