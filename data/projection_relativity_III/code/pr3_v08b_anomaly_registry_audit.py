#!/usr/bin/env python3
"""
PR-III v08b: Anomaly Registry Audit

Step 09B audits local and global anomaly cancellation for the frozen PR
representation ledger. It inserts no new fields and uses no observed mixing data.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
GLOBAL_LEDGER_PATH = REPO_ROOT / "data" / "global_running_anomaly_ledger_seed.json"


class AnomalyRegistryAuditError(RuntimeError):
    """Raised when Step 09B anomaly audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AnomalyRegistryAuditError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_anomaly_registry() -> dict[str, Any]:
    global_ledger = load_json(GLOBAL_LEDGER_PATH)
    if global_ledger.get("status") != "STEP_09A_GLOBAL_LEDGER_LOCKED":
        raise AnomalyRegistryAuditError("Step 09A global ledger must be locked before Step 09B.")

    gates = global_ledger.get("acceptance_gates", {})
    required = [
        "step_05_alpha_closure_imported",
        "step_06_electroweak_closure_imported",
        "step_07_neutrino_closure_imported",
        "step_08_strong_closure_imported",
        "exact_all_orders_theorem_claims_excluded",
        "anomaly_and_consistency_audit_queue_defined",
        "step_09B_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise AnomalyRegistryAuditError(f"Step 09A gate(s) failed or missing: {failed}")

    Y_Q = Fraction(1, 3)
    Y_uc = Fraction(-4, 3)
    Y_dc = Fraction(2, 3)
    Y_L = Fraction(-1, 1)
    Y_ec = Fraction(2, 1)
    T3 = Fraction(1, 2)
    T2 = Fraction(1, 2)

    su3_cubed = 2 - 1 - 1
    su3_sq_u1 = 2 * T3 * Y_Q + T3 * Y_uc + T3 * Y_dc
    su2_sq_u1 = 3 * T2 * Y_Q + T2 * Y_L
    u1_cubed = 6 * Y_Q**3 + 3 * Y_uc**3 + 3 * Y_dc**3 + 2 * Y_L**3 + Y_ec**3
    grav_u1 = 6 * Y_Q + 3 * Y_uc + 3 * Y_dc + 2 * Y_L + Y_ec
    weak_doublets_per_gen = 4
    n_gen = 3
    total_doublets = weak_doublets_per_gen * n_gen

    checks = {
        "SU3_cubed": su3_cubed == 0,
        "SU3_squared_U1Y": su3_sq_u1 == 0,
        "SU2_squared_U1Y": su2_sq_u1 == 0,
        "U1Y_cubed": u1_cubed == 0,
        "gravity_squared_U1Y": grav_u1 == 0,
        "Witten": total_doublets % 2 == 0,
    }
    failed_checks = [name for name, ok in checks.items() if not ok]
    if failed_checks:
        raise AnomalyRegistryAuditError(f"Anomaly check(s) failed: {failed_checks}")

    return {
        "project": "Projection Relativity III",
        "dataset": "global_anomaly_registry_audit",
        "status": "STEP_09B_ANOMALY_REGISTRY_AUDIT_LOCKED",
        "input_policy": {
            "uses_only_representation_ledger": True,
            "external_fields_inserted": False,
            "observed_CKM_PMNS_used": False,
            "generation_values_modified": False,
        },
        "hypercharge_convention": {
            "residual_charge_operator": "Q=T3+Y/2",
            "normalization": "PR-II hypercharge convention",
        },
        "one_generation_left_weyl_ledger": [
            {"field": "Q_L", "representation": "(3,2)", "Y": "1/3", "multiplicity": 6},
            {"field": "u_R^c", "representation": "(3bar,1)", "Y": "-4/3", "multiplicity": 3},
            {"field": "d_R^c", "representation": "(3bar,1)", "Y": "2/3", "multiplicity": 3},
            {"field": "L_L", "representation": "(1,2)", "Y": "-1", "multiplicity": 2},
            {"field": "e_R^c", "representation": "(1,1)", "Y": "2", "multiplicity": 1},
            {"field": "nu_R^c_optional", "representation": "(1,1)", "Y": "0", "multiplicity": 1, "contribution": "zero"},
        ],
        "local_anomaly_sums_per_generation": {
            "SU3_cubed": {
                "formula": "2*A(3)-A(3bar)-A(3bar)",
                "value": str(su3_cubed),
                "status": "PASS",
            },
            "SU3_squared_U1Y": {
                "formula": "2*(1/2)*(1/3)+(1/2)*(-4/3)+(1/2)*(2/3)",
                "value": str(su3_sq_u1),
                "status": "PASS",
            },
            "SU2_squared_U1Y": {
                "formula": "3*(1/2)*(1/3)+1*(1/2)*(-1)",
                "value": str(su2_sq_u1),
                "status": "PASS",
            },
            "U1Y_cubed": {
                "formula": "6*(1/3)^3+3*(-4/3)^3+3*(2/3)^3+2*(-1)^3+2^3",
                "value": str(u1_cubed),
                "status": "PASS",
            },
            "gravity_squared_U1Y": {
                "formula": "6*(1/3)+3*(-4/3)+3*(2/3)+2*(-1)+2",
                "value": str(grav_u1),
                "status": "PASS",
            },
        },
        "global_SU2_Witten_audit": {
            "doublets_per_generation": str(weak_doublets_per_gen),
            "N_gen_PR": str(n_gen),
            "total_SU2_doublets": str(total_doublets),
            "is_even": True,
            "status": "PASS",
        },
        "residual_U1em_audit": {
            "projection": "SU(2)_L x U(1)_Y -> U(1)_em",
            "vectorlike_pairs": ["u_L/u_R", "d_L/d_R", "e_L/e_R"],
            "neutral_branch": "neutrino electrically neutral",
            "status": "VECTORLIKE_PASS",
        },
        "generation_scaling": {
            "anomalies_cancel_per_generation": True,
            "N_gen_PR": str(n_gen),
            "scaled_local_anomalies": "0",
        },
        "acceptance_gates": {
            "hypercharge_convention_fixed": True,
            "SU3_cubed_anomaly_cancels": True,
            "SU3_squared_U1_anomaly_cancels": True,
            "SU2_squared_U1_anomaly_cancels": True,
            "U1_cubed_anomaly_cancels": True,
            "gravity_squared_U1_anomaly_cancels": True,
            "Witten_anomaly_absent": True,
            "residual_U1em_vectorlike": True,
            "external_anomaly_canceling_fields_not_inserted": True,
            "step_09C_defined": True,
        },
        "next_step": "Step 09C: running-continuity audit",
    }


def main() -> None:
    print(json.dumps(build_anomaly_registry(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
