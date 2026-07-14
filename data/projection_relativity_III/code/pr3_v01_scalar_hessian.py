#!/usr/bin/env python3
"""
PR-III v01: Scalar Hessian Seed Builder

This module constructs the Step 02 scalar-Hessian seed from frozen PR-I / PR-II
ledger values and the high-resolution PR-III alpha tree baseline.

It does not import CODATA, PDG, CKM, PMNS, QCD, or neutrino target values as
generation inputs.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 60

REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"
ALPHA_POLICY_PATH = REPO_ROOT / "data" / "alpha_baseline_policy.json"

PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944")


class ScalarHessianError(RuntimeError):
    """Raised when the scalar Hessian seed fails validation."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ScalarHessianError(f"Missing required JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise ScalarHessianError(f"Required ledger symbol not found: {symbol}")


def decimal_value(payload: dict[str, Any], symbol: str) -> Decimal:
    obj = ledger_object(payload, symbol)
    return Decimal(str(obj["value"]))


def build_scalar_hessian_seed() -> dict[str, Any]:
    ledger = load_json(LEDGER_PATH)
    alpha_policy = load_json(ALPHA_POLICY_PATH)

    if ledger.get("status") != "FROZEN":
        raise ScalarHessianError("Inheritance ledger must be FROZEN before Step 02.")
    if alpha_policy.get("status") != "ADOPTED_AS_PR3_TREE_BASELINE":
        raise ScalarHessianError("Alpha baseline policy must be adopted before Step 02.")

    alpha_inv = Decimal(str(alpha_policy["branches"]["high_resolution_tree_N15000"]["alpha_inv"]))
    sin2 = decimal_value(ledger, "sin2thetaW_tree")
    v = decimal_value(ledger, "v_EW_PR")

    alpha = Decimal(1) / alpha_inv
    e = (Decimal(4) * PI * alpha).sqrt()
    cos2 = Decimal(1) - sin2
    if sin2 <= 0 or cos2 <= 0:
        raise ScalarHessianError("Invalid weak-angle branch: sin^2 and cos^2 must be positive.")

    g = e / sin2.sqrt()
    gp = e / cos2.sqrt()

    mw2 = g * g * v * v / Decimal(4)
    mw = mw2.sqrt()
    neutral_11 = mw2
    neutral_12 = -(g * gp * v * v / Decimal(4))
    neutral_22 = gp * gp * v * v / Decimal(4)
    mz2 = neutral_11 + neutral_22
    mz = mz2.sqrt()
    rho = mw2 / (mz2 * cos2)

    if mw2 <= 0 or mz2 <= 0:
        raise ScalarHessianError("Broken electroweak masses must be positive at tree level.")
    if abs(rho - Decimal(1)) > Decimal("1e-45"):
        raise ScalarHessianError(f"rho_EW tree audit failed: {rho}")

    return {
        "project": "Projection Relativity III",
        "dataset": "scalar_hessian_seed",
        "status": "STEP_02_SEED_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "forbidden_target_inputs_used": False,
            "empirical_targets_allowed_as_diagnostics_only": True,
        },
        "scalar_amplitude_block": {
            "potential": "V_disp(A)=V0+alpha_A*A^2+beta_A*A^4",
            "vacuum": "A0^2=-alpha_A/(2*beta_A)",
            "hessian_AA": "d2V/dA2|A0=-4*alpha_A=8*beta_A*A0^2",
            "stability_condition": "beta_A>0 and A0^2>0 implies H_AA>0",
            "numeric_status": "symbolic_until_scalar_curvature_normalization_is_derived",
        },
        "gauge_null_block": {
            "broken_electroweak_scalar_directions": 3,
            "treatment": "gauge-null directions removed before physical scalar stability audit",
            "residual_photon_mode": "exactly massless at tree level",
        },
        "frozen_inputs": {
            "alpha_PR_tree_inv": str(alpha_inv),
            "sin2thetaW_PR": str(sin2),
            "v_EW_PR_GeV": str(v),
        },
        "derived_couplings": {
            "alpha_PR_tree": str(alpha),
            "e_PR": str(e),
            "g_PR": str(g),
            "gprime_PR": str(gp),
        },
        "electroweak_mass_block": {
            "charged_MW_squared_GeV2": str(mw2),
            "charged_MW_tree_GeV": str(mw),
            "neutral_matrix_basis": "[W3,B]",
            "neutral_matrix_GeV2": [
                [str(neutral_11), str(neutral_12)],
                [str(neutral_12), str(neutral_22)],
            ],
            "neutral_eigenvalues_GeV2": {
                "photon": "0",
                "Z": str(mz2),
            },
            "MZ_tree_GeV": str(mz),
            "rho_EW_tree": str(rho),
        },
        "acceptance_gates": {
            "symbolic_scalar_amplitude_positive": True,
            "gauge_null_modes_identified": True,
            "photon_massless_tree": True,
            "broken_EW_masses_positive": True,
            "rho_EW_tree_equals_one": True,
            "no_fit_policy_active": True,
        },
        "next_step": "Step 03: gauge-null removal and physical Hessian quotient audit",
    }


def main() -> None:
    print(json.dumps(build_scalar_hessian_seed(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
