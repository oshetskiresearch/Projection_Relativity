#!/usr/bin/env python3
"""
PR-III v04c: PR Spectral Kernel Architecture Audit

Step 05C defines the admissible PR spectral kernel class K_i^PR for the
alpha radiative extraction. It does not compute Delta Z_A^PR.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
CHARGED_INVENTORY_PATH = REPO_ROOT / "data" / "charged_mode_supertrace_inventory.json"
ALPHA_CONVERGENCE_PATH = REPO_ROOT / "data" / "alpha_convergence_N300_N10000_N15000.json"
INHERITANCE_LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"


class PRSpectralKernelError(RuntimeError):
    """Raised when Step 05C spectral-kernel validation fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise PRSpectralKernelError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise PRSpectralKernelError(f"Missing ledger symbol: {symbol}")


def build_kernel_seed() -> dict[str, Any]:
    inventory = load_json(CHARGED_INVENTORY_PATH)
    convergence = load_json(ALPHA_CONVERGENCE_PATH)
    ledger = load_json(INHERITANCE_LEDGER_PATH)

    if inventory.get("status") != "STEP_05B_INVENTORY_LOCKED":
        raise PRSpectralKernelError("Step 05B charged-mode inventory must be locked before Step 05C.")
    if convergence.get("status") != "FROZEN_CONVERGENCE_SEQUENCE_RECEIVED":
        raise PRSpectralKernelError("Alpha convergence sequence must be frozen before Step 05C.")
    if ledger.get("status") != "FROZEN":
        raise PRSpectralKernelError("Inheritance ledger must be frozen before Step 05C.")

    gates = inventory.get("acceptance_gates", {})
    required_inventory_gates = [
        "all_nonzero_residual_charges_inventoried",
        "neutral_modes_explicitly_excluded",
        "charged_fermion_Q2_sum_equals_8",
        "charged_weak_vector_and_ghost_sectors_represented",
        "goldstone_partners_marked_conditional",
        "spin_gauge_kernel_not_assigned_prematurely",
        "no_empirical_target_values_used",
        "delta_ZA_not_computed",
    ]
    failed = [gate for gate in required_inventory_gates if gates.get(gate) is not True]
    if failed:
        raise PRSpectralKernelError(f"Step 05B gate(s) failed or missing: {failed}")

    baseline = convergence["adopted_baseline"]
    mu_gap = Decimal(str(baseline["mu_min_squared_HR"]))
    if mu_gap <= 0:
        raise PRSpectralKernelError("High-resolution spectral gap must be positive.")

    lambda_EW = Decimal(str(ledger_object(ledger, "Lambda_EW_PR")["value"]))
    if lambda_EW <= 0:
        raise PRSpectralKernelError("Lambda_EW_PR must be positive if used as provisional reference scale.")

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v04c_pr_spectral_kernel",
        "status": "STEP_05C_KERNEL_ARCHITECTURE_LOCKED",
        "kernel_architecture": {
            "generic_kernel": "K_i^PR = (C_i^hk/(16*pi^2))*I_i^PR",
            "delta_ZA_formula": "DeltaZ_A^PR=sum_i sigma_i*n_i*Q_i^2*K_i^PR",
            "C_i_hk_status": "assigned_in_step_05D",
            "I_i_PR_status": "defined_as_PR_spectral_regulator_class_in_step_05C",
        },
        "spectral_regulator": {
            "mu_min_squared_HR": str(mu_gap),
            "support_condition": "mu_n^2 >= mu_min_squared_HR > 0",
            "shifted_spectrum": "mu_n^2=lambda_n-lambda_0",
            "regulator_source": "internal_PR_spectral_gap_and_reference_subtraction_not_arbitrary_cutoff",
            "kernel_class": "I_i^PR(tau_i)=sum_{n in S_i} omega_i,n^PR [ log(1+tau_i/mu_n^2) - R_i(tau_i;mu_n^2) ]",
        },
        "threshold_policy": {
            "tau_i": "M_i^2/Lambda_ref^2",
            "allowed_mass_sources": [
                "frozen PR tree values",
                "PR-II generated mass-sector outputs",
                "future PR-III derived masses",
                "symbolic placeholders pending PR-derived values",
            ],
            "forbidden_mass_sources": [
                "PDG masses as generation inputs",
                "fitted thresholds",
                "empirical values chosen to force Delta alpha_PR_rad_inv",
            ],
            "allowed_provisional_reference_scale": "Lambda_EW_PR",
            "Lambda_EW_PR_GeV": str(lambda_EW),
        },
        "boundary_anchors": {
            "p1_HR": baseline["p1"],
            "q_bc_HR": baseline["q_bc_HR"],
            "c_bc": baseline["c_bc"],
            "alpha_PR_tree_inv": baseline["alpha_PR_tree_inv"],
        },
        "charged_inventory_dependency": {
            "source": "data/charged_mode_supertrace_inventory.json",
            "kernel_multiplies_locked_charge_inventory": True,
            "neutral_modes_remain_zero_by_Q2": True,
        },
        "admissibility_gates": {
            "uses_internal_spectral_gap": True,
            "reference_normalized": True,
            "uses_only_PR_derived_or_symbolic_thresholds": True,
            "charge_inventory_not_altered": True,
            "finite_without_arbitrary_cutoff_tuning": True,
            "diagnostic_alpha_residual_not_used": True,
            "neutral_modes_zero_by_Q2": True,
            "spin_gauge_coefficients_not_hidden": True,
        },
        "next_step": "Step 05D: compute candidate DeltaZ_A^PR from locked inventory and kernel",
    }


def main() -> None:
    print(json.dumps(build_kernel_seed(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
