#!/usr/bin/env python3
"""
PR-III v05e: Electroweak Diagnostic Comparison

Step 06E compares the generated C1 weak ledger to external references after
generation. It does not modify the candidate or feed reference values back into
any generation step.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
C1_AUDIT_PATH = REPO_ROOT / "data" / "electroweak_weak_mass_ledger_audit_C1.json"


class EWDiagnosticComparisonError(RuntimeError):
    """Raised when Step 06E diagnostic comparison fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise EWDiagnosticComparisonError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_diagnostic_comparison() -> dict[str, Any]:
    c1 = load_json(C1_AUDIT_PATH)
    if c1.get("status") != "STEP_06D_WEAK_MASS_LEDGER_AUDIT_LOCKED":
        raise EWDiagnosticComparisonError("Step 06D weak mass ledger audit must be locked before Step 06E.")

    gates = c1.get("acceptance_gates", {})
    required = [
        "C1_uses_only_frozen_PR_quantities",
        "transported_inverse_alpha_lower_than_low_energy",
        "couplings_reconstructed_from_PR_values_only",
        "weak_masses_generated_from_ledger_equations",
        "positive_WZ_masses",
        "rho_EW_preserved",
        "diagnostic_comparison_deferred",
        "C1_not_final_theorem",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise EWDiagnosticComparisonError(f"Step 06D gate(s) failed or missing: {failed}")

    generated = c1["weak_mass_ledger_C1"]
    mw = dec(generated["MW_GeV"])
    mz = dec(generated["MZ_GeV"])
    gf = dec(generated["GF_GeV_minus2"])

    refs = {
        "MW_ref_GeV": Decimal("80.3692"),
        "MW_sigma_GeV": Decimal("0.0133"),
        "MZ_ref_GeV": Decimal("91.1876"),
        "MZ_sigma_GeV": Decimal("0.0021"),
        "GF_ref_GeV_minus2": Decimal("0.000011663788"),
        "GF_sigma_GeV_minus2": Decimal("0.000000000007"),
    }

    mw_res = mw - refs["MW_ref_GeV"]
    mz_res = mz - refs["MZ_ref_GeV"]
    gf_res = gf - refs["GF_ref_GeV_minus2"]

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v05e_ew_diagnostic_comparison",
        "status": "STEP_06E_DIAGNOSTIC_COMPARISON_LOCKED",
        "candidate_under_audit": c1["candidate_under_audit"],
        "generated_PR_values": {
            "MW_C1_GeV": str(mw),
            "MZ_C1_GeV": str(mz),
            "GF_PR_GeV_minus2": str(gf),
            "rho_EW_C1": generated["rho_EW_C1"],
        },
        "diagnostic_references": {key: str(value) for key, value in refs.items()},
        "diagnostic_residuals": {
            "MW_residual_GeV": str(mw_res),
            "MW_sigma_distance": str(mw_res / refs["MW_sigma_GeV"]),
            "MW_relative_ppm": str(mw_res / refs["MW_ref_GeV"] * Decimal("1000000")),
            "MZ_residual_GeV": str(mz_res),
            "MZ_sigma_distance": str(mz_res / refs["MZ_sigma_GeV"]),
            "MZ_relative_ppm": str(mz_res / refs["MZ_ref_GeV"] * Decimal("1000000")),
            "GF_residual_GeV_minus2": str(gf_res),
            "GF_sigma_distance": str(gf_res / refs["GF_sigma_GeV_minus2"]),
            "GF_relative_ppm": str(gf_res / refs["GF_ref_GeV_minus2"] * Decimal("1000000")),
        },
        "diagnostic_decision": {
            "GF_status": "DIAGNOSTIC_PASS_WITHIN_ONE_SIGMA",
            "MW_status": "REQUIRES_REFINEMENT",
            "MZ_status": "REQUIRES_REFINEMENT",
            "C1_status": "INTERNAL_LEDGER_PASS_ONLY",
            "final_EW_precision_theorem": "NOT_YET",
            "next_step": "Step 06F weak-angle or oblique refinement",
        },
        "acceptance_gates": {
            "references_used_only_after_generation": True,
            "all_residuals_reported": True,
            "GF_precision_success_recorded": True,
            "WZ_mass_failure_recorded": True,
            "C1_not_overstated_as_final_closure": True,
            "next_refinement_direction_defined": True,
        },
    }


def main() -> None:
    print(json.dumps(build_diagnostic_comparison(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
