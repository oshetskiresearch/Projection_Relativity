#!/usr/bin/env python3
"""
PR-III v05a: Electroweak Scale-Transport Protocol Audit

Step 06A locks the protocol for carrying the Step 05H low-energy alpha closure
into the PR electroweak boundary scale. It does not compute running.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_05H_PATH = REPO_ROOT / "data" / "alpha_residual_closure_current_precision.json"
LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"


class EWTransportProtocolError(RuntimeError):
    """Raised when Step 06A protocol validation fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise EWTransportProtocolError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise EWTransportProtocolError(f"Missing ledger symbol: {symbol}")


def build_protocol() -> dict[str, Any]:
    alpha = load_json(STEP_05H_PATH)
    ledger = load_json(LEDGER_PATH)

    if alpha.get("status") != "STEP_05H_RESIDUAL_BOUNDING_LOCKED":
        raise EWTransportProtocolError("Step 05H alpha closure must be locked before Step 06A.")
    if ledger.get("status") != "FROZEN":
        raise EWTransportProtocolError("Inheritance ledger must be frozen before Step 06A.")

    gates = alpha.get("acceptance_gates", {})
    required = [
        "D1D2_candidate_remains_no_fit",
        "references_used_only_after_generation",
        "inside_Rb_one_sigma",
        "current_precision_closure_not_exact_theorem",
        "remaining_residual_reported",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise EWTransportProtocolError(f"Step 05H gate(s) failed or missing: {failed}")

    return {
        "project": "Projection Relativity III",
        "dataset": "electroweak_scale_transport_protocol_seed",
        "status": "STEP_06A_EW_TRANSPORT_PROTOCOL_LOCKED",
        "low_energy_input": {
            "alpha_PR_0_inv": alpha["candidate"]["alpha_PR_phys_D1D2_inv"],
            "source": "Step 05H D1+D2 alpha closure",
        },
        "electroweak_scale": {
            "mu_EW_PR_GeV": ledger_object(ledger, "Lambda_EW_PR")["value"],
            "scale_symbol": "Lambda_EW_PR",
            "source": "frozen PR-II weak displacement anchor",
        },
        "order_scale": {
            "v_EW_PR_GeV": ledger_object(ledger, "v_EW_PR")["value"],
        },
        "weak_angle_boundary": {
            "sin2thetaW_PR_boundary": ledger_object(ledger, "sin2thetaW_tree")["value"],
            "transport_form": "sin2thetaW_PR(mu_EW)=sin2thetaW_PR^(0)+Delta_sin2thetaW_PR_run",
        },
        "transport_equation": {
            "alpha_transport": "alpha_PR_inv(mu_EW)=alpha_PR_inv(0)-Delta_run_PR(0_to_mu_EW)",
            "running_term_status": "not_assigned_in_step_06A",
        },
        "coupling_reconstruction": {
            "e_PR_mu": "sqrt(4*pi*alpha_PR(mu_EW))",
            "g_PR_mu": "e_PR(mu_EW)/sin(thetaW(mu_EW))",
            "gprime_PR_mu": "e_PR(mu_EW)/cos(thetaW(mu_EW))",
        },
        "weak_ledger_equations": {
            "MW2": "one_fourth*g_PR(mu_EW)^2*v_EW_PR^2",
            "MZ2": "one_fourth*(g_PR(mu_EW)^2+gprime_PR(mu_EW)^2)*v_EW_PR^2",
            "GF_PR": "1/(sqrt(2)*v_EW_PR^2)",
            "rho_EW_PR": "MW2/(MZ2*cos(thetaW)^2)",
        },
        "allowed_inputs": [
            "alpha_PR_phys_D1D2_inv",
            "Lambda_EW_PR",
            "v_EW_PR",
            "sin2thetaW_PR",
            "PR charged-mode inventory",
            "PR spectral kernel objects",
        ],
        "excluded_reference_values": [
            "external weak-sector reference values",
            "external coupling references",
            "observed mixing matrices",
        ],
        "acceptance_gates": {
            "low_energy_alpha_imported_from_step_05H": True,
            "EW_matching_scale_PR_derived": True,
            "transport_equation_defined_without_fitted_running": True,
            "coupling_reconstruction_locked": True,
            "weak_ledger_equations_locked": True,
            "diagnostic_comparisons_deferred": True,
        },
        "next_step": "Step 06B: construct electroweak running inventory and kernel",
    }


def main() -> None:
    print(json.dumps(build_protocol(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
