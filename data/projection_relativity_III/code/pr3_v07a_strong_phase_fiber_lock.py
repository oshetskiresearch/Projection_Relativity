#!/usr/bin/env python3
"""
PR-III v07a: Strong Phase-Fiber Branch Lock

Step 08A freezes the SU(3)c group ledger and PR-II alpha3_PR anchor before
constructing the strong running kernel. No external QCD reference is used.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

getcontext().prec = 60

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_07F_PATH = REPO_ROOT / "data" / "neutrino_final_closure_audit.json"
LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"


class StrongPhaseFiberLockError(RuntimeError):
    """Raised when Step 08A branch locking fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise StrongPhaseFiberLockError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise StrongPhaseFiberLockError(f"Missing ledger symbol: {symbol}")


def build_strong_branch_lock() -> dict[str, Any]:
    step07 = load_json(STEP_07F_PATH)
    ledger = load_json(LEDGER_PATH)

    if step07.get("status") != "STEP_07F_FINAL_NEUTRINO_CLOSURE_AUDIT_LOCKED":
        raise StrongPhaseFiberLockError("Step 07F final neutrino audit must be locked before Step 08A.")
    if step07.get("closure_status_decision", {}).get("step_07_status") != "COMPLETE":
        raise StrongPhaseFiberLockError("Step 07 must be complete before Step 08A.")
    if ledger.get("status") != "FROZEN":
        raise StrongPhaseFiberLockError("Inheritance ledger must be frozen before Step 08A.")

    alpha3 = Decimal(str(ledger_object(ledger, "alpha3_PR")["value"]))
    if alpha3 <= 0:
        raise StrongPhaseFiberLockError("alpha3_PR anchor must be positive.")

    nc = 3
    adjoint_dim = nc * nc - 1
    ca = Fraction(nc, 1)
    cf = Fraction(nc * nc - 1, 2 * nc)
    tf = Fraction(1, 2)

    if adjoint_dim != 8 or ca != 3 or cf != Fraction(4, 3) or tf != Fraction(1, 2):
        raise StrongPhaseFiberLockError("SU(3)c group ledger failed.")

    return {
        "project": "Projection Relativity III",
        "dataset": "strong_phase_fiber_closure_seed",
        "status": "STEP_08A_STRONG_BRANCH_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "external_QCD_targets_used": False,
            "diagnostic_comparisons_deferred": True,
            "running_correction_computed": False,
        },
        "prerequisite_status": {
            "step_07_status": "COMPLETE",
            "step_08_ready": True,
        },
        "strong_anchor": {
            "alpha3_PR": str(alpha3),
            "source": "frozen PR-II inheritance ledger",
            "role": "compact-boundary strong-coupling anchor, not external fit",
        },
        "su3_group_ledger": {
            "group": "SU(3)_c",
            "N_c": nc,
            "adjoint_dimension": adjoint_dim,
            "C_A": str(ca),
            "C_F": str(cf),
            "T_F": str(tf),
            "identities_are_fit_parameters": False,
        },
        "running_object": {
            "equation": "mu*d(alpha3_PR)/dmu = beta3_PR(alpha3, P_color, K_PR)",
            "one_loop_color_audit_form": "beta0_PR=(11/3)*C_A-(4/3)*T_F*n_f_PR",
            "n_f_PR_status": "deferred_to_PR_derived_threshold_audit",
            "running_computed_in_step_08A": False,
        },
        "allowed_generation_inputs": [
            "frozen PR-II alpha3_PR",
            "SU(3)c group identities",
            "PR-II quark mass sheets once imported from frozen source",
            "PR spectral gap and boundary anchors",
            "PR-III electroweak closure ledger",
            "symbolic thresholds pending PR derivation",
        ],
        "forbidden_generation_inputs": [
            "PDG alpha_s(M_Z)",
            "external quark masses",
            "external QCD Lambda_MSbar",
            "hadron masses as tuning targets",
            "lattice QCD target values",
            "observed CKM entries",
        ],
        "acceptance_gates": {
            "step_07_completion_verified": True,
            "alpha3_PR_imported_from_frozen_ledger": True,
            "SU3_group_ledger_locked": True,
            "strong_beta_running_object_defined_symbolically": True,
            "active_flavor_thresholds_deferred_to_PR_inputs": True,
            "external_QCD_targets_excluded": True,
            "step_08B_defined": True,
        },
        "next_step": "Step 08B: construct PR strong spectral/running kernel",
    }


def main() -> None:
    print(json.dumps(build_strong_branch_lock(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
