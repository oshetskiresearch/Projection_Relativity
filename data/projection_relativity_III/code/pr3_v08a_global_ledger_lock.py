#!/usr/bin/env python3
"""
PR-III v08a: Global Cross-Sector Ledger Lock

Step 09A consolidates locked outputs from Steps 05-08 into a global ledger
before anomaly and running-continuity audits. It does not compute new sector
corrections.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
ALPHA_PATH = REPO_ROOT / "data" / "alpha_residual_closure_current_precision.json"
EW_PATH = REPO_ROOT / "data" / "electroweak_neutral_D3_candidate_C3.json"
NU_PATH = REPO_ROOT / "data" / "neutrino_final_closure_audit.json"
STRONG_PATH = REPO_ROOT / "data" / "strong_final_closure_audit.json"


class GlobalLedgerLockError(RuntimeError):
    """Raised when Step 09A global ledger lock fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise GlobalLedgerLockError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def compact_decimal(value: Any) -> str:
    return format(Decimal(str(value)).normalize(), "f")


def rounded_decimal(value: Any, places: str) -> str:
    return format(Decimal(str(value)).quantize(Decimal(places)), "f")


def build_global_ledger() -> dict[str, Any]:
    alpha = load_json(ALPHA_PATH)
    ew = load_json(EW_PATH)
    nu = load_json(NU_PATH)
    strong = load_json(STRONG_PATH)

    if alpha.get("status") != "STEP_05H_RESIDUAL_BOUNDING_LOCKED":
        raise GlobalLedgerLockError("Step 05H alpha closure must be locked.")
    if ew.get("status") != "STEP_06J_NEUTRAL_D3_REFINEMENT_GENERATED":
        raise GlobalLedgerLockError("Step 06J electroweak closure must be generated.")
    if nu.get("status") != "STEP_07F_FINAL_NEUTRINO_CLOSURE_AUDIT_LOCKED":
        raise GlobalLedgerLockError("Step 07F neutrino closure must be locked.")
    if strong.get("status") != "STEP_08F_FINAL_STRONG_CLOSURE_AUDIT_LOCKED":
        raise GlobalLedgerLockError("Step 08F strong closure must be locked.")

    nu_branch = nu["final_PR_branch"]
    strong_group = strong["su3_group_ledger"]
    strong_active = strong["active_flavor_status"]

    return {
        "project": "Projection Relativity III",
        "dataset": "global_running_anomaly_ledger_seed",
        "status": "STEP_09A_GLOBAL_LEDGER_LOCKED",
        "input_policy": {
            "uses_only_locked_PR_outputs": True,
            "diagnostic_references_post_generation_only": True,
            "generation_values_modified": False,
            "exact_all_orders_theorems_claimed": False,
        },
        "sector_ledgers": {
            "electromagnetic": {
                "alpha_PR_inv": alpha["candidate"]["alpha_PR_phys_D1D2_inv"],
                "status": alpha["closure_status_decision"]["alpha_candidate_status"],
                "final_exact_theorem": "NOT_CLAIMED",
            },
            "electroweak": {
                "MW_PR_GeV": ew["corrected_weak_ledger_C3"]["MW_C3_PR_GeV"],
                "MZ_PR_GeV": ew["corrected_weak_ledger_C3"]["MZ_C3_PR_GeV"],
                "GF_PR_GeV_minus2": ew["corrected_weak_ledger_C3"]["GF_PR_GeV_minus2"],
                "status": ew["diagnostic_decision"]["EW_candidate_status"],
                "final_exact_theorem": ew["diagnostic_decision"]["final_exact_EW_theorem"],
            },
            "neutrino": {
                "m1_eV": nu_branch["m1_eV"],
                "m2_eV": nu_branch["m2_eV"],
                "m3_eV": nu_branch["m3_eV"],
                "sum_m_eV": nu_branch["sum_m_eV"],
                "m_beta_meV": rounded_decimal(nu_branch["m_beta_meV"], "0.000000000001"),
                "m_beta_beta_meV": compact_decimal(nu_branch["m_beta_beta_meV"]),
                "status": nu["closure_status_decision"]["neutrino_branch_status"],
                "final_exact_theorem": "NOT_CLAIMED",
            },
            "strong": {
                "alpha3_PR": strong["final_strong_anchor"]["alpha3_PR"],
                "group": strong_group["group"],
                "N_c": strong_group["N_c"],
                "adjoint_dimension": strong_group["adjoint_dimension"],
                "C_A": strong_group["C_A"],
                "C_F": strong_group["C_F"],
                "T_F": strong_group["T_F"],
                "n_f_PR_at_Lambda_EW_PR": strong_active["n_f_PR_at_Lambda_EW_PR"],
                "beta0_PR_at_Lambda_EW_PR": strong_active["beta0_PR_at_Lambda_EW_PR"],
                "status": strong["closure_status_decision"]["strong_branch_status"],
                "final_exact_theorem": "NOT_CLAIMED",
            },
        },
        "global_audit_queue": {
            "anomaly_registry": [
                "SU(3)c color representation consistency",
                "SU(2)L global/Witten anomaly check",
                "SU(2)^2 U(1) anomaly check",
                "U(1)^3 anomaly check",
                "gravity^2 U(1) anomaly check",
                "residual U(1)em vectorlike consistency",
            ],
            "running_continuity": [
                "alpha_PR low-energy closure to EW transport",
                "EW coupling/mass ledger consistency",
                "strong alpha3 anchor with PR threshold ledger",
                "neutrino radiative stability under EW closure",
            ],
            "provenance_manifest": [
                "forbidden target inputs excluded by sector",
                "diagnostic references post-generation only",
                "exact theorem claims separated from current diagnostic precision closure",
            ],
        },
        "forbidden_global_generation_inputs": [
            "CODATA/PDG targets as generation inputs",
            "external weak masses",
            "external quark masses",
            "external QCD Lambda_MSbar",
            "observed CKM entries",
            "observed PMNS entries",
            "cosmological neutrino limits",
            "0nu beta beta limits",
            "hadron masses as tuning targets",
        ],
        "acceptance_gates": {
            "step_05_alpha_closure_imported": True,
            "step_06_electroweak_closure_imported": True,
            "step_07_neutrino_closure_imported": True,
            "step_08_strong_closure_imported": True,
            "exact_all_orders_theorem_claims_excluded": True,
            "anomaly_and_consistency_audit_queue_defined": True,
            "step_09B_defined": True,
        },
        "next_step": "Step 09B: anomaly registry audit",
    }


def main() -> None:
    print(json.dumps(build_global_ledger(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
