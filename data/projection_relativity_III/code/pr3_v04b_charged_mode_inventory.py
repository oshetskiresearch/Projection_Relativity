#!/usr/bin/env python3
"""
PR-III v04b: Charged-Mode Supertrace Inventory Audit

Step 05B constructs the charged-mode inventory for the electromagnetic
radiative extraction. It locks charge-square sums and mode status, but does not
compute the PR spectral kernel K_i^PR or Delta Z_A^PR.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = REPO_ROOT / "data" / "alpha_radiative_extraction_protocol_seed.json"


class ChargedInventoryError(RuntimeError):
    """Raised when the charged-mode inventory audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ChargedInventoryError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def q2_sum(charges: list[Fraction], degeneracies: list[int] | None = None) -> Fraction:
    if degeneracies is None:
        degeneracies = [1 for _ in charges]
    if len(charges) != len(degeneracies):
        raise ChargedInventoryError("charges and degeneracies must have the same length")
    return sum(Fraction(deg) * q * q for q, deg in zip(charges, degeneracies))


def build_charged_inventory() -> dict[str, Any]:
    protocol = load_json(PROTOCOL_PATH)
    if protocol.get("status") != "STEP_05A_PROTOCOL_LOCKED":
        raise ChargedInventoryError("Step 05A protocol must be locked before Step 05B.")

    gates = protocol.get("acceptance_gates", {})
    required = [
        "electromagnetic_extraction_convention_fixed",
        "background_field_gauge_selected",
        "gauge_null_policy_preserved",
        "only_charged_modes_contribute",
        "generic_supertrace_form_defined",
        "PR_spectral_kernel_deferred_to_step_05C",
        "diagnostic_residual_forbidden_as_input",
        "no_empirical_target_values_used",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise ChargedInventoryError(f"Step 05A gate(s) failed or missing: {failed}")

    charged_weak_vector = q2_sum([Fraction(1), Fraction(-1)])
    charged_ghost = q2_sum([Fraction(1), Fraction(-1)])
    charged_goldstone = q2_sum([Fraction(1), Fraction(-1)])
    charged_lepton = q2_sum([Fraction(-1), Fraction(-1), Fraction(-1)])
    up_quarks = q2_sum([Fraction(2, 3)], [9])
    down_quarks = q2_sum([Fraction(-1, 3)], [9])
    fermion_total = charged_lepton + up_quarks + down_quarks
    per_generation = Fraction(1) + Fraction(4, 3) + Fraction(1, 3)

    if charged_weak_vector != 2:
        raise ChargedInventoryError("W charge-square audit failed")
    if charged_ghost != 2:
        raise ChargedInventoryError("Ghost charge-square audit failed")
    if charged_goldstone != 2:
        raise ChargedInventoryError("Goldstone charge-square audit failed")
    if charged_lepton != 3:
        raise ChargedInventoryError("Charged-lepton charge-square audit failed")
    if up_quarks != 4:
        raise ChargedInventoryError("Up-quark charge-square audit failed")
    if down_quarks != 1:
        raise ChargedInventoryError("Down-quark charge-square audit failed")
    if fermion_total != 8:
        raise ChargedInventoryError("Charged-fermion total charge-square audit failed")
    if per_generation != Fraction(8, 3):
        raise ChargedInventoryError("Per-generation charge-square audit failed")

    return {
        "project": "Projection Relativity III",
        "dataset": "charged_mode_supertrace_inventory",
        "status": "STEP_05B_INVENTORY_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "forbidden_target_inputs_used": False,
            "empirical_targets_allowed_as_diagnostics_only": True,
        },
        "generic_formula": "DeltaZ_A^PR = sum_i sigma_i*n_i*Q_i^2*K_i^PR",
        "kernel_status": "K_i^PR deferred to Step 05C",
        "supertrace_sign_convention": {
            "real_bosonic_scalar": "+1/2",
            "vector_boson_block": "+1/2 with vector kernel carrying spin/gauge structure",
            "ghost_block": "-1",
            "Dirac_fermion_block": "-1",
        },
        "charged_mode_inventory": [
            {
                "sector": "charged_weak_vectors",
                "modes": ["W+", "W-"],
                "charges": ["+1", "-1"],
                "charge_square_sum": str(charged_weak_vector),
                "raw_determinant_sign": "+1/2 vector kernel",
                "status": "included",
                "notes": "Vector spin/gauge structure deferred to K_vector^PR.",
            },
            {
                "sector": "charged_electroweak_ghosts",
                "modes": ["c+", "c-"],
                "charges": ["+1", "-1"],
                "charge_square_sum": str(charged_ghost),
                "raw_determinant_sign": "-1 ghost kernel",
                "status": "included_with_background_field_gauge",
                "notes": "Must accompany charged weak vector block.",
            },
            {
                "sector": "charged_goldstone_gauge_fixing_partners",
                "modes": ["phi+", "phi-"],
                "charges": ["+1", "-1"],
                "charge_square_sum": str(charged_goldstone),
                "raw_determinant_sign": "+1/2 scalar kernel",
                "status": "conditional_gauge_fixing_partner",
                "notes": "Step 03 quotient removes these as physical scalar modes; gauge-fixing can reintroduce only with ghost terms.",
            },
            {
                "sector": "charged_leptons",
                "modes": ["e", "mu", "tau"],
                "charges": ["-1", "-1", "-1"],
                "charge_square_sum": str(charged_lepton),
                "raw_determinant_sign": "-1 fermion kernel",
                "status": "included",
                "notes": "Three charged-lepton projection sheets inherited from PR-II.",
            },
            {
                "sector": "up_type_quarks_color_resolved",
                "modes": ["u", "c", "t"],
                "charge": "+2/3",
                "generations": 3,
                "colors": 3,
                "charge_square_sum": str(up_quarks),
                "raw_determinant_sign": "-1 fermion kernel",
                "status": "included_for_electromagnetic_charge_counting",
                "notes": "Strong thresholds and running deferred to strong-sector modules.",
            },
            {
                "sector": "down_type_quarks_color_resolved",
                "modes": ["d", "s", "b"],
                "charge": "-1/3",
                "generations": 3,
                "colors": 3,
                "charge_square_sum": str(down_quarks),
                "raw_determinant_sign": "-1 fermion kernel",
                "status": "included_for_electromagnetic_charge_counting",
                "notes": "Strong thresholds and running deferred to strong-sector modules.",
            },
        ],
        "neutral_exclusions": [
            {"mode": "photon_background", "Q": "0 self-charge in abelian extraction", "status": "external_background_not_loop_self_charge"},
            {"mode": "Z", "Q": "0", "status": "excluded_from_direct_Q2_contribution"},
            {"mode": "neutrinos", "Q": "0", "status": "excluded_from_direct_Q2_contribution"},
            {"mode": "radial_scalar_h_A", "Q": "0 unless charged projection kernel later derived", "status": "excluded_from_current_direct_Q2_contribution"},
            {"mode": "gluons", "Q": "0 under U(1)_em", "status": "strong_sector_deferred"},
        ],
        "charge_square_audits": {
            "charged_weak_vector_Q2_sum": str(charged_weak_vector),
            "charged_ghost_Q2_sum": str(charged_ghost),
            "charged_goldstone_conditional_Q2_sum": str(charged_goldstone),
            "charged_lepton_Q2_sum": str(charged_lepton),
            "up_type_quark_color_Q2_sum": str(up_quarks),
            "down_type_quark_color_Q2_sum": str(down_quarks),
            "charged_fermion_total_Q2_sum": str(fermion_total),
            "per_generation_charged_fermion_Q2_sum": str(per_generation),
        },
        "acceptance_gates": {
            "all_nonzero_residual_charges_inventoried": True,
            "neutral_modes_explicitly_excluded": True,
            "charged_fermion_Q2_sum_equals_8": True,
            "charged_weak_vector_and_ghost_sectors_represented": True,
            "goldstone_partners_marked_conditional": True,
            "spin_gauge_kernel_not_assigned_prematurely": True,
            "no_empirical_target_values_used": True,
            "delta_ZA_not_computed": True,
        },
        "next_step": "Step 05C: define PR spectral kernel K_i^PR",
    }


def main() -> None:
    print(json.dumps(build_charged_inventory(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
