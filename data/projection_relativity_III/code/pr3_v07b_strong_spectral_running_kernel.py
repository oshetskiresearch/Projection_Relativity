#!/usr/bin/env python3
"""
PR-III v07b: Strong Spectral / Running Kernel

Step 08B locks the PR-native strong spectral/running kernel architecture. It
computes no running correction and imports no external QCD target values.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

getcontext().prec = 80

REPO_ROOT = Path(__file__).resolve().parents[1]
STEP_08A_PATH = REPO_ROOT / "data" / "strong_phase_fiber_closure_seed.json"
KERNEL_SEED_PATH = REPO_ROOT / "data" / "pr_spectral_kernel_seed.json"


class StrongSpectralKernelError(RuntimeError):
    """Raised when Step 08B kernel locking fails."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise StrongSpectralKernelError(f"Missing JSON file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_strong_kernel_seed() -> dict[str, Any]:
    branch = load_json(STEP_08A_PATH)
    pr_kernel = load_json(KERNEL_SEED_PATH)

    if branch.get("status") != "STEP_08A_STRONG_BRANCH_LOCKED":
        raise StrongSpectralKernelError("Step 08A strong branch must be locked before Step 08B.")
    if pr_kernel.get("status") != "STEP_05C_KERNEL_ARCHITECTURE_LOCKED":
        raise StrongSpectralKernelError("PR spectral kernel architecture must be locked before Step 08B.")

    gates = branch.get("acceptance_gates", {})
    required = [
        "step_07_completion_verified",
        "alpha3_PR_imported_from_frozen_ledger",
        "SU3_group_ledger_locked",
        "strong_beta_running_object_defined_symbolically",
        "active_flavor_thresholds_deferred_to_PR_inputs",
        "external_QCD_targets_excluded",
        "step_08B_defined",
    ]
    failed = [gate for gate in required if gates.get(gate) is not True]
    if failed:
        raise StrongSpectralKernelError(f"Step 08A gate(s) failed or missing: {failed}")

    alpha3 = Decimal(str(branch["strong_anchor"]["alpha3_PR"]))
    mu_gap = Decimal(str(pr_kernel["spectral_regulator"]["mu_min_squared_HR"]))
    if alpha3 <= 0:
        raise StrongSpectralKernelError("alpha3_PR must be positive.")
    if mu_gap <= 0:
        raise StrongSpectralKernelError("PR spectral gap must be positive.")

    nc = 3
    ca = Fraction(3, 1)
    cf = Fraction(4, 3)
    tf = Fraction(1, 2)

    return {
        "project": "Projection Relativity III",
        "dataset": "strong_spectral_running_kernel_seed",
        "status": "STEP_08B_STRONG_SPECTRAL_RUNNING_KERNEL_LOCKED",
        "input_policy": {
            "uses_only_frozen_PR_values": True,
            "external_QCD_targets_used": False,
            "diagnostic_comparisons_deferred": True,
            "running_correction_computed": False,
        },
        "strong_anchor": {
            "alpha3_PR": str(alpha3),
            "source": "Step 08A frozen PR-II compact-boundary strong anchor",
        },
        "su3_group_ledger": {
            "group": "SU(3)_c",
            "N_c": str(nc),
            "adjoint_dimension": str(nc * nc - 1),
            "C_A": str(ca),
            "C_F": str(cf),
            "T_F": str(tf),
        },
        "running_equation": {
            "symbolic_beta": "mu*d(alpha3_PR)/dmu = beta3_PR(alpha3, P_color, K3_PR)",
            "one_loop_form": "beta3_PR ~ -(alpha3_PR^2/(2*pi))*beta0_PR*K3_PR + ...",
            "beta0_form": "beta0_PR=(11/3)*C_A-(4/3)*T_F*n_f_PR",
            "n_f_PR_status": "deferred_to_PR_threshold_audit",
        },
        "strong_supertrace_registry": [
            {"block": "gluon_adjoint", "operator": "O_g^{ab,mu nu}", "status": "included"},
            {"block": "color_ghosts", "operator": "M_gh^{ab}", "status": "included"},
            {"block": "quark_color_sheets", "operator": "D_q", "status": "included_after_PR_threshold_import"},
            {"block": "color_neutral_leptons", "operator": "none", "status": "excluded"},
            {"block": "electroweak_residual_backgrounds", "operator": "external_to_pure_SU3_kernel", "status": "excluded_from_direct_color_trace"},
        ],
        "strong_kernel_class": {
            "discrete_form": "K_3a_PR(mu0_to_mu)=sum_n omega_3a_n log((M_a^2+mu^2+mu_n^2*Lambda_3^2)/(M_a^2+mu0^2+mu_n^2*Lambda_3^2))-R_3a_run",
            "support_condition": "mu_n^2 >= mu_min_HR^2 > 0",
            "mu_min_HR_squared": str(mu_gap),
            "reference_subtraction": "R_3a_run preserves PR alpha3 anchor and cannot force diagnostic alpha_s agreement",
            "cutoff_policy": "no arbitrary cutoff",
        },
        "threshold_policy": {
            "allowed_sources": [
                "PR-II quark mass sheets once imported from frozen source",
                "PR-III derived threshold values",
                "symbolic thresholds pending PR source synchronization",
                "PR spectral gap and boundary anchors",
            ],
            "forbidden_sources": [
                "external quark masses",
                "PDG quark mass tables",
                "hadron masses as tuning targets",
                "external Lambda_MSbar",
                "threshold choices selected to force alpha_s agreement",
            ],
        },
        "reference_scale_policy": {
            "Lambda3_PR_status": "symbolic_until_derived",
            "provisional_symbolic_map": "Lambda3_PR = Lambda_EW_PR * Xi3_PR",
            "Xi3_PR_status": "to_be_derived",
            "external_Lambda_MSbar_allowed": False,
        },
        "acceptance_gates": {
            "step_08A_anchor_and_group_ledger_imported": True,
            "strong_supertrace_registry_defined": True,
            "strong_kernel_reference_normalized": True,
            "spectral_support_uses_positive_gap": True,
            "thresholds_restricted_to_PR_or_symbolic": True,
            "external_QCD_targets_excluded": True,
            "running_correction_not_computed_prematurely": True,
            "step_08C_defined": True,
        },
        "next_step": "Step 08C: one-loop color audit and asymptotic-freedom sign",
    }


def main() -> None:
    print(json.dumps(build_strong_kernel_seed(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
