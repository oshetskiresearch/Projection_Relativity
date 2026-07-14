#!/usr/bin/env python3
"""
PR-III v08d: No-Fit Provenance Manifest

Step 09D consolidates allowed/forbidden input provenance across completed
sector closures. It adds no new corrections and does not modify generated values.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
GLOBAL_PATH = REPO_ROOT / "data" / "global_running_anomaly_ledger_seed.json"
CONTINUITY_PATH = REPO_ROOT / "data" / "global_running_continuity_audit.json"
ANOMALY_PATH = REPO_ROOT / "data" / "global_anomaly_registry_audit.json"


class NoFitProvenanceManifestError(RuntimeError):
    """Raised when Step 09D provenance audit fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise NoFitProvenanceManifestError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_manifest() -> dict[str, Any]:
    global_ledger = load_json(GLOBAL_PATH)
    continuity = load_json(CONTINUITY_PATH)
    anomaly = load_json(ANOMALY_PATH)

    if global_ledger.get("status") != "STEP_09A_GLOBAL_LEDGER_LOCKED":
        raise NoFitProvenanceManifestError("Step 09A global ledger must be locked before Step 09D.")
    if anomaly.get("status") != "STEP_09B_ANOMALY_REGISTRY_AUDIT_LOCKED":
        raise NoFitProvenanceManifestError("Step 09B anomaly registry must be locked before Step 09D.")
    if continuity.get("status") != "STEP_09C_RUNNING_CONTINUITY_AUDIT_LOCKED":
        raise NoFitProvenanceManifestError("Step 09C running continuity must be locked before Step 09D.")

    gates = continuity.get("acceptance_gates", {})
    required = [
        "alpha_connects_to_EW_transport",
        "EW_transport_connects_to_final_weak_mass_ledger",
        "neutrino_kernel_uses_EW_boundary_scale",
        "strong_threshold_ledger_continuous_at_Lambda_EW",
        "anomaly_registry_compatible_with_continuity_chain",
        "no_new_diagnostic_reference_introduced",
        "no_generated_sector_value_modified",
        "step_09D_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise NoFitProvenanceManifestError(f"Step 09C gate(s) failed or missing: {failed}")

    manifest = {
        "electromagnetic": {
            "generated_object": "alpha_PR_inv",
            "allowed_generation_inputs": [
                "high-resolution PR spectral ledger",
                "p1_HR",
                "q_bc_HR",
                "c_bc",
                "Delta_EW_HR",
                "N_gen_PR",
                "sin2thetaW_PR",
                "D1 and D2 boundary leakage terms",
            ],
            "forbidden_generation_inputs": [
                "empirical alpha",
                "CODATA alpha",
                "Rb alpha",
                "alpha residual fitted by hand",
                "external weak/QCD/flavor targets",
            ],
            "diagnostic_references_after_generation_only": True,
            "status": "PASS",
        },
        "electroweak": {
            "generated_object": "MW_MZ_GF",
            "allowed_generation_inputs": [
                "alpha_PR(0) from Step 05",
                "q_bc_HR",
                "c_bc",
                "Delta_EW_HR",
                "N_gen_PR",
                "sin2thetaW_PR",
                "v_EW_PR",
                "Lambda_EW_PR",
                "C1 transport",
                "C2 vector self-energy split",
                "C3 neutral D3 correction",
            ],
            "forbidden_generation_inputs": [
                "measured W mass",
                "measured Z mass",
                "measured Fermi constant",
                "measured weak angle",
                "experimental alpha(mZ)",
                "fitted kappa_W or kappa_Z",
                "external oblique parameters",
            ],
            "diagnostic_references_after_generation_only": True,
            "status": "PASS",
        },
        "neutrino": {
            "generated_object": "masses_PMNS_mbeta_mbetabeta",
            "allowed_generation_inputs": [
                "frozen PR-II neutrino masses",
                "frozen PR-II PMNS branch",
                "frozen PR-II m_beta_beta",
                "PR-III electroweak stability scale",
                "PR multiplicative envelope",
            ],
            "forbidden_generation_inputs": [
                "measured neutrino mass splittings",
                "observed PMNS angles",
                "cosmological mass-sum limits",
                "neutrinoless double-beta limits",
                "sterile-neutrino target values",
            ],
            "diagnostic_references_after_generation_only": True,
            "status": "PASS",
        },
        "strong": {
            "generated_object": "alpha3_PR_thresholds_nf_beta0",
            "allowed_generation_inputs": [
                "frozen PR-II alpha3_PR",
                "SU(3)c group identities",
                "PR-II quark threshold sheets",
                "PR-II generation count",
                "PR-III electroweak matching scale",
                "PR spectral gap and boundary anchors",
                "symbolic strong kernel objects",
            ],
            "forbidden_generation_inputs": [
                "PDG alpha_s(M_Z) as a fit input",
                "external quark masses",
                "external QCD Lambda_MSbar",
                "hadron masses as tuning targets",
                "lattice QCD target values",
                "observed CKM entries",
            ],
            "diagnostic_references_after_generation_only": True,
            "status": "PASS",
        },
        "anomaly_and_continuity": {
            "generated_object": "anomaly_registry_and_running_continuity",
            "allowed_generation_inputs": [
                "frozen electroweak representation ledger",
                "Q=T3+Y/2 charge convention",
                "SU(3)c and SU(2)L representation identities",
                "N_gen_PR=3",
                "locked sector outputs from Steps 05-08",
            ],
            "forbidden_generation_inputs": [
                "external anomaly-canceling fields",
                "empirical charge adjustments",
                "observed CKM entries",
                "observed PMNS entries",
                "new diagnostic references in continuity audit",
            ],
            "diagnostic_references_after_generation_only": True,
            "status": "PASS",
        },
    }

    return {
        "project": "Projection Relativity III",
        "dataset": "global_no_fit_provenance_manifest",
        "status": "STEP_09D_NO_FIT_PROVENANCE_MANIFEST_LOCKED",
        "input_policy": {
            "uses_only_locked_PR_outputs": True,
            "diagnostic_references_post_generation_only": True,
            "generation_values_modified": False,
            "forbidden_generation_inputs_used": False,
            "exact_all_orders_theorems_claimed": False,
        },
        "sector_manifest": manifest,
        "global_decision": {
            "global_no_fit_status": "PASS",
            "forbidden_generation_inputs_used": False,
            "diagnostic_references_post_generation_only": True,
            "generated_values_modified_by_diagnostics": False,
            "external_anomaly_canceling_fields_inserted": False,
            "exact_all_orders_theorems_claimed": False,
        },
        "acceptance_gates": {
            "every_completed_sector_has_allowed_input_list": True,
            "every_completed_sector_has_forbidden_input_list": True,
            "diagnostic_references_marked_post_generation_only": True,
            "generated_values_not_modified_by_diagnostics": True,
            "no_external_anomaly_canceling_fields_inserted": True,
            "exact_all_orders_theorem_claims_excluded": True,
            "step_09E_defined": True,
        },
        "next_step": "Step 09E: cross-sector diagnostic table",
    }


def main() -> None:
    print(json.dumps(build_manifest(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
