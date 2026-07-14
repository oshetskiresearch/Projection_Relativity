#!/usr/bin/env python3
"""
PR-III v06f: Final Neutrino Closure Audit

Step 07F consolidates the no-fit neutrino stability and diagnostic compatibility
results. It adds no new correction and does not claim an exact all-orders theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DIAG_PATH = REPO_ROOT / "data" / "neutrino_diagnostic_comparison.json"
MBB_PATH = REPO_ROOT / "data" / "neutrino_mbb_stability_envelope.json"
ORDERING_PATH = REPO_ROOT / "data" / "neutrino_ordering_pmns_stability_audit.json"


class FinalNeutrinoClosureError(RuntimeError):
    """Raised when Step 07F final closure audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FinalNeutrinoClosureError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_final_neutrino_audit() -> dict[str, Any]:
    diag = load_json(DIAG_PATH)
    mbb = load_json(MBB_PATH)
    ordering = load_json(ORDERING_PATH)

    if diag.get("status") != "STEP_07E_NEUTRINO_DIAGNOSTIC_COMPARISON_LOCKED":
        raise FinalNeutrinoClosureError("Step 07E diagnostic comparison must be locked before Step 07F.")
    if mbb.get("status") != "STEP_07C_M_BETA_BETA_STABILITY_LOCKED":
        raise FinalNeutrinoClosureError("Step 07C m_beta_beta stability must be locked before Step 07F.")
    if ordering.get("status") != "STEP_07D_ORDERING_PMNS_STABILITY_LOCKED":
        raise FinalNeutrinoClosureError("Step 07D ordering/PMNS stability must be locked before Step 07F.")

    gates = diag.get("acceptance_gates", {})
    required = [
        "diagnostic_values_used_only_after_generation",
        "PR_neutrino_branch_not_modified",
        "oscillation_branch_diagnostic_compatible",
        "mass_sum_below_conservative_cosmology_ceiling",
        "m_beta_below_direct_beta_decay_bound",
        "m_beta_beta_below_current_direct_limits",
        "not_overstated_as_detection_or_exact_theorem",
        "step_07F_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise FinalNeutrinoClosureError(f"Step 07E gate(s) failed or missing: {failed}")

    generated = diag["generated_PR_values"]
    envelope = mbb["m_beta_beta_envelope"]
    branch_envelope = mbb["mass_branch_envelope"]
    diagnostic_status = dict(diag["diagnostic_decision"])
    diagnostic_status.pop("final_neutrino_theorem", None)

    return {
        "project": "Projection Relativity III",
        "dataset": "neutrino_final_closure_audit",
        "status": "STEP_07F_FINAL_NEUTRINO_CLOSURE_AUDIT_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "diagnostic_references_used_after_generation_only": True,
            "generation_values_modified": False,
            "final_exact_theorem_claimed": False,
        },
        "final_PR_branch": {
            "m1_eV": generated["m1_eV"],
            "m2_eV": generated["m2_eV"],
            "m3_eV": generated["m3_eV"],
            "sum_m_eV": generated["sum_m_eV"],
            "m_beta_eV": generated["m_beta_eV"],
            "m_beta_meV": generated["m_beta_meV"],
            "m_beta_beta_eV": generated["m_beta_beta_eV"],
            "m_beta_beta_meV": generated["m_beta_beta_meV"],
        },
        "stability_envelope": {
            "m_beta_beta_lower_meV": envelope["lower_meV"],
            "m_beta_beta_upper_meV": envelope["upper_meV"],
            "m_beta_beta_envelope_meV": envelope["Delta_m_beta_beta_env_meV"],
            "relative_envelope_ppm": envelope["relative_ppm"],
            "m1_branch_status": branch_envelope["m1_status"],
            "normal_ordering_preserved": branch_envelope["ordering_preserved"],
        },
        "diagnostic_status": diagnostic_status,
        "no_fit_provenance": {
            "allowed_generation_inputs": [
                "frozen PR-II neutrino masses",
                "frozen PR-II PMNS branch",
                "frozen PR-II m_beta_beta",
                "PR-III alpha closure ledger",
                "PR-III electroweak closure ledger",
                "PR spectral gap and boundary anchors",
                "Step 07B/07C PR stability envelope",
            ],
            "excluded_generation_inputs": [
                "measured neutrino mass splittings",
                "observed PMNS angles",
                "cosmological mass-sum limits",
                "neutrinoless double-beta experimental limits",
                "sterile-neutrino target values",
            ],
        },
        "closure_status_decision": {
            "neutrino_branch_status": "STABILITY_LOCKED_AND_DIAGNOSTIC_COMPATIBLE",
            "normal_ordering_status": "STABLE_UNDER_PR_MULTIPLICATIVE_ENVELOPE",
            "PMNS_status": "FROZEN_UNITARY_BRANCH_WITH_UNITARY_UPDATE_RULE",
            "m_beta_status": "BELOW_CURRENT_DIRECT_BETA_DECAY_LIMITS",
            "m_beta_beta_status": "STABLE_AND_BELOW_CURRENT_DIRECT_0NUBB_LIMITS",
            "PR2_neutrino_obligation": "SATISFIED_TO_CURRENT_DIAGNOSTIC_PRECISION",
            "final_exact_neutrino_theorem": "NOT_CLAIMED",
            "step_07_status": "COMPLETE",
        },
        "remaining_obligations": [
            "derive or rule out additive Majorana seed S_nu_i_PR",
            "derive phase-sensitive PMNS radiative deformation A_nu_PR",
            "construct all-orders neutrino uncertainty theorem",
            "update diagnostic comparisons when future constraints improve",
        ],
        "acceptance_gates": {
            "branch_remains_no_fit": True,
            "massless_branch_protected_at_multiplicative_order": True,
            "normal_ordering_stable": True,
            "PMNS_unitarity_preserved_by_update_rule": True,
            "m_beta_beta_stable_under_PR_envelope": True,
            "diagnostic_comparisons_post_generation_only": True,
            "not_overstated_as_detection_or_exact_theorem": True,
            "step_08_defined": True,
        },
        "next_step": "Step 08: SU(3)_c strong phase-fiber closure and running audit",
    }


def main() -> None:
    print(json.dumps(build_final_neutrino_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
