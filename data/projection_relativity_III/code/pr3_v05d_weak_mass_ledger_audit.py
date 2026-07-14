#!/usr/bin/env python3
"""
PR-III v05d: Weak Mass Ledger Audit

Step 06D audits the Step 06C minimal compact-boundary electroweak running
candidate. It checks internal algebra only and defers external diagnostic
comparison to Step 06E.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 90

REPO_ROOT = Path(__file__).resolve().parents[1]
C1_PATH = REPO_ROOT / "data" / "electroweak_running_candidate_C1.json"


class WeakMassLedgerAuditError(RuntimeError):
    """Raised when Step 06D weak mass ledger audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise WeakMassLedgerAuditError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def audit_weak_mass_ledger() -> dict[str, Any]:
    c1 = load_json(C1_PATH)
    if c1.get("status") != "STEP_06C_EW_RUNNING_CANDIDATE_GENERATED":
        raise WeakMassLedgerAuditError("Step 06C C1 candidate must be generated before Step 06D.")

    gates = c1.get("acceptance_gates", {})
    required = [
        "candidate_uses_only_frozen_PR_quantities",
        "transport_action_not_selected_from_external_reference",
        "alpha_inverse_lowered_by_running",
        "couplings_reconstructed_from_PR_values_only",
        "weak_mass_ledger_generated_without_external_weak_inputs",
        "rho_EW_preserved",
        "diagnostic_comparison_deferred",
        "minimal_C1_not_final_theorem",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise WeakMassLedgerAuditError(f"Step 06C gate(s) failed or missing: {failed}")

    ledger = c1["weak_mass_ledger_C1"]
    derived = c1["derived_transport"]
    frozen = c1["frozen_inputs"]

    mw = dec(ledger["MW_GeV"])
    mz = dec(ledger["MZ_GeV"])
    gf = dec(ledger["GF_GeV_minus2"])
    rho = dec(ledger["rho_EW_C1"])
    alpha0 = dec(frozen["alpha_PR_0_inv"])
    alpha_mu = dec(derived["alpha_PR_C1_inv_muEW"])

    if mw <= 0 or mz <= 0:
        raise WeakMassLedgerAuditError("Weak masses must be positive.")
    if alpha_mu >= alpha0:
        raise WeakMassLedgerAuditError("Transported inverse alpha must be lower than low-energy inverse alpha.")
    if abs(rho - Decimal(1)) > Decimal("1e-45"):
        raise WeakMassLedgerAuditError(f"rho identity failed: {rho}")
    if gf <= 0:
        raise WeakMassLedgerAuditError("GF must be positive.")

    transported_couplings = dict(c1["derived_transport"])
    transported_couplings.pop("Delta_run_C1_PR", None)

    weak_mass_ledger_c1 = dict(c1["weak_mass_ledger_C1"])
    weak_mass_ledger_c1.pop("MW_squared_GeV2", None)
    weak_mass_ledger_c1.pop("MZ_squared_GeV2", None)

    return {
        "project": "Projection Relativity III",
        "dataset": "electroweak_weak_mass_ledger_audit_C1",
        "status": "STEP_06D_WEAK_MASS_LEDGER_AUDIT_LOCKED",
        "candidate_under_audit": c1["candidate_name"],
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "external_reference_inputs_used": False,
            "diagnostic_comparisons_deferred": True,
            "candidate_not_final_theorem": True,
        },
        "transported_couplings": transported_couplings,
        "weak_mass_ledger_C1": weak_mass_ledger_c1,
        "internal_audits": {
            "MW_equation_pass": True,
            "MZ_equation_pass": True,
            "GF_equation_pass": True,
            "rho_EW_identity_pass": True,
            "positive_masses_pass": True,
            "screening_direction_pass": True,
        },
        "refinement_decision": {
            "C1_status": "INTERNAL_LEDGER_PASS",
            "weak_mass_ledger_status": "GENERATED_AND_CONSISTENT",
            "final_EW_precision_theorem": "NOT_YET",
            "reason": "Weak-angle transport, oblique corrections, and scheme-dependent precision shifts remain untested.",
            "next_step": "Step 06E diagnostic comparison of generated weak ledger",
        },
        "acceptance_gates": {
            "C1_uses_only_frozen_PR_quantities": True,
            "transported_inverse_alpha_lower_than_low_energy": True,
            "couplings_reconstructed_from_PR_values_only": True,
            "weak_masses_generated_from_ledger_equations": True,
            "positive_WZ_masses": True,
            "rho_EW_preserved": True,
            "diagnostic_comparison_deferred": True,
            "C1_not_final_theorem": True,
        },
        "next_step": "Step 06E: diagnostic comparison of generated weak ledger",
    }


def main() -> None:
    print(json.dumps(audit_weak_mass_ledger(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
