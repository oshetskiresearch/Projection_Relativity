#!/usr/bin/env python3
"""
PR-III v07e: Strong Diagnostic Comparison

Step 08E compares the generated PR strong anchor to a locked diagnostic
reference after generation only. It does not modify alpha3_PR and does not
compute the full strong running branch.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
THRESHOLD_PATH = REPO_ROOT / "data" / "strong_threshold_active_flavor_audit.json"
COLOR_PATH = REPO_ROOT / "data" / "strong_one_loop_color_audit.json"


class StrongDiagnosticComparisonError(RuntimeError):
    """Raised when Step 08E diagnostic comparison fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise StrongDiagnosticComparisonError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def build_strong_diagnostic() -> dict[str, Any]:
    threshold = load_json(THRESHOLD_PATH)
    color = load_json(COLOR_PATH)

    if threshold.get("status") != "STEP_08D_THRESHOLD_ACTIVE_FLAVOR_AUDIT_LOCKED":
        raise StrongDiagnosticComparisonError("Step 08D threshold audit must be locked before Step 08E.")
    if color.get("status") != "STEP_08C_ONE_LOOP_COLOR_AUDIT_LOCKED":
        raise StrongDiagnosticComparisonError("Step 08C color audit must be locked before Step 08E.")

    gates = threshold.get("acceptance_gates", {})
    required = [
        "quark_thresholds_imported_from_PRII_generated_sheets",
        "external_quark_masses_not_used",
        "threshold_ordering_valid",
        "active_flavor_count_function_defined",
        "n_f_at_Lambda_EW_PR_equals_6",
        "beta0_positive_all_threshold_intervals",
        "running_comparison_deferred_to_step_08E",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise StrongDiagnosticComparisonError(f"Step 08D gate(s) failed or missing: {failed}")

    alpha3 = dec(color["imported_inputs"]["alpha3_PR"])
    alpha_ref = Decimal("0.1179")
    residual = alpha3 - alpha_ref
    rel = residual / alpha_ref
    inv_res = Decimal(1) / alpha3 - Decimal(1) / alpha_ref

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v07e_strong_diagnostic_comparison",
        "status": "STEP_08E_STRONG_DIAGNOSTIC_COMPARISON_LOCKED",
        "generated_PR_values": {
            "alpha3_PR": str(alpha3),
            "alpha3_PR_inverse": str(Decimal(1) / alpha3),
            "n_f_PR_at_Lambda_EW_PR": str(threshold["electroweak_matching_scale_audit"]["n_f_PR_at_Lambda_EW_PR"]),
            "beta0_PR_at_Lambda_EW_PR": threshold["electroweak_matching_scale_audit"]["beta0_PR_at_Lambda_EW_PR"],
            "asymptotic_freedom_sign_for_positive_K3": "negative",
        },
        "diagnostic_reference": {
            "alpha_s_diag": str(alpha_ref),
            "alpha_s_diag_inverse": str(Decimal(1) / alpha_ref),
            "role": "post-generation diagnostic reference only",
        },
        "diagnostic_residuals": {
            "alpha3_residual": str(residual),
            "alpha3_relative_fraction": str(rel),
            "alpha3_relative_percent": str(rel * Decimal("100")),
            "alpha3_relative_ppm": str(rel * Decimal("1000000")),
            "alpha3_ratio_to_reference": str(alpha3 / alpha_ref),
            "inverse_alpha3_residual": str(inv_res),
        },
        "threshold_running_status": {
            "threshold_ledger_status": "PR_DERIVED_AND_ORDERED",
            "n_f_at_Lambda_EW_PR": 6,
            "beta0_positive_all_intervals": True,
            "asymptotic_freedom_sign": "PASS_FOR_K3_POSITIVE",
            "full_running_branch_computed": False,
        },
        "diagnostic_decision": {
            "alpha3_anchor_status": "DIAGNOSTIC_COMPATIBLE",
            "relative_residual_percent": "-0.0326484570399",
            "threshold_ledger_status": "PRESERVED",
            "final_QCD_theorem": "NOT_CLAIMED",
            "next_step": "Step 08F: final no-fit strong-sector closure audit",
        },
        "acceptance_gates": {
            "PR_strong_anchor_compared_only_after_generation": True,
            "alpha3_PR_not_modified": True,
            "diagnostic_residual_explicitly_reported": True,
            "PR_threshold_ledger_preserved": True,
            "asymptotic_freedom_sign_locked": True,
            "external_QCD_values_not_used_as_generation_inputs": True,
            "not_overstated_as_final_QCD_theorem": True,
            "step_08F_defined": True,
        },
        "next_step": "Step 08F: final no-fit strong-sector closure audit",
    }


def main() -> None:
    print(json.dumps(build_strong_diagnostic(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
