#!/usr/bin/env python3
"""
PR-III v05c: Electroweak Running Candidate C1

Step 06C computes the minimal compact-boundary transport candidate for carrying
alpha_PR(0) to the PR electroweak matching scale. It uses only frozen PR values.
External weak-sector references are reserved for later diagnostics.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 90

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_06B_PATH = REPO_ROOT / "data" / "electroweak_running_inventory_kernel_seed.json"
STEP_06A_PATH = REPO_ROOT / "data" / "electroweak_scale_transport_protocol_seed.json"
KERNEL_SEED_PATH = REPO_ROOT / "data" / "pr_spectral_kernel_seed.json"
LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"

PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944")


class EWRunningCandidateError(RuntimeError):
    """Raised when Step 06C candidate generation fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise EWRunningCandidateError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise EWRunningCandidateError(f"Missing ledger symbol: {symbol}")


def build_candidate() -> dict[str, Any]:
    step06b = load_json(STEP_06B_PATH)
    step06a = load_json(STEP_06A_PATH)
    kernel = load_json(KERNEL_SEED_PATH)
    ledger = load_json(LEDGER_PATH)

    if step06b.get("status") != "STEP_06B_EW_RUNNING_KERNEL_LOCKED":
        raise EWRunningCandidateError("Step 06B running kernel must be locked before Step 06C.")
    if step06a.get("status") != "STEP_06A_EW_TRANSPORT_PROTOCOL_LOCKED":
        raise EWRunningCandidateError("Step 06A transport protocol must be locked before Step 06C.")

    gates = step06b.get("acceptance_gates", {})
    required = [
        "step_06A_transport_equation_imported",
        "step_05B_charge_inventory_preserved",
        "neutral_modes_excluded_by_Q2",
        "PR_running_kernel_class_defined_without_arbitrary_cutoff",
        "threshold_sources_restricted_to_PR_or_symbolic",
        "external_weak_targets_not_used",
        "running_correction_not_computed_prematurely",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise EWRunningCandidateError(f"Step 06B gate(s) failed or missing: {failed}")

    alpha0_inv = dec(step06a["low_energy_input"]["alpha_PR_0_inv"])
    qbc = dec(kernel["boundary_anchors"]["q_bc_HR"])
    cbc = dec(kernel["boundary_anchors"]["c_bc"])
    sin2 = dec(ledger_object(ledger, "sin2thetaW_tree")["value"])
    v = dec(ledger_object(ledger, "v_EW_PR")["value"])
    lam = dec(ledger_object(ledger, "Lambda_EW_PR")["value"])

    delta_run = qbc * cbc
    alpha_mu_inv = alpha0_inv - delta_run
    if alpha_mu_inv <= 0:
        raise EWRunningCandidateError("Transported inverse alpha must remain positive.")
    if alpha_mu_inv >= alpha0_inv:
        raise EWRunningCandidateError("C1 transport should lower inverse alpha.")

    alpha_mu = Decimal(1) / alpha_mu_inv
    e = (Decimal(4) * PI * alpha_mu).sqrt()
    cos2 = Decimal(1) - sin2
    sin = sin2.sqrt()
    cos = cos2.sqrt()
    g = e / sin
    gp = e / cos
    mw2 = g * g * v * v / Decimal(4)
    mz2 = (g * g + gp * gp) * v * v / Decimal(4)
    mw = mw2.sqrt()
    mz = mz2.sqrt()
    gf = Decimal(1) / (Decimal(2).sqrt() * v * v)
    rho = mw2 / (mz2 * cos2)

    if abs(rho - Decimal(1)) > Decimal("1e-45"):
        raise EWRunningCandidateError(f"rho audit failed: {rho}")

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v05c_ew_running_candidate",
        "status": "STEP_06C_EW_RUNNING_CANDIDATE_GENERATED",
        "candidate_name": "minimal_compact_boundary_transport_C1",
        "formula": {
            "Delta_run_C1_PR": "q_bc_HR*c_bc",
            "alpha_PR_C1_inv_muEW": "alpha_PR_0_inv-Delta_run_C1_PR",
            "e_PR_C1": "sqrt(4*pi/alpha_PR_C1_inv_muEW)",
            "g_PR_C1": "e_PR_C1/sqrt(sin2thetaW_PR)",
            "gprime_PR_C1": "e_PR_C1/sqrt(1-sin2thetaW_PR)",
            "MW_PR_C1": "sqrt((1/4)*g_PR_C1^2*v_EW_PR^2)",
            "MZ_PR_C1": "sqrt((1/4)*(g_PR_C1^2+gprime_PR_C1^2)*v_EW_PR^2)",
            "GF_PR": "1/(sqrt(2)*v_EW_PR^2)",
            "rho_EW_C1": "MW2/(MZ2*cos2thetaW_PR)",
        },
        "frozen_inputs": {
            "alpha_PR_0_inv": str(alpha0_inv),
            "q_bc_HR": str(qbc),
            "c_bc": str(cbc),
            "sin2thetaW_PR": str(sin2),
            "v_EW_PR_GeV": str(v),
            "Lambda_EW_PR_GeV": str(lam),
        },
        "derived_transport": {
            "Delta_run_C1_PR": str(delta_run),
            "alpha_PR_C1_inv_muEW": str(alpha_mu_inv),
            "alpha_PR_C1_muEW": str(alpha_mu),
            "e_PR_C1_muEW": str(e),
            "g_PR_C1_muEW": str(g),
            "gprime_PR_C1_muEW": str(gp),
        },
        "weak_mass_ledger_C1": {
            "MW_squared_GeV2": str(mw2),
            "MW_GeV": str(mw),
            "MZ_squared_GeV2": str(mz2),
            "MZ_GeV": str(mz),
            "GF_GeV_minus2": str(gf),
            "rho_EW_C1": str(rho),
        },
        "acceptance_gates": {
            "candidate_uses_only_frozen_PR_quantities": True,
            "transport_action_not_selected_from_external_reference": True,
            "alpha_inverse_lowered_by_running": True,
            "couplings_reconstructed_from_PR_values_only": True,
            "weak_mass_ledger_generated_without_external_weak_inputs": True,
            "rho_EW_preserved": True,
            "diagnostic_comparison_deferred": True,
            "minimal_C1_not_final_theorem": True,
        },
        "next_step": "Step 06D: weak mass ledger audit and refinement decision",
    }


def main() -> None:
    print(json.dumps(build_candidate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
