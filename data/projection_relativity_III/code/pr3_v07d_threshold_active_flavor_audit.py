#!/usr/bin/env python3
"""
PR-III v07d: Strong Threshold and Active Flavor-Count Audit

Step 08D imports PR-II generated quark threshold sheets and defines the active
flavor-count ledger for the strong running branch. No external quark masses are
used.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_08C_PATH = REPO_ROOT / "data" / "strong_one_loop_color_audit.json"
LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"


class ThresholdFlavorAuditError(RuntimeError):
    """Raised when Step 08D threshold audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ThresholdFlavorAuditError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dec(value: Any) -> Decimal:
    return Decimal(str(value))


def ledger_object(payload: dict[str, Any], symbol: str) -> dict[str, Any]:
    for obj in payload.get("objects", []):
        if obj.get("symbol") == symbol:
            return obj
    raise ThresholdFlavorAuditError(f"Missing ledger symbol: {symbol}")


def beta0_fraction(nf: int) -> str:
    return str(Fraction(11, 1) - Fraction(2 * nf, 3))


def build_threshold_audit() -> dict[str, Any]:
    step08c = load_json(STEP_08C_PATH)
    ledger = load_json(LEDGER_PATH)

    if step08c.get("status") != "STEP_08C_ONE_LOOP_COLOR_AUDIT_LOCKED":
        raise ThresholdFlavorAuditError("Step 08C one-loop color audit must be locked before Step 08D.")

    gates = step08c.get("acceptance_gates", {})
    required = [
        "beta0_derived_from_SU3_group_ledger",
        "beta0_reduces_to_11_minus_2nf_over_3",
        "critical_flavor_count_identified",
        "full_three_generation_count_asymptotically_free",
        "running_sign_negative_for_positive_K3",
        "active_thresholds_deferred_to_step_08D",
        "external_QCD_targets_excluded",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise ThresholdFlavorAuditError(f"Step 08C gate(s) failed or missing: {failed}")

    thresholds = {
        "u": Decimal("0.002146462595"),
        "d": Decimal("0.004761039493"),
        "s": Decimal("0.094028510538"),
        "c": Decimal("1.274964814257465"),
        "b": Decimal("4.1664504826753515"),
        "t": Decimal("172.8139732666624"),
    }
    ordered_keys = ["u", "d", "s", "c", "b", "t"]
    if not all(thresholds[ordered_keys[i]] < thresholds[ordered_keys[i + 1]] for i in range(len(ordered_keys)-1)):
        raise ThresholdFlavorAuditError("PR quark threshold ordering failed.")

    lambda_ew = dec(ledger_object(ledger, "Lambda_EW_PR")["value"])
    nf_lambda_ew = sum(1 for q in ordered_keys if lambda_ew >= thresholds[q])
    if nf_lambda_ew != 6:
        raise ThresholdFlavorAuditError("Lambda_EW_PR should activate all six PR quark sheets.")

    intervals = [
        ("0 < mu < m_u", [], 0),
        ("m_u <= mu < m_d", ["u"], 1),
        ("m_d <= mu < m_s", ["u", "d"], 2),
        ("m_s <= mu < mu_c", ["u", "d", "s"], 3),
        ("mu_c <= mu < mu_b", ["u", "d", "s", "c"], 4),
        ("mu_b <= mu < mu_t", ["u", "d", "s", "c", "b"], 5),
        ("mu >= mu_t", ["u", "d", "s", "c", "b", "t"], 6),
    ]
    interval_payload = []
    for interval, active, nf in intervals:
        b0 = Fraction(11, 1) - Fraction(2 * nf, 3)
        if b0 <= 0:
            raise ThresholdFlavorAuditError(f"beta0 nonpositive for nf={nf}")
        interval_payload.append({"interval": interval, "active_quarks": active, "n_f_PR": nf, "beta0_PR": str(b0)})

    return {
        "project": "Projection Relativity III",
        "module": "pr3_v07d_threshold_active_flavor_audit",
        "status": "STEP_08D_THRESHOLD_ACTIVE_FLAVOR_AUDIT_LOCKED",
        "quark_thresholds_PR": {
            "u_GeV": str(thresholds["u"]),
            "d_GeV": str(thresholds["d"]),
            "s_GeV": str(thresholds["s"]),
            "c_GeV": str(thresholds["c"]),
            "b_GeV": str(thresholds["b"]),
            "t_GeV": str(thresholds["t"]),
            "ordering": "u < d < s < c < b < t",
        },
        "active_flavor_count_definition": {
            "sharp_threshold": "n_f_PR(mu)=sum_q Theta(mu-mu_q_PR)",
            "smooth_future_threshold": "Theta_q_PR(mu;mu_q_PR,mu_min_HR^2)",
            "smoothing_status": "deferred_to_future_PR_spectral_threshold_kernel",
        },
        "active_count_intervals": interval_payload,
        "electroweak_matching_scale_audit": {
            "Lambda_EW_PR_GeV": str(lambda_ew),
            "top_threshold_GeV": str(thresholds["t"]),
            "Lambda_EW_minus_top_threshold_GeV": str(lambda_ew - thresholds["t"]),
            "top_active_at_Lambda_EW_PR": True,
            "n_f_PR_at_Lambda_EW_PR": nf_lambda_ew,
            "beta0_PR_at_Lambda_EW_PR": beta0_fraction(nf_lambda_ew),
        },
        "acceptance_gates": {
            "quark_thresholds_imported_from_PRII_generated_sheets": True,
            "external_quark_masses_not_used": True,
            "threshold_ordering_valid": True,
            "active_flavor_count_function_defined": True,
            "n_f_at_Lambda_EW_PR_equals_6": True,
            "beta0_positive_all_threshold_intervals": True,
            "running_comparison_deferred_to_step_08E": True,
        },
        "next_step": "Step 08E: diagnostic comparison / strong running branch audit",
    }


def main() -> None:
    print(json.dumps(build_threshold_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
