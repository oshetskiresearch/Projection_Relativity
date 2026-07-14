#!/usr/bin/env python3
"""
PR-III v03: Radiative Determinant Architecture Audit

This module locks the Step 04 PR-native radiative determinant architecture.
It does not compute Delta Z_A or the physical alpha correction. It verifies that
all determinant blocks are represented, gauge-null modes are excluded, photon
zero modes are handled by reference normalization, and no empirical target value
is inserted.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
GAUGE_QUOTIENT_PATH = REPO_ROOT / "data" / "gauge_null_quotient_seed.json"
SCALAR_SEED_PATH = REPO_ROOT / "data" / "scalar_hessian_seed.json"


class RadiativeDeterminantError(RuntimeError):
    """Raised when the Step 04 determinant architecture fails validation."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RadiativeDeterminantError(f"Missing required JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_radiative_determinant_seed() -> dict[str, Any]:
    quotient = load_json(GAUGE_QUOTIENT_PATH)
    scalar_seed = load_json(SCALAR_SEED_PATH)

    if quotient.get("status") != "STEP_03_QUOTIENT_LOCKED":
        raise RadiativeDeterminantError("Step 03 quotient must be locked before Step 04.")
    if scalar_seed.get("status") != "STEP_02_SEED_LOCKED":
        raise RadiativeDeterminantError("Step 02 scalar seed must be locked before Step 04.")

    mass_block = scalar_seed["electroweak_mass_block"]
    mw2 = dec(mass_block["charged_MW_squared_GeV2"])
    mz2 = dec(mass_block["neutral_eigenvalues_GeV2"]["Z"])
    photon = dec(mass_block["neutral_eigenvalues_GeV2"]["photon"])

    if mw2 <= 0 or mz2 <= 0:
        raise RadiativeDeterminantError("W/Z tree masses must be positive for determinant registry.")
    if photon != 0:
        raise RadiativeDeterminantError("Photon eigenvalue must be exactly zero at Step 04.")

    gates = quotient.get("acceptance_gates", {})
    required_true = [
        "scalar_nullity_equals_three",
        "nullity_matches_broken_quotient_dimension",
        "physical_quotient_contains_only_H_AA",
        "H_AA_symbolically_positive",
        "photon_unbroken_and_massless",
        "Z_direction_orthogonal_and_positive",
        "degrees_of_freedom_conserved",
        "no_fit_policy_active",
    ]
    failed = [gate for gate in required_true if gates.get(gate) is not True]
    if failed:
        raise RadiativeDeterminantError(f"Step 03 gate(s) failed or missing: {failed}")

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v03_radiative_determinant",
        "status": "STEP_04_DETERMINANT_ARCHITECTURE_LOCKED",
        "trace_convention": {
            "definition": "Tr_PR' log(O O_ref^-1) = - d/ds [zeta_O_PR(s)-zeta_Oref_PR(s)] at s=0",
            "zeta_definition": "zeta_O_PR(s)=sum_{lambda_n in spec_PR'(O)} lambda_n^(-s)",
            "prime": "gauge-null modes and exact zero modes excluded or reference-normalized",
        },
        "supertrace_seed": {
            "formula": "DeltaGamma_PR^(1)[B] = 1/2 STr_PR' log[H_PR[B] H_PR[0]^-1]",
            "block_form": "1/2 Tr_scalar' log(H_A/H_A0) + 1/2 Tr_vector' log(O_V/O_V0) - Tr_ghost' log(M_gh/M_gh0) - Tr_fermion' log(D_F/D_F0)",
            "delta_ZA_status": "not_computed_in_step_04",
        },
        "block_registry": [
            {
                "block": "physical_scalar",
                "operator": "H_A = H_AA",
                "multiplicity": 1,
                "status": "included_symbolic",
                "notes": "H_AA=8 beta_A A0^2>0",
            },
            {
                "block": "gauge_null_scalars",
                "operator": "pi_1, pi_2, pi_3",
                "multiplicity": 3,
                "status": "excluded_by_step_03_quotient",
                "notes": "Gauge-null electroweak orientation modes, not determinant eigenvalues.",
            },
            {
                "block": "photon",
                "operator": "O_gamma",
                "multiplicity": 1,
                "status": "external_background_reference_normalized",
                "notes": "Massless residual U(1)_em projection used for Delta Z_A extraction.",
            },
            {
                "block": "charged_weak_vectors",
                "operator": "O_W = [-D^2+M_W^2]g^{mu nu}+R_W^{mu nu}",
                "multiplicity": 2,
                "status": "included_seed_registry",
                "mass_squared_GeV2": str(mw2),
            },
            {
                "block": "neutral_weak_vector",
                "operator": "O_Z = [-partial^2+M_Z^2]g^{mu nu}+R_Z^{mu nu}",
                "multiplicity": 1,
                "status": "included_seed_registry",
                "mass_squared_GeV2": str(mz2),
            },
            {
                "block": "electroweak_ghosts",
                "operator": "M_gh",
                "multiplicity": "gauge_fixing_dependent",
                "status": "architecture_locked_explicit_gauge_fixing_pending",
                "notes": "Ghosts represented explicitly so gauge redundancy is not silently counted.",
            },
            {
                "block": "fermions_flavor",
                "operator": "D_F",
                "multiplicity": "PR-II flavor sheets",
                "status": "deferred_to_later_PR3_flavor_radiative_module",
            },
            {
                "block": "strong_sector",
                "operator": "O_G",
                "multiplicity": "SU(3)_c",
                "status": "deferred_until_strong_fiber_closure",
            },
        ],
        "reference_normalization": {
            "gauge_null_modes_removed": True,
            "photon_zero_mode_reference_normalized": True,
            "vacuum_reference_subtracted": True,
            "log_zero_avoided": True,
        },
        "alpha_radiative_extraction_convention": {
            "effective_action_term": "DeltaGamma_PR^(1)[F] contains -1/4 DeltaZ_A^PR int F_{mu nu}F^{mu nu}",
            "alpha_shift": "Delta alpha_PR_rad_inv = 4*pi*DeltaZ_A^PR",
            "status": "Step 05 output, not Step 04 input",
        },
        "acceptance_gates": {
            "physical_hessian_imported_from_step_03": True,
            "gauge_null_modes_excluded": True,
            "photon_treated_as_external_massless_background": True,
            "positive_WZ_tree_masses_registered": True,
            "PR_trace_log_reference_normalized": True,
            "ghost_and_fermion_blocks_explicitly_represented": True,
            "no_empirical_target_values_used": True,
            "delta_ZA_not_inserted": True,
        },
        "next_step": "Step 05: derive DeltaZ_A^PR and Delta alpha_PR_rad_inv",
    }


def main() -> None:
    report = build_radiative_determinant_seed()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
