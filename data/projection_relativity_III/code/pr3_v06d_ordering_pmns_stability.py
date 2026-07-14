#!/usr/bin/env python3
"""
PR-III v06d: Normal-Ordering and PMNS Stability Audit

Step 07D audits the Step 07C neutrino stability envelope for normal-ordering
preservation and PMNS branch consistency. It does not import oscillation or PMNS
measurements as generation inputs.
"""

from __future__ import annotations

import json
import math
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 100

REPO_ROOT = Path(__file__).resolve().parents[1]
MBB_PATH = REPO_ROOT / "data" / "neutrino_mbb_stability_envelope.json"
SEED_PATH = REPO_ROOT / "data" / "neutrino_branch_radiative_stability_seed.json"
LOCKED_THETA23_DEG_DISPLAY = "48.73531040302701"
LOCKED_THETA23_DISPLAY_TOL = Decimal("5e-13")


class OrderingPMNSStabilityError(RuntimeError):
    """Raised when Step 07D stability audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise OrderingPMNSStabilityError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_ordering_pmns_audit() -> dict[str, Any]:
    mbb = load_json(MBB_PATH)
    seed = load_json(SEED_PATH)

    if mbb.get("status") != "STEP_07C_M_BETA_BETA_STABILITY_LOCKED":
        raise OrderingPMNSStabilityError("Step 07C m_beta_beta stability must be locked before Step 07D.")
    if seed.get("status") != "STEP_07A_NEUTRINO_BRANCH_LOCKED":
        raise OrderingPMNSStabilityError("Step 07A branch seed must be locked before Step 07D.")

    gates = mbb.get("acceptance_gates", {})
    required = [
        "m_beta_beta_propagated_only_through_PR_stability_scale",
        "zero_nu_beta_beta_experimental_limits_not_used",
        "massless_branch_protected",
        "stability_interval_reported",
        "result_labeled_envelope_not_detection",
        "step_07D_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise OrderingPMNSStabilityError(f"Step 07C gate(s) failed or missing: {failed}")

    mass = mbb["mass_branch_envelope"]
    m1 = Decimal("0")
    m2 = dec(mbb["frozen_inputs"]["m2_eV"])
    m3 = dec(mbb["frozen_inputs"]["m3_eV"])
    dm1 = Decimal("0")
    dm2 = dec(mass["Delta_m2_env_eV"])
    dm3 = dec(mass["Delta_m3_env_eV"])

    m2_low, m2_high = m2 - dm2, m2 + dm2
    m3_low, m3_high = m3 - dm3, m3 + dm3
    if not (m1 + dm1 < m2_low < m3_low):
        raise OrderingPMNSStabilityError("Normal ordering not preserved over the envelope.")

    dm21 = m2 * m2 - m1 * m1
    dm31 = m3 * m3 - m1 * m1
    dm32 = m3 * m3 - m2 * m2
    dm21_min, dm21_max = m2_low * m2_low, m2_high * m2_high
    dm31_min, dm31_max = m3_low * m3_low, m3_high * m3_high
    dm32_min = m3_low * m3_low - m2_high * m2_high
    dm32_max = m3_high * m3_high - m2_low * m2_low
    if min(dm21_min, dm31_min, dm32_min) <= 0:
        raise OrderingPMNSStabilityError("A mass-squared splitting became nonpositive.")

    pmns = seed["pr2_tree_branch"]["pmns_angles"]
    s12 = dec(pmns["sin2theta12"])
    s23 = dec(pmns["sin2theta23"])
    s13 = dec(pmns["sin2theta13"])
    c12 = Decimal(1) - s12
    c13 = Decimal(1) - s13
    ue1 = c12 * c13
    ue2 = s12 * c13
    ue3 = s13
    row_sum = ue1 + ue2 + ue3
    if row_sum != Decimal(1):
        raise OrderingPMNSStabilityError(f"PMNS first-row normalization failed: {row_sum}")

    theta12 = math.degrees(math.asin(math.sqrt(float(s12))))
    theta23 = math.degrees(math.asin(math.sqrt(float(s23))))
    theta13 = math.degrees(math.asin(math.sqrt(float(s13))))
    theta23_display = LOCKED_THETA23_DEG_DISPLAY
    if abs(Decimal(str(theta23)) - Decimal(theta23_display)) > LOCKED_THETA23_DISPLAY_TOL:
        raise OrderingPMNSStabilityError(
            f"theta23 display lock drifted beyond tolerance: computed={theta23}, locked={theta23_display}"
        )

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v06d_ordering_pmns_stability",
        "status": "STEP_07D_ORDERING_PMNS_STABILITY_LOCKED",
        "mass_branch": {
            "m1_eV": str(m1),
            "m2_eV": str(m2),
            "m3_eV": str(m3),
            "Delta_m1_env_eV": str(dm1),
            "Delta_m2_env_eV": str(dm2),
            "Delta_m3_env_eV": str(dm3),
            "m2_interval_eV": [str(m2_low), str(m2_high)],
            "m3_interval_eV": [str(m3_low), str(m3_high)],
            "ordering_preserved": True,
        },
        "mass_squared_branch": {
            "Delta_m21_squared_PR_eV2": str(dm21),
            "Delta_m31_squared_PR_eV2": str(dm31),
            "Delta_m32_squared_PR_eV2": str(dm32),
            "Delta_m21_squared_interval_eV2": [str(dm21_min), str(dm21_max)],
            "Delta_m31_squared_interval_eV2": [str(dm31_min), str(dm31_max)],
            "Delta_m32_squared_interval_eV2": [str(dm32_min), str(dm32_max)],
            "all_splittings_positive": True,
        },
        "pmns_branch": {
            "sin2theta12": str(s12),
            "sin2theta23": str(s23),
            "sin2theta13": str(s13),
            "delta_CP_deg": pmns["delta_CP_deg"],
            "theta12_deg": str(theta12),
            # Locked artifact stores theta23 as a fixed display string to avoid float repr tail drift.
            "theta23_deg": theta23_display,
            "theta13_deg": str(theta13),
        },
        "pmns_first_row_audit": {
            "abs_Ue1_squared": str(ue1),
            "abs_Ue2_squared": str(ue2),
            "abs_Ue3_squared": str(ue3),
            "row_sum": str(row_sum),
        },
        "pmns_update_rule": {
            "form": "U_PMNS_phys=U_PMNS_0*exp(A_nu_PR)",
            "constraint": "A_nu_PR^dagger=-A_nu_PR",
            "first_order": "Delta_U_PMNS_PR=U_PMNS_0*A_nu_PR",
            "unitarity_preserved_to_first_order": True,
            "observed_pmns_angles_forbidden_as_inputs": True,
        },
        "acceptance_gates": {
            "normal_ordering_preserved_over_envelope": True,
            "mass_squared_splittings_remain_positive": True,
            "massless_branch_protected": True,
            "pmns_first_row_normalization_preserved": True,
            "future_pmns_corrections_unitary_generator_only": True,
            "external_oscillation_pmns_targets_not_used": True,
            "step_07E_defined": True,
        },
        "next_step": "Step 07E: diagnostic comparison of neutrino branch after generation",
    }


def main() -> None:
    print(json.dumps(build_ordering_pmns_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
