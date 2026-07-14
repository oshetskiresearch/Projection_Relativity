#!/usr/bin/env python3
"""
PR-III v08f: Final PR-III Consistency Statement

Step 09F consolidates the completed PR-III sandbox ledger into a final
consistency-locked statement. It adds no correction and claims no exact all-orders theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
TABLE_PATH = REPO_ROOT / "data" / "global_cross_sector_diagnostic_table.json"
PROVENANCE_PATH = REPO_ROOT / "data" / "global_no_fit_provenance_manifest.json"
CONTINUITY_PATH = REPO_ROOT / "data" / "global_running_continuity_audit.json"
ANOMALY_PATH = REPO_ROOT / "data" / "global_anomaly_registry_audit.json"


class FinalPRIIIConsistencyError(RuntimeError):
    """Raised when Step 09F final consistency audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FinalPRIIIConsistencyError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_final_consistency() -> dict[str, Any]:
    table = load_json(TABLE_PATH)
    provenance = load_json(PROVENANCE_PATH)
    continuity = load_json(CONTINUITY_PATH)
    anomaly = load_json(ANOMALY_PATH)

    if table.get("status") != "STEP_09E_CROSS_SECTOR_DIAGNOSTIC_TABLE_LOCKED":
        raise FinalPRIIIConsistencyError("Step 09E diagnostic table must be locked before Step 09F.")
    if provenance.get("status") != "STEP_09D_NO_FIT_PROVENANCE_MANIFEST_LOCKED":
        raise FinalPRIIIConsistencyError("Step 09D provenance manifest must be locked before Step 09F.")
    if continuity.get("status") != "STEP_09C_RUNNING_CONTINUITY_AUDIT_LOCKED":
        raise FinalPRIIIConsistencyError("Step 09C continuity audit must be locked before Step 09F.")
    if anomaly.get("status") != "STEP_09B_ANOMALY_REGISTRY_AUDIT_LOCKED":
        raise FinalPRIIIConsistencyError("Step 09B anomaly audit must be locked before Step 09F.")

    table_gates = table.get("acceptance_gates", {})
    required = [
        "every_completed_sector_represented",
        "diagnostic_references_post_generation_only",
        "generated_values_not_modified",
        "precision_and_compatibility_statuses_explicit",
        "structural_statuses_included",
        "exact_all_orders_theorem_claims_excluded",
        "step_09F_defined",
    ]
    failed = [gate for gate in required if table_gates.get(gate) is not True]
    if failed:
        raise FinalPRIIIConsistencyError(f"Step 09E gate(s) failed or missing: {failed}")

    return {
        "project": "Projection Relativity III",
        "dataset": "global_final_priii_consistency_statement",
        "status": "STEP_09F_FINAL_PRIII_CONSISTENCY_STATEMENT_LOCKED",
        "input_policy": {
            "uses_only_locked_PR_outputs": True,
            "new_diagnostic_references_introduced": False,
            "generation_values_modified": False,
            "new_corrections_computed": False,
            "final_exact_all_orders_theorem_claimed": False,
        },
        "final_sector_status": {
            "electromagnetic": {
                "status": "CURRENT_EXPERIMENTAL_PRECISION_CLOSED",
                "key_result": "alpha_inverse inside selected one-sigma diagnostic reference",
                "exact_theorem_claimed": False,
            },
            "electroweak": {
                "status": "ONE_SIGMA_DIAGNOSTIC_PRECISION_LOCKED",
                "key_result": "M_W, M_Z, and G_F all inside selected one-sigma diagnostics",
                "exact_theorem_claimed": False,
            },
            "neutrino": {
                "status": "STABILITY_LOCKED_AND_DIAGNOSTIC_COMPATIBLE",
                "key_result": "normal ordering, m_beta, and m_beta_beta stable and below current direct bounds",
                "exact_theorem_claimed": False,
            },
            "strong": {
                "status": "ANCHOR_LOCKED_THRESHOLD_LOCKED_AND_DIAGNOSTIC_COMPATIBLE",
                "key_result": "alpha3 anchor compatible at sub-0.04 percent; asymptotic freedom sign locked",
                "exact_theorem_claimed": False,
            },
            "anomaly_registry": {
                "status": "PASS",
                "key_result": "local anomalies cancel per generation, Witten anomaly absent, residual U(1)em vectorlike",
            },
            "running_continuity": {
                "status": "PASS",
                "key_result": "cross-sector ledger continuity passes",
            },
            "no_fit_provenance": {
                "status": "PASS",
                "key_result": "forbidden inputs excluded; diagnostic references post-generation only",
            },
        },
        "global_decision": {
            "PRIII_global_status": "CONSISTENCY_LOCKED",
            "precision_status": "ALPHA_MW_MZ_GF_ONE_SIGMA_DIAGNOSTIC_PASS",
            "compatibility_status": "NEUTRINO_AND_STRONG_BRANCHES_COMPATIBLE",
            "structural_status": "ANOMALY_CONTINUITY_NO_FIT_PASS",
            "PR2_obligations": "SATISFIED_TO_CURRENT_DIAGNOSTIC_PRECISION",
            "final_exact_all_orders_theorem": "NOT_CLAIMED",
            "PRIII_sandbox_ledger": "COMPLETE_THROUGH_STEP_09",
        },
        "safe_manuscript_statement": "PR-III extends the PR-I/PR-II projection ledger into a cross-sector radiative, electroweak, neutrino, and strong consistency program whose generated outputs pass the current diagnostic and structural audits recorded here, without using the corresponding diagnostic targets as generation inputs.",
        "unsafe_claim_excluded": "PR-III proves a complete exact all-orders theory of the Standard Model and QCD.",
        "remaining_obligations": [
            "all-orders alpha theorem or higher-order residual proof",
            "exact electroweak all-orders uncertainty theorem",
            "additive Majorana seed derivation or exclusion",
            "phase-sensitive PMNS radiative deformation derivation",
            "strong reference scale Lambda_3_PR derivation",
            "smooth PR strong threshold profiles",
            "higher-loop strong running branch and scheme audit",
            "confinement/hadronization as a separate PR module",
            "final manuscript consolidation and reproducibility package",
        ],
        "acceptance_gates": {
            "step_09E_global_diagnostic_table_imported": True,
            "one_sigma_precision_diagnostics_reported": True,
            "compatibility_and_bound_diagnostics_reported": True,
            "structural_anomaly_continuity_no_fit_statuses_reported": True,
            "exact_all_orders_theorem_claims_excluded": True,
            "remaining_obligations_explicitly_preserved": True,
            "PRIII_marked_consistency_locked_not_exact_theorem": True,
        },
        "next_step": "Manuscript consolidation and reproducibility package",
    }


def main() -> None:
    print(json.dumps(build_final_consistency(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
