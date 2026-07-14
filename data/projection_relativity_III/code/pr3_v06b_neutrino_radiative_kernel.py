#!/usr/bin/env python3
"""
PR-III v06b: Neutrino Radiative Stability Kernel

Step 07B locks the neutrino radiative kernel architecture. It does not compute
or apply a final radiative correction.

Reproducibility note:
This generator intentionally emits the `frozen_branch` object consumed by
pr3_v06c_mbb_stability.py and present in the locked JSON artifact.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_07A_PATH = REPO_ROOT / "data" / "neutrino_branch_radiative_stability_seed.json"
EW_CLOSURE_PATH = REPO_ROOT / "data" / "electroweak_neutral_D3_candidate_C3.json"


class NeutrinoRadiativeKernelError(RuntimeError):
    """Raised when Step 07B kernel locking fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise NeutrinoRadiativeKernelError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_kernel_seed() -> dict[str, Any]:
    branch = load_json(STEP_07A_PATH)
    ew = load_json(EW_CLOSURE_PATH)

    if branch.get("status") != "STEP_07A_NEUTRINO_BRANCH_LOCKED":
        raise NeutrinoRadiativeKernelError("Step 07A branch lock must exist before Step 07B.")
    if ew.get("status") != "STEP_06J_NEUTRAL_D3_REFINEMENT_GENERATED":
        raise NeutrinoRadiativeKernelError("Step 06J electroweak closure must exist before Step 07B.")

    gates = branch.get("acceptance_gates", {})
    required = [
        "normal_ordering_branch_frozen",
        "PMNS_branch_frozen",
        "m_beta_beta_frozen",
        "radiative_correction_structure_defined",
        "m1_branch_not_manually_lifted",
        "external_neutrino_targets_excluded",
        "step_07B_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise NeutrinoRadiativeKernelError(f"Step 07A gate(s) failed or missing: {failed}")

    masses = branch["pr2_tree_branch"]["masses_eV"]
    m1 = dec(masses["m1"])
    m2 = dec(masses["m2"])
    m3 = dec(masses["m3"])
    msum = dec(masses["sum"])
    mbb = dec(branch["pr2_tree_branch"]["m_beta_beta_eV"])
    delta_ew = dec(ew["frozen_inputs"]["Delta_EW_HR"])
    n_gen = dec(ew["frozen_inputs"]["N_gen_PR"])
    eps = delta_ew / n_gen.sqrt()
    eps2 = eps * eps

    return {
        "project": "Projection Relativity III",
        "dataset": "neutrino_radiative_kernel_seed",
        "status": "STEP_07B_NEUTRINO_RADIATIVE_KERNEL_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "external_neutrino_targets_used": False,
            "diagnostic_comparisons_deferred": True,
            "radiative_correction_computed": False,
        },
        "kernel_structure": {
            "mass_correction": "Delta_m_i_PR_rad = m_i^(0)*R_nu_i_PR + S_nu_i_PR",
            "multiplicative_kernel": "R_nu_i_PR = (1/(16*pi^2))*(C_W_nu*L_W_i_PR + C_Z_nu*L_Z_i_PR + C_M_nu*L_M_i_PR)",
            "additive_seed_status": "forbidden_unless_derived_from_PR_Majorana_boundary_structure",
            "m1_branch_status": "protected_at_multiplicative_order",
        },
        "frozen_branch": {
            "m1_eV": str(m1),
            "m2_eV": str(m2),
            "m3_eV": str(m3),
            "m_sum_eV": str(msum),
            "m_beta_beta_eV": str(mbb),
            "m_beta_beta_meV": str(mbb * Decimal("1000")),
        },
        "electroweak_stability_scale": {
            "Delta_EW_HR": str(delta_ew),
            "N_gen_PR": str(n_gen),
            "epsilon_nu_PR": str(eps),
            "epsilon_nu_PR_squared": str(eps2),
        },
        "seed_stability_envelope": {
            "Delta_m2_seed_eV": str(m2 * eps2),
            "Delta_m3_seed_eV": str(m3 * eps2),
            "Delta_m_beta_beta_seed_eV": str(mbb * eps2),
            "Delta_m_beta_beta_seed_meV": str(mbb * eps2 * Decimal("1000")),
        },
        "admissibility_gates": {
            "multiplicative_kernel_defined": True,
            "additive_majorana_seed_forbidden_unless_derived": True,
            "m1_branch_protected_at_multiplicative_order": True,
            "epsilon_nu_scale_recorded": True,
            "stability_envelope_reported_not_claimed_as_correction": True,
            "external_neutrino_targets_excluded": True,
            "step_07C_defined": True,
        },
        "next_step": "Step 07C: propagate kernel into m_beta_beta stability",
    }


def main() -> None:
    print(json.dumps(build_kernel_seed(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
