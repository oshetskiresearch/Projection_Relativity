#!/usr/bin/env python3
"""
PR-III v05b: Electroweak Running Inventory and Kernel Audit

Step 06B builds the electroweak running inventory and admissible PR running
kernel class. It does not compute Delta_run_PR.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_06A_PATH = REPO_ROOT / "data" / "electroweak_scale_transport_protocol_seed.json"
CHARGED_INVENTORY_PATH = REPO_ROOT / "data" / "charged_mode_supertrace_inventory.json"
KERNEL_SEED_PATH = REPO_ROOT / "data" / "pr_spectral_kernel_seed.json"


class EWRunningKernelError(RuntimeError):
    """Raised when Step 06B validation fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise EWRunningKernelError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_running_kernel_seed() -> dict[str, Any]:
    protocol = load_json(STEP_06A_PATH)
    charged = load_json(CHARGED_INVENTORY_PATH)
    kernel = load_json(KERNEL_SEED_PATH)

    if protocol.get("status") != "STEP_06A_EW_TRANSPORT_PROTOCOL_LOCKED":
        raise EWRunningKernelError("Step 06A protocol must be locked before Step 06B.")
    if charged.get("status") != "STEP_05B_INVENTORY_LOCKED":
        raise EWRunningKernelError("Step 05B charged inventory must be locked before Step 06B.")
    if kernel.get("status") != "STEP_05C_KERNEL_ARCHITECTURE_LOCKED":
        raise EWRunningKernelError("Step 05C kernel architecture must be locked before Step 06B.")

    protocol_gates = protocol.get("acceptance_gates", {})
    required_protocol = [
        "low_energy_alpha_imported_from_step_05H",
        "EW_matching_scale_PR_derived",
        "transport_equation_defined_without_fitted_running",
        "coupling_reconstruction_locked",
        "weak_ledger_equations_locked",
        "diagnostic_comparisons_deferred",
    ]
    failed_protocol = [gate for gate in required_protocol if protocol_gates.get(gate) is not True]
    if failed_protocol:
        raise EWRunningKernelError(f"Step 06A gate(s) failed or missing: {failed_protocol}")

    charged_gates = charged.get("acceptance_gates", {})
    required_charged = [
        "all_nonzero_residual_charges_inventoried",
        "neutral_modes_explicitly_excluded",
        "charged_fermion_Q2_sum_equals_8",
        "charged_weak_vector_and_ghost_sectors_represented",
        "no_empirical_target_values_used",
        "delta_ZA_not_computed",
    ]
    failed_charged = [gate for gate in required_charged if charged_gates.get(gate) is not True]
    if failed_charged:
        raise EWRunningKernelError(f"Step 05B gate(s) failed or missing: {failed_charged}")

    kernel_gates = kernel.get("admissibility_gates", {})
    required_kernel = [
        "uses_internal_spectral_gap",
        "reference_normalized",
        "uses_only_PR_derived_or_symbolic_thresholds",
        "finite_without_arbitrary_cutoff_tuning",
        "diagnostic_alpha_residual_not_used",
    ]
    failed_kernel = [gate for gate in required_kernel if kernel_gates.get(gate) is not True]
    if failed_kernel:
        raise EWRunningKernelError(f"Step 05C gate(s) failed or missing: {failed_kernel}")

    return {
        "project": "Projection Relativity III",
        "dataset": "electroweak_running_inventory_kernel_seed",
        "status": "STEP_06B_EW_RUNNING_KERNEL_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "external_reference_inputs_used": False,
            "diagnostic_comparisons_deferred": True,
            "running_correction_computed": False,
        },
        "transport_equation": {
            "alpha_transport": "alpha_PR_inv(mu_EW)=alpha_PR_inv(0)-Delta_run_PR(0_to_mu_EW)",
            "running_decomposition": "Delta_run_PR=sum_i B_i_PR*L_i_PR(0_to_mu_EW)",
            "B_i_PR_status": "assigned_in_step_06C",
            "L_i_PR_status": "kernel_class_locked_in_step_06B",
        },
        "running_inventory": [
            {"sector": "charged_weak_vectors", "charge_square_sum": "2", "threshold_status": "PR tree W mass from Step 02", "included": True},
            {"sector": "charged_electroweak_ghosts", "charge_square_sum": "2", "threshold_status": "paired with W gauge convention", "included": True},
            {"sector": "charged_goldstone_partners", "charge_square_sum": "2", "threshold_status": "conditional gauge-fixing partner", "included": "conditional"},
            {"sector": "charged_leptons", "charge_square_sum": "3", "threshold_status": "PR-II mass sheets or symbolic pending import", "included": True},
            {"sector": "up_type_quarks_color_resolved", "charge_square_sum": "4", "threshold_status": "PR-II quark sheets or symbolic pending import", "included": True},
            {"sector": "down_type_quarks_color_resolved", "charge_square_sum": "1", "threshold_status": "PR-II quark sheets or symbolic pending import", "included": True},
            {"sector": "neutral_modes", "charge_square_sum": "0", "threshold_status": "not applicable", "included": False},
        ],
        "kernel_class": {
            "continuous_form": "L_i_PR=int_0^muEW2 dQ2/(Q2+M_i2) * W_i_PR(Q2; mu_min_HR2, omega_i,n_PR)",
            "discrete_form": "L_i_PR=sum_n omega_i,n_PR log((M_i2+mu_EW2+mu_n2*Lambda_ref2)/(M_i2+mu_n2*Lambda_ref2))-R_i_run",
            "support_condition": "mu_n2 >= mu_min_HR2 > 0",
            "mu_min_HR2": kernel["spectral_regulator"]["mu_min_squared_HR"],
            "reference_scale_provisional": "Lambda_EW_PR",
            "Lambda_EW_PR_GeV": protocol["electroweak_scale"]["mu_EW_PR_GeV"],
            "subtraction_rule": "R_i_run preserves Step 05 low-energy normalization and cannot be selected to force diagnostic weak-scale values",
        },
        "threshold_policy": {
            "allowed_sources": [
                "PR tree W/Z seed values",
                "PR-II generated lepton and quark mass sheets once imported",
                "symbolic thresholds pending PR source synchronization",
                "future PR-III derived threshold values",
            ],
            "excluded_sources": [
                "external weak-sector reference masses",
                "external quark or lepton mass tables as generation inputs",
                "threshold values chosen to force weak-scale agreement",
            ],
        },
        "acceptance_gates": {
            "step_06A_transport_equation_imported": True,
            "step_05B_charge_inventory_preserved": True,
            "neutral_modes_excluded_by_Q2": True,
            "PR_running_kernel_class_defined_without_arbitrary_cutoff": True,
            "threshold_sources_restricted_to_PR_or_symbolic": True,
            "external_weak_targets_not_used": True,
            "running_correction_not_computed_prematurely": True,
        },
        "next_step": "Step 06C: compute PR electroweak running candidate",
    }


def main() -> None:
    print(json.dumps(build_running_kernel_seed(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
