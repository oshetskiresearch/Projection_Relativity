#!/usr/bin/env python3
"""
PR-III v04a: Alpha Radiative Extraction Protocol Audit

Step 05A locks the extraction convention for Delta Z_A^PR. It does not compute
the radiative coefficient. It verifies that the diagnostic residual is marked as
non-generative and that the charged-mode principle is active.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 60

REPO_ROOT = Path(__file__).resolve().parents[1]
ALPHA_POLICY_PATH = REPO_ROOT / "data" / "alpha_baseline_policy.json"
DETERMINANT_SEED_PATH = REPO_ROOT / "data" / "radiative_determinant_seed.json"

PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944")


class AlphaProtocolError(RuntimeError):
    """Raised when Step 05A protocol validation fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AlphaProtocolError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_protocol_seed() -> dict[str, Any]:
    alpha_policy = load_json(ALPHA_POLICY_PATH)
    determinant = load_json(DETERMINANT_SEED_PATH)

    if alpha_policy.get("status") != "ADOPTED_AS_PR3_TREE_BASELINE":
        raise AlphaProtocolError("Alpha baseline policy must be adopted before Step 05A.")
    if determinant.get("status") != "STEP_04_DETERMINANT_ARCHITECTURE_LOCKED":
        raise AlphaProtocolError("Step 04 determinant architecture must be locked before Step 05A.")

    tree = dec(alpha_policy["branches"]["high_resolution_tree_N15000"]["alpha_inv"])
    reference = dec(alpha_policy["branches"]["diagnostic_reference_supplied"]["alpha_inv"])
    if alpha_policy["branches"]["diagnostic_reference_supplied"].get("allowed_as_generation_input") is not False:
        raise AlphaProtocolError("Diagnostic alpha reference must be forbidden as a generation input.")

    delta_hr = tree - reference
    diagnostic_delta_alpha = -delta_hr
    diagnostic_delta_za = diagnostic_delta_alpha / (Decimal(4) * PI)

    gates = determinant.get("acceptance_gates", {})
    required = [
        "physical_hessian_imported_from_step_03",
        "gauge_null_modes_excluded",
        "photon_treated_as_external_massless_background",
        "positive_WZ_tree_masses_registered",
        "PR_trace_log_reference_normalized",
        "ghost_and_fermion_blocks_explicitly_represented",
        "no_empirical_target_values_used",
        "delta_ZA_not_inserted",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise AlphaProtocolError(f"Step 04 gate(s) failed or missing: {failed}")

    return {
        "project": "Projection Relativity III",
        "dataset": "alpha_radiative_extraction_protocol_seed",
        "status": "STEP_05A_PROTOCOL_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "forbidden_target_inputs_used": False,
            "diagnostic_residual_recorded_but_not_used": True,
        },
        "extraction_convention": {
            "effective_action_term": "DeltaGamma_PR^(1)[F] contains -1/4 DeltaZ_A^PR int d^4x F_{mu nu}F^{mu nu}",
            "alpha_shift": "Delta alpha_PR_rad_inv = 4*pi*DeltaZ_A^PR",
            "step_05A_computes_delta_ZA": False,
        },
        "gauge_convention": {
            "choice": "background_field_gauge",
            "reason": "preserves covariance of residual U(1)_em background and permits extraction of F_{mu nu}F^{mu nu} coefficient",
            "reference_normalization": "log(O) -> log(O O_ref^-1)",
            "gauge_null_policy": "Step 03 quotient remains active; gauge-fixing Goldstone partners can appear only with matching ghost terms",
        },
        "charged_mode_principle": {
            "rule": "Q_i=0 implies DeltaZ_A^(i)=0",
            "generic_formula": "DeltaZ_A^PR=sum_i sigma_i*n_i*Q_i^2*K_i^PR",
            "kernel_status": "K_i^PR deferred to Step 05C",
        },
        "preliminary_charged_sectors": [
            {"sector": "charged_weak_vectors", "modes": ["W+", "W-"], "status": "to_be_inventoried_in_step_05B"},
            {"sector": "electroweak_ghosts", "modes": ["charged W ghosts"], "status": "to_be_included_with_gauge_convention"},
            {"sector": "gauge_fixing_goldstone_partners", "modes": ["charged partners if gauge-fixed"], "status": "conditional_pair_with_ghosts"},
            {"sector": "charged_leptons", "modes": ["e", "mu", "tau"], "status": "to_be_inventoried_in_step_05B"},
            {"sector": "quarks", "modes": ["up-type", "down-type"], "status": "requires color/flavor multiplicity audit"},
            {"sector": "neutral_modes", "modes": ["photon background", "Z", "neutrinos"], "status": "no direct Q^2 contribution"},
        ],
        "diagnostic_reference": {
            "alpha_PR_tree_inv": str(tree),
            "alpha_ref_inv": str(reference),
            "delta_HR_inv": f"{delta_hr:.15f}",
            "diagnostic_Delta_alpha_rad_inv": f"{diagnostic_delta_alpha:.15f}",
            "diagnostic_Delta_ZA": f"{diagnostic_delta_za:.17f}",
            "allowed_as_generation_input": False,
        },
        "acceptance_gates": {
            "electromagnetic_extraction_convention_fixed": True,
            "background_field_gauge_selected": True,
            "gauge_null_policy_preserved": True,
            "only_charged_modes_contribute": True,
            "generic_supertrace_form_defined": True,
            "PR_spectral_kernel_deferred_to_step_05C": True,
            "diagnostic_residual_forbidden_as_input": True,
            "no_empirical_target_values_used": True,
        },
        "next_step": "Step 05B: charged-mode supertrace inventory",
    }


def main() -> None:
    print(json.dumps(build_protocol_seed(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
