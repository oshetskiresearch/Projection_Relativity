#!/usr/bin/env python3
"""
PR-III v06c: Effective Majorana Mass Stability

Step 07C propagates the Step 07B neutrino stability kernel into m_beta_beta as a
PR-derived stability envelope. It does not use experimental 0nu beta beta limits
or oscillation targets.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 100

REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_PATH = REPO_ROOT / "data" / "neutrino_radiative_kernel_seed.json"


class MbbStabilityError(RuntimeError):
    """Raised when Step 07C stability propagation fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise MbbStabilityError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_mbb_stability() -> dict[str, Any]:
    kernel = load_json(KERNEL_PATH)
    if kernel.get("status") != "STEP_07B_NEUTRINO_RADIATIVE_KERNEL_LOCKED":
        raise MbbStabilityError("Step 07B kernel must be locked before Step 07C.")

    gates = kernel.get("admissibility_gates", {})
    required = [
        "multiplicative_kernel_defined",
        "additive_majorana_seed_forbidden_unless_derived",
        "m1_branch_protected_at_multiplicative_order",
        "epsilon_nu_scale_recorded",
        "stability_envelope_reported_not_claimed_as_correction",
        "external_neutrino_targets_excluded",
        "step_07C_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise MbbStabilityError(f"Step 07B gate(s) failed or missing: {failed}")

    branch = kernel["frozen_branch"]
    m1 = dec(branch["m1_eV"])
    m2 = dec(branch["m2_eV"])
    m3 = dec(branch["m3_eV"])
    mbb = dec(branch["m_beta_beta_eV"])
    eps = dec(kernel["electroweak_stability_scale"]["epsilon_nu_PR"])
    eps2 = dec(kernel["electroweak_stability_scale"]["epsilon_nu_PR_squared"])

    dm1 = m1 * eps2
    dm2 = m2 * eps2
    dm3 = m3 * eps2
    dmbb = mbb * eps2
    msum = m1 + m2 + m3

    lower = mbb - dmbb
    upper = mbb + dmbb
    if lower <= 0:
        raise MbbStabilityError("m_beta_beta lower envelope must remain positive.")
    if not (m1 + dm1 <= m2 - dm2 < m3 - dm3):
        raise MbbStabilityError("Lower-envelope normal ordering failed.")

    return {
        "project": "Projection Relativity III",
        "dataset": "neutrino_mbb_stability_envelope",
        "status": "STEP_07C_M_BETA_BETA_STABILITY_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "external_neutrino_targets_used": False,
            "diagnostic_comparisons_deferred": True,
            "correction_is_envelope_not_claimed_exact": True,
        },
        "frozen_inputs": {
            "m1_eV": str(m1),
            "m2_eV": str(m2),
            "m3_eV": str(m3),
            "m_sum_eV": str(msum),
            "m_beta_beta_eV": str(mbb),
            "m_beta_beta_meV": str(mbb * Decimal("1000")),
            "epsilon_nu_PR": str(eps),
            "epsilon_nu_PR_squared": str(eps2),
        },
        "m_beta_beta_envelope": {
            "Delta_m_beta_beta_env_eV": str(dmbb),
            "Delta_m_beta_beta_env_meV": str(dmbb * Decimal("1000")),
            "lower_eV": str(lower),
            "upper_eV": str(upper),
            "lower_meV": str(lower * Decimal("1000")),
            "upper_meV": str(upper * Decimal("1000")),
            "relative_ppm": str(eps2 * Decimal("1000000")),
        },
        "mass_branch_envelope": {
            "m1_status": "protected_at_multiplicative_order",
            "Delta_m1_env_eV": str(dm1),
            "Delta_m2_env_eV": str(dm2),
            "Delta_m3_env_eV": str(dm3),
            "m_sum_upper_eV": str(msum + (dm1 + dm2 + dm3)),
            "m_sum_lower_eV": str(msum - (dm1 + dm2 + dm3)),
            "ordering_preserved": True,
        },
        "acceptance_gates": {
            "m_beta_beta_propagated_only_through_PR_stability_scale": True,
            "zero_nu_beta_beta_experimental_limits_not_used": True,
            "massless_branch_protected": True,
            "stability_interval_reported": True,
            "result_labeled_envelope_not_detection": True,
            "step_07D_defined": True,
        },
        "next_step": "Step 07D: normal-ordering and PMNS stability audit",
    }


def main() -> None:
    print(json.dumps(build_mbb_stability(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
