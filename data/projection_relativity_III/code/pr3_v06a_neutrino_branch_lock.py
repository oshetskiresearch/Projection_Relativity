#!/usr/bin/env python3
"""
PR-III v06a: Neutrino Branch Lock

Step 07A freezes the PR-II neutrino branch and defines the no-fit protocol for
radiative stability testing.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 60

REPO_ROOT = Path(__file__).resolve().parents[1]
EW_CLOSURE_PATH = REPO_ROOT / "data" / "electroweak_neutral_D3_candidate_C3.json"
LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"


class NeutrinoBranchLockError(RuntimeError):
    """Raised when Step 07A branch locking fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise NeutrinoBranchLockError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_neutrino_branch_lock() -> dict[str, Any]:
    ew = load_json(EW_CLOSURE_PATH)
    ledger = load_json(LEDGER_PATH)

    if ew.get("status") != "STEP_06J_NEUTRAL_D3_REFINEMENT_GENERATED":
        raise NeutrinoBranchLockError("Step 06J electroweak closure must be generated before Step 07A.")
    if ew.get("acceptance_gates", {}).get("step_07_ready") is not True:
        raise NeutrinoBranchLockError("Step 06J must mark Step 07 ready.")
    if ledger.get("status") != "FROZEN":
        raise NeutrinoBranchLockError("Inheritance ledger must be frozen before Step 07A.")

    m1 = Decimal("0")
    m2 = Decimal("0.008627283010")
    m3 = Decimal("0.05010655367")
    mass_sum = m1 + m2 + m3
    m_bb = Decimal("0.001507694477")

    if not (m1 <= m2 < m3):
        raise NeutrinoBranchLockError("Normal ordering check failed.")
    if mass_sum != Decimal("0.058733836680"):
        raise NeutrinoBranchLockError(f"Unexpected mass sum: {mass_sum}")
    if m_bb <= 0:
        raise NeutrinoBranchLockError("m_beta_beta must be positive.")

    return {
        "project": "Projection Relativity III",
        "dataset": "neutrino_branch_radiative_stability_seed",
        "status": "STEP_07A_NEUTRINO_BRANCH_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "external_neutrino_targets_used": False,
            "diagnostic_comparisons_deferred": True,
            "radiative_correction_computed": False,
        },
        "pr2_tree_branch": {
            "ordering": "normal",
            "masses_eV": {
                "m1": str(m1),
                "m2": str(m2),
                "m3": str(m3),
                "sum": str(mass_sum),
            },
            "pmns_angles": {
                "sin2theta12": "0.299447410807983",
                "sin2theta23": "0.565008899090616",
                "sin2theta13": "0.022270270124743",
                "delta_CP_deg": "195.646778408",
            },
            "m_beta_beta_eV": str(m_bb),
            "m_beta_beta_meV": str(m_bb * Decimal("1000")),
        },
        "radiative_stability_form": {
            "m_i_phys": "m_i^(0)+Delta_m_i_PR_rad",
            "U_PMNS_phys": "U_PMNS^(0)+Delta_U_PMNS_PR_rad",
            "m_beta_beta_phys": "m_beta_beta^(0)+Delta_m_beta_beta_PR_rad",
            "m1_branch_policy": "massless boundary branch protected unless PR-III derives a nonzero radiative seed",
        },
        "allowed_generation_inputs": [
            "frozen PR-II neutrino branch",
            "frozen PR-II PMNS branch",
            "PR-III alpha closure ledger",
            "PR-III electroweak closure ledger",
            "PR spectral gap and boundary anchors",
            "symbolic radiative kernel pending derivation",
        ],
        "forbidden_generation_inputs": [
            "measured neutrino mass splittings",
            "observed PMNS angles",
            "cosmological neutrino mass-sum limits",
            "neutrinoless double-beta experimental limits",
            "sterile-neutrino target values",
        ],
        "acceptance_gates": {
            "normal_ordering_branch_frozen": True,
            "PMNS_branch_frozen": True,
            "m_beta_beta_frozen": True,
            "radiative_correction_structure_defined": True,
            "m1_branch_not_manually_lifted": True,
            "external_neutrino_targets_excluded": True,
            "step_07B_defined": True,
        },
        "next_step": "Step 07B: construct neutrino radiative stability kernel",
    }


def main() -> None:
    print(json.dumps(build_neutrino_branch_lock(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
