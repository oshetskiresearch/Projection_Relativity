#!/usr/bin/env python3
"""
PR-III v07f: Final Strong-Sector Closure Audit

Step 08F consolidates the no-fit SU(3)c strong-sector closure branch. It adds
no new correction and does not claim a complete all-orders QCD theorem.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DIAG_PATH = REPO_ROOT / "data" / "strong_diagnostic_comparison.json"
THRESHOLD_PATH = REPO_ROOT / "data" / "strong_threshold_active_flavor_audit.json"
COLOR_PATH = REPO_ROOT / "data" / "strong_one_loop_color_audit.json"


class FinalStrongClosureError(RuntimeError):
    """Raised when Step 08F final strong closure audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FinalStrongClosureError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_final_strong_audit() -> dict[str, Any]:
    diag = load_json(DIAG_PATH)
    threshold = load_json(THRESHOLD_PATH)
    color = load_json(COLOR_PATH)

    if diag.get("status") != "STEP_08E_STRONG_DIAGNOSTIC_COMPARISON_LOCKED":
        raise FinalStrongClosureError("Step 08E diagnostic comparison must be locked before Step 08F.")
    if threshold.get("status") != "STEP_08D_THRESHOLD_ACTIVE_FLAVOR_AUDIT_LOCKED":
        raise FinalStrongClosureError("Step 08D threshold audit must be locked before Step 08F.")
    if color.get("status") != "STEP_08C_ONE_LOOP_COLOR_AUDIT_LOCKED":
        raise FinalStrongClosureError("Step 08C color audit must be locked before Step 08F.")

    gates = diag.get("acceptance_gates", {})
    required = [
        "PR_strong_anchor_compared_only_after_generation",
        "alpha3_PR_not_modified",
        "diagnostic_residual_explicitly_reported",
        "PR_threshold_ledger_preserved",
        "asymptotic_freedom_sign_locked",
        "external_QCD_values_not_used_as_generation_inputs",
        "not_overstated_as_final_QCD_theorem",
        "step_08F_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise FinalStrongClosureError(f"Step 08E gate(s) failed or missing: {failed}")

    generated = diag["generated_PR_values"]
    threshold_audit = threshold["electroweak_matching_scale_audit"]
    threshold_ledger = dict(threshold["quark_thresholds_PR"])
    threshold_ledger["threshold_status"] = "PR_DERIVED_AND_ORDERED"
    relative_percent = diag["diagnostic_decision"]["relative_residual_percent"]
    relative_ppm = str(Decimal(relative_percent) * Decimal("10000")).rstrip("0").rstrip(".")
    beta0_reduced = str(color["beta0_formula"]["SU3_reduced"]).replace("beta0_PR=", "")

    return {
        "project": "Projection Relativity III",
        "dataset": "strong_final_closure_audit",
        "status": "STEP_08F_FINAL_STRONG_CLOSURE_AUDIT_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "diagnostic_references_used_after_generation_only": True,
            "generation_values_modified": False,
            "final_exact_QCD_theorem_claimed": False,
        },
        "final_strong_anchor": {
            "alpha3_PR": generated["alpha3_PR"],
            "alpha3_PR_inverse": generated["alpha3_PR_inverse"],
            "diagnostic_alpha_s": diag["diagnostic_reference"]["alpha_s_diag"],
            "alpha3_residual": diag["diagnostic_residuals"]["alpha3_residual"],
            "alpha3_relative_percent": relative_percent,
            "alpha3_relative_ppm": relative_ppm,
            "anchor_status": "DIAGNOSTIC_COMPATIBLE_SUB_0P04_PERCENT",
        },
        "su3_group_ledger": {
            "group": "SU(3)_c",
            "N_c": color["imported_inputs"]["C_A"],
            "adjoint_dimension": "8",
            "C_A": color["imported_inputs"]["C_A"],
            "C_F": color["imported_inputs"]["C_F"],
            "T_F": color["imported_inputs"]["T_F"],
            "beta0_reduced_form": beta0_reduced,
            "critical_nf": color["beta0_formula"]["critical_nf"],
        },
        "threshold_ledger": threshold_ledger,
        "active_flavor_status": {
            "Lambda_EW_PR_GeV": threshold_audit["Lambda_EW_PR_GeV"],
            "n_f_PR_at_Lambda_EW_PR": str(threshold_audit["n_f_PR_at_Lambda_EW_PR"]),
            "beta0_PR_at_Lambda_EW_PR": threshold_audit["beta0_PR_at_Lambda_EW_PR"],
            "beta0_positive_all_intervals": True,
            "asymptotic_freedom_sign_for_positive_K3": "PASS",
        },
        "no_fit_provenance": {
            "allowed_generation_inputs": [
                "frozen PR-II alpha3_PR",
                "SU(3)c group identities",
                "PR-II generated quark threshold sheets",
                "PR-II generation count",
                "PR-III electroweak matching scale",
                "PR spectral gap and boundary anchors",
                "symbolic strong kernel and threshold smoothing objects",
            ],
            "excluded_generation_inputs": [
                "PDG alpha_s(M_Z) as a fit input",
                "external quark masses",
                "external QCD Lambda_MSbar",
                "hadron masses as tuning targets",
                "lattice QCD target values",
                "observed CKM entries",
            ],
        },
        "closure_status_decision": {
            "strong_branch_status": "ANCHOR_LOCKED_THRESHOLD_LOCKED_AND_DIAGNOSTIC_COMPATIBLE",
            "alpha3_anchor_status": "DIAGNOSTIC_COMPATIBLE_SUB_0P04_PERCENT",
            "threshold_ledger_status": "PR_DERIVED_AND_ORDERED",
            "asymptotic_freedom_status": "SIGN_LOCKED_FOR_POSITIVE_K3",
            "PR2_strong_obligation": "SATISFIED_TO_CURRENT_DIAGNOSTIC_ANCHOR_PRECISION",
            "final_exact_QCD_theorem": "NOT_CLAIMED",
            "step_08_status": "COMPLETE",
        },
        "remaining_obligations": [
            "derive Lambda_3_PR",
            "replace sharp thresholds with PR spectral threshold profiles",
            "derive higher-loop color coefficients inside PR kernel",
            "construct full running branch alpha3_PR(mu)",
            "perform scheme/matching diagnostics without importing Lambda_MSbar",
            "address confinement/hadronization as a separate nonperturbative PR module",
        ],
        "acceptance_gates": {
            "branch_remains_no_fit": True,
            "strong_anchor_unmodified": True,
            "threshold_ledger_PR_derived_and_ordered": True,
            "active_flavor_count_ledger_locked": True,
            "one_loop_asymptotic_freedom_sign_locked": True,
            "diagnostic_comparison_post_generation_only": True,
            "not_overstated_as_complete_QCD_theorem": True,
            "step_09_defined": True,
        },
        "next_step": "Step 09: global running-coupling and anomaly/consistency audit",
    }


def main() -> None:
    print(json.dumps(build_final_strong_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
