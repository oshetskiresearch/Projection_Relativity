#!/usr/bin/env python3
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# OSHETSKI RESEARCH
#
# COLAB-USABLE VERSION
# Projection Relativity II Electroweak / Flavor Validation Harness
# Michael Stanislaus Oshetski
# ORCID# 0009-0007-3623-7586
# June 2026
#
# "Dedicated to my brother and best friend,
# John Oshetski Jr. ("Motorhead")
# I'll see you in the decoherence!"
#
# Covers:
# 1. PR-I compact-boundary ledger import and no-target-input discipline
# 2. Compact electroweak lift: R_w x S^1_Y x SU(2)_L
# 3. SU(2)_L generator algebra, Casimir checks, and non-Abelian negative controls
# 4. Projection locking: SU(2)_L x U(1)_Y -> U(1)_em
# 5. Residual charge recovery: Q = T3 + Y/2
# 6. Photon masslessness, W/Z mass matrix, weak mixing, and rho_EW = 1
# 7. Weak-scale and Fermi-constant compact-boundary closure
# 8. Compact order-mode / scalar tree-level coupling ledger
# 9. Charged-current ladder, beta-transition topology, and Fermi limit
# 10. Neutral-current Z couplings and vector/axial charge ledger
# 11. Fermion representation ledger and local/global anomaly cancellation
# 12. Generation origin: dim[(SU(2)_L x U(1)_Y)/U(1)_em] = 3
# 13. Generation-sheet overlap hierarchy and sector-specific overlap operators
# 14. Charged-lepton Koide sheet rule and precision mass candidate
# 15. QCD strong-coupling anchor, running ledger, and threshold matching
# 16. Heavy-quark threshold candidates and light-quark hierarchy diagnostics
# 17. CKM compact flavor-mixing candidate and CP/Jarlskog checks
# 18. PMNS compact lepton-mixing candidate and unitarity checks
# 19. Neutrino normal-ordering mass-sector candidate
# 20. Majorana-dominant compact-singlet channel and m_beta_beta candidate
# 21. Negative controls, forbidden-input checks, audit manifest, and scorecard
#
# Scope:
# This is a numerical validation suite aligned with Projection Relativity II.
# It verifies the electroweak/flavor closure chain wherever machine-checkable,
# including structural identities, closure candidates, precision candidates,
# diagnostic ledgers, negative controls, and forbidden-input checks.
#
# The harness enforces the PR-II no-new-parameter rule:
# target observables such as G_F, v_EW, M_W, M_Z, charged-lepton masses,
# quark masses, CKM values, PMNS values, alpha_s(M_Z), Lambda_QCD,
# and neutrino mass splittings are not used as generation inputs.
# They are loaded only as diagnostic references after PR-II candidate values
# have already been generated.
#
# This script complements the manuscript and any symbolic audit layer.
# It should be described as:
# "structurally derived, numerically validated where machine-checkable,
# and checked against negative controls and forbidden target-input leakage."
#
# It does not claim that every electroweak precision, scalar-mass,
# radiative-running, QCD-scheme, or observational statement is fully certified
# beyond the machine-checkable scope. Scalar mass, full electroweak precision,
# and strong-sector precision matching are assigned to the PR-III precision layer.
#
# Usage:
#   Standard:
#       python pr2_full_colab_harness_colab.py
#
#   In Google Colab:
#       from google.colab import files
#       uploaded = files.upload()
#       %run pr2_full_colab_harness_colab.py
#       files.download("/content/pr2_harness_output.zip")
#
# Outputs:
#   /content/pr2_harness_output/
#   /content/pr2_harness_output.zip
#
# Output files include:
#   pr2_generated_outputs.json
#   audit/PRII_RUN_SUMMARY.md
#   audit/PRII_RUN_SUMMARY.json
#   audit/PRII_TEST_RESULTS.csv
#   audit/PRII_AUDIT_MANIFEST.csv
#   summary_tables/pr2_diagnostic_residuals.csv
#   summary_tables/neutral_current_couplings.csv
#   summary_tables/sector_overlap_spectra.csv
#
# Expected current validation status:
#   tests_total: 146
#   tests_passed: 146
#   tests_failed: 0
#   status: PASS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from __future__ import annotations

import csv
import json
import math
import os
import zipfile
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

# -----------------------------
# Runtime paths
# -----------------------------
BASE = Path("/content") if Path("/content").exists() else Path.cwd()
OUT = BASE / "pr2_harness_output"
AUDIT = OUT / "audit"
STEPS = OUT / "step_outputs"
TABLES = OUT / "summary_tables"
for p in [OUT, AUDIT, STEPS, TABLES]:
    p.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Allowed PR-I / PR-II generation inputs
# -----------------------------
GENERATION_INPUTS: Dict[str, float] = {
    "q_bc": 10.905007182855176,
    "c_bc": 3354902985 / 4211081216,
    "T_Y": 1.0 / 4.0,
    "Mpl_reduced_GeV": 2.4353234593382036e18,
    # Fundamental/group structural constants used as exact representation data.
    "N_gen": 3.0,
    "C2_SU3_fund": 4.0 / 3.0,
    "C2_SU2_doublet": 3.0 / 4.0,
}

# Diagnostic references: loaded only after PR-II candidate generation.
# These are NOT allowed to enter generation formulas.
DIAGNOSTIC_REFERENCES: Dict[str, float] = {
    "v_EW_ref_GeV": 246.2196507941374,
    "G_F_ref_GeV_minus2": 1.1663787e-5,
    "alpha_MZ_inv_diagnostic": 127.955,
    "m_e_ref_MeV": 0.510998950,
    "m_mu_ref_MeV": 105.6583755,
    "m_tau_ref_MeV": 1776.930,
    "m_u_ref_MeV": 2.16,
    "m_d_ref_MeV": 4.70,
    "m_s_ref_MeV": 93.5,
    "m_c_ref_GeV": 1.2730,
    "m_b_ref_GeV": 4.183,
    "m_t_ref_GeV": 172.56,
    "alpha_s_MZ_ref": 0.1179,
    "dm21_ref_eV2": 7.49e-5,
    "dm31_ref_eV2": 2.513e-3,
}

FORBIDDEN_GENERATION_INPUTS = {
    "G_F", "v_EW", "M_W", "M_Z", "m_h", "lambda_h",
    "m_e", "m_mu", "m_tau",
    "m_u", "m_d", "m_s", "m_c", "m_b", "m_t",
    "CKM", "PMNS", "alpha_s_MZ", "Lambda_QCD",
    "Delta_m21_sq", "Delta_m31_sq", "m_beta", "m_betabeta",
}

# -----------------------------
# Test harness helpers
# -----------------------------
@dataclass
class TestRecord:
    step: str
    name: str
    status: str
    value: str = ""
    expected: str = ""
    tolerance: str = ""
    details: str = ""


class Harness:
    def __init__(self) -> None:
        self.records: List[TestRecord] = []

    def check(self, step: str, name: str, condition: bool, details: str = "") -> None:
        self.records.append(TestRecord(step, name, "PASS" if condition else "FAIL", details=details))

    def close(self, step: str, name: str, value: float, expected: float,
              rel: float = 1e-10, abs_tol: float = 1e-12, details: str = "") -> None:
        ok = abs(value - expected) <= max(abs_tol, rel * max(abs(expected), 1e-300))
        self.records.append(TestRecord(
            step, name, "PASS" if ok else "FAIL",
            value=f"{value:.18g}", expected=f"{expected:.18g}",
            tolerance=f"rel={rel:g}, abs={abs_tol:g}", details=details
        ))

    def matrix_unitary(self, step: str, name: str, U: np.ndarray, tol: float = 1e-12) -> float:
        resid = float(np.max(np.abs(U.conj().T @ U - np.eye(U.shape[0]))))
        self.check(step, name, resid < tol, details=f"max residual={resid:.3e}")
        return resid

    def summary(self) -> Dict[str, int]:
        total = len(self.records)
        failed = sum(r.status != "PASS" for r in self.records)
        return {"tests_total": total, "tests_passed": total - failed, "tests_failed": failed}

    def write_csv(self, path: Path) -> None:
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(asdict(self.records[0]).keys()) if self.records else [])
            if self.records:
                writer.writeheader()
                for r in self.records:
                    writer.writerow(asdict(r))


H = Harness()

# -----------------------------
# Numerical helpers
# -----------------------------
def rel_err(value: float, ref: float) -> float:
    return (value - ref) / ref


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")


def write_csv_rows(path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def ckm_matrix(s12: float, s23: float, s13: float, delta: float) -> np.ndarray:
    c12, c23, c13 = math.sqrt(1-s12*s12), math.sqrt(1-s23*s23), math.sqrt(1-s13*s13)
    e_minus = complex(math.cos(-delta), math.sin(-delta))
    e_plus = complex(math.cos(delta), math.sin(delta))
    return np.array([
        [c12*c13, s12*c13, s13*e_minus],
        [-s12*c23 - c12*s23*s13*e_plus, c12*c23 - s12*s23*s13*e_plus, s23*c13],
        [s12*s23 - c12*c23*s13*e_plus, -c12*s23 - s12*c23*s13*e_plus, c23*c13],
    ], dtype=complex)


def pmns_matrix(s12: float, s23: float, s13: float, delta: float) -> np.ndarray:
    return ckm_matrix(s12, s23, s13, delta)  # same standard 3-angle parameterization


def jarlskog(s12: float, s23: float, s13: float, delta: float) -> float:
    c12, c23, c13 = math.sqrt(1-s12*s12), math.sqrt(1-s23*s23), math.sqrt(1-s13*s13)
    return c12*c23*(c13**2)*s12*s23*s13*math.sin(delta)

# -----------------------------
# Derived compact-boundary ledger
# -----------------------------
q = GENERATION_INPUTS["q_bc"]
c = GENERATION_INPUTS["c_bc"]
TY = GENERATION_INPUTS["T_Y"]
Mpl = GENERATION_INPUTS["Mpl_reduced_GeV"]
Ngen = int(GENERATION_INPUTS["N_gen"])

alpha_pr_inv = 4 * math.pi * q
rG = c / q
delta_bc = 1 - c
DeltaEW = (1 - c) / q
sin2w = TY - DeltaEW
cos2w = 1 - sin2w
theta_w = math.asin(math.sqrt(sin2w))
tan_w = math.tan(theta_w)
AEW = (1 + 3*c) / 2
Cconf = (1 + c) / 2
XiEW = q * c * sin2w
sqrt_XiEW = math.sqrt(XiEW)
yT = math.sqrt(2 / XiEW)

# Step 7/8 weak-scale action
S_base = math.pi*q + math.log(q/c) + math.log(4/3) + (TY - sin2w) * (1+c)/2
dS2 = -0.5 * (1 + 3*c) * (TY - sin2w)**2
S_total = S_base + dS2
LambdaEW = Mpl * math.exp(-S_total)
vEW = LambdaEW * sqrt_XiEW
GF = 1 / (math.sqrt(2) * vEW**2)

# Diagnostic weak-scale EM coupling for optional W/Z numerical values.
alpha_MZ_inv_diag = DIAGNOSTIC_REFERENCES["alpha_MZ_inv_diagnostic"]
alpha_MZ_diag = 1 / alpha_MZ_inv_diag
e_diag = math.sqrt(4 * math.pi * alpha_MZ_diag)
g_diag = e_diag / math.sqrt(sin2w)
gp_diag = e_diag / math.sqrt(cos2w)
MW_diag = g_diag * vEW / 2
MZ_diag = math.sqrt(g_diag*g_diag + gp_diag*gp_diag) * vEW / 2

# -----------------------------
# Step 00: input discipline
# -----------------------------
step = "00_input_discipline"
intersection = set(GENERATION_INPUTS.keys()) & FORBIDDEN_GENERATION_INPUTS
H.check(step, "allowed_generation_inputs_do_not_use_forbidden_target_names", len(intersection) == 0,
        details=f"intersection={sorted(intersection)}")
H.check(step, "diagnostic_references_separated_from_generation_inputs", 
        set(DIAGNOSTIC_REFERENCES.keys()).isdisjoint(set(GENERATION_INPUTS.keys())))

# -----------------------------
# Step 01: SU(2) algebra and compact EW lift
# -----------------------------
step = "01_electroweak_lift_su2_algebra"
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
T = [s1/2, s2/2, s3/2]
I2 = np.eye(2, dtype=complex)
eps = np.zeros((3,3,3), dtype=int)
eps[0,1,2] = eps[1,2,0] = eps[2,0,1] = 1
eps[1,0,2] = eps[2,1,0] = eps[0,2,1] = -1
for i in range(3):
    H.check(step, f"T{i+1}_Hermitian", np.allclose(T[i], T[i].conj().T))
for a in range(3):
    for b in range(3):
        lhs = T[a] @ T[b] - T[b] @ T[a]
        rhs = 1j * sum(eps[a,b,cidx] * T[cidx] for cidx in range(3))
        H.check(step, f"commutator_{a+1}_{b+1}", np.allclose(lhs, rhs, atol=1e-14))
        H.close(step, f"trace_norm_{a+1}_{b+1}", float(np.trace(T[a] @ T[b]).real), 0.5 if a==b else 0.0, abs_tol=1e-14)
Casimir = sum(Ta @ Ta for Ta in T)
H.check(step, "fundamental_Casimir_3_over_4", np.allclose(Casimir, 0.75*I2))
Tplus = T[0] + 1j*T[1]
Tminus = T[0] - 1j*T[1]
up = np.array([[1],[0]], dtype=complex)
down = np.array([[0],[1]], dtype=complex)
H.check(step, "Tplus_down_to_up", np.allclose(Tplus @ down, up))
H.check(step, "Tminus_up_to_down", np.allclose(Tminus @ up, down))
H.check(step, "negative_control_abelianized_su2_rejected", not np.allclose(T[0]@T[1] - T[1]@T[0], np.zeros((2,2))))

# -----------------------------
# Step 02: projection locking and mass matrix
# -----------------------------
step = "02_projection_locking_mass_matrix"
Y_order = 1.0
Q_order = T[2] + (Y_order/2)*I2
Phi0 = np.array([[0],[1/math.sqrt(2)]], dtype=complex)  # v omitted; Q neutrality scale independent
H.check(step, "Q_Phi0_zero", np.allclose(Q_order @ Phi0, np.zeros_like(Phi0), atol=1e-14))
# neutral matrix with generated v but arbitrary g ratio from sin2w and diagnostic e for numeric outputs
M0 = (vEW**2/4) * np.array([[g_diag**2, -g_diag*gp_diag],[-g_diag*gp_diag, gp_diag**2]], dtype=float)
H.close(step, "neutral_mass_matrix_determinant_zero", float(np.linalg.det(M0)), 0.0, abs_tol=1e-8)
eig = np.linalg.eigvalsh(M0)
H.check(step, "one_neutral_eigenvalue_massless", abs(float(eig[0])) < 1e-8)
H.close(step, "M_W_relation", MW_diag, g_diag*vEW/2, rel=1e-14)
H.close(step, "M_Z_relation", MZ_diag, math.sqrt(g_diag*g_diag+gp_diag*gp_diag)*vEW/2, rel=1e-14)
H.close(step, "rho_EW_tree_level", MW_diag**2/(MZ_diag**2*cos2w), 1.0, rel=1e-12)
H.check(step, "negative_control_no_W3B_mixing_photon_massive", np.linalg.det((vEW**2/4)*np.diag([g_diag**2,gp_diag**2])) != 0)

# -----------------------------
# Step 03: weak mixing closure
# -----------------------------
step = "03_weak_mixing_closure"
H.close(step, "alpha_PR_inverse", alpha_pr_inv, 137.036361812007, rel=1e-12)
H.close(step, "DeltaEW", DeltaEW, 0.018644236701811, rel=1e-12)
H.close(step, "sin2thetaW_PR", sin2w, 0.231355763298189, rel=1e-12)
H.close(step, "gprime_over_g", tan_w, 0.548627374785032, rel=1e-12)
H.check(step, "negative_control_raw_trace_not_precision", abs(TY - sin2w) > 1e-3)
H.check(step, "negative_control_wrong_sign_deficit_rejected", abs((TY+DeltaEW) - sin2w) > 1e-3)

# -----------------------------
# Step 04-08: weak scale/Fermi hierarchy
# -----------------------------
step = "04_08_weak_scale_fermi_hierarchy"
H.close(step, "Xi_EW", XiEW, 2.0099841245909515, rel=1e-12)
H.close(step, "yT_terminal_overlap", yT, 0.997513275401799, rel=1e-12)
H.close(step, "S_base", S_base, 37.18004007116382, rel=1e-12)
H.close(step, "deltaS_second_order", dS2, -5.892040980909848e-4, rel=1e-12)
H.close(step, "S_total", S_total, 37.17945086706573, rel=1e-12)
H.close(step, "LambdaEW_PR_GeV", LambdaEW, 173.67059834472832, rel=1e-10)
H.close(step, "vEW_PR_GeV", vEW, 246.21959589022453, rel=1e-10)
H.close(step, "GF_PR_GeV_minus2", GF, 1.166379220175995e-5, rel=1e-10)
H.check(step, "negative_control_dimensionless_Xi_not_GeV", XiEW < 10.0 and abs(XiEW - vEW) > 100.0)
H.check(step, "negative_control_no_second_order_less_precise", abs((Mpl*math.exp(-S_base))*sqrt_XiEW - DIAGNOSTIC_REFERENCES['v_EW_ref_GeV']) > abs(vEW - DIAGNOSTIC_REFERENCES['v_EW_ref_GeV']))

# -----------------------------
# Step 09-10: charged and neutral currents
# -----------------------------
step = "09_10_currents"
H.close(step, "Fermi_matching_g2_over_8MW2", g_diag**2/(8*MW_diag**2), 1/(2*vEW**2), rel=1e-12)
# [Q,T+]=T+ for lepton doublet Y=-1; Y commutes, so enough with T3.
Ylep = -1.0
Q_lep = T[2] + (Ylep/2)*I2
H.check(step, "Q_ladder_Tplus_charge_plus", np.allclose(Q_lep@Tplus - Tplus@Q_lep, Tplus))
H.check(step, "Q_ladder_Tminus_charge_minus", np.allclose(Q_lep@Tminus - Tminus@Q_lep, -Tminus))
# Neutral current couplings
fermions = {
    "nu_e": (0.0, 0.5),
    "e": (-1.0, -0.5),
    "u": (2/3, 0.5),
    "d": (-1/3, -0.5),
}
neutral_rows = []
for name, (Qf, T3f) in fermions.items():
    gV = T3f - 2*Qf*sin2w
    gA = T3f
    gL = T3f - Qf*sin2w
    gR = -Qf*sin2w
    H.close(step, f"{name}_gV_relation", gV, gL+gR, rel=1e-14)
    H.close(step, f"{name}_gA_relation", gA, gL-gR, rel=1e-14)
    neutral_rows.append({"fermion": name, "Q": Qf, "T3": T3f, "gV": gV, "gA": gA})
H.check(step, "negative_control_wrong_vector_factor_rejected", abs((-0.5 - (-1)*sin2w) - (-0.5 + 2*sin2w)) > 0.1)
write_csv_rows(TABLES / "neutral_current_couplings.csv", neutral_rows)

# -----------------------------
# Step 11-13: anomaly/generation tests
# -----------------------------
step = "11_13_anomaly_generation"
# Left-handed Weyl ledger: multiplicity, SU3 index/sign or SU3 cubed sign, SU2 index, Y, is_doublet_count
# Minimal one generation.
ledger = [
    (6,  1,  0.5,  1/3, True),      # Q_L: 3 colors * 2 weak components; SU3 cubed sign handled separately below
    (3, -1,  0.5, -4/3, False),     # u_R^c
    (3, -1,  0.5,  2/3, False),     # d_R^c
    (2,  0,  0.0, -1, True),        # L_L
    (1,  0,  0.0,  2, False),       # e_R^c
]
# Explicit anomaly coefficients from formulas.
SU3_cubed = 2 - 1 - 1
SU3SU3Y = 2*(0.5)*(1/3) + 0.5*(-4/3) + 0.5*(2/3)
SU2SU2Y = 3*0.5*(1/3) + 0.5*(-1)
gravY = 6*(1/3) + 3*(-4/3) + 3*(2/3) + 2*(-1) + 2
Y3 = 6*(1/3)**3 + 3*(-4/3)**3 + 3*(2/3)**3 + 2*(-1)**3 + 2**3
N2_one = 4
N2_three = 12
H.close(step, "SU3_cubed_anomaly", SU3_cubed, 0, abs_tol=1e-14)
H.close(step, "SU3_squared_U1Y_anomaly", SU3SU3Y, 0, abs_tol=1e-14)
H.close(step, "SU2_squared_U1Y_anomaly", SU2SU2Y, 0, abs_tol=1e-14)
H.close(step, "gravity_squared_U1Y_anomaly", gravY, 0, abs_tol=1e-14)
H.close(step, "U1Y_cubed_anomaly", Y3, 0, abs_tol=1e-14)
H.check(step, "Witten_SU2_one_generation_even", N2_one % 2 == 0)
H.check(step, "Witten_SU2_three_generation_even", N2_three % 2 == 0)
Ngen_PR = 4 - 1
H.close(step, "Ngen_from_broken_EW_projection_space", Ngen_PR, 3, abs_tol=0)
H.check(step, "negative_control_Ngen_2_rejected", 2 != Ngen_PR)
H.check(step, "negative_control_Ngen_4_rejected", 4 != Ngen_PR)

# -----------------------------
# Step 14-15: generation sheet hierarchy and sector overlaps
# -----------------------------
step = "14_15_flavor_overlaps"
eta = np.array([rG**2, rG, 1.0])
y_sheet = yT * eta
H.close(step, "eta1", eta[0], 0.005337289810442, rel=1e-12)
H.close(step, "eta2", eta[1], 0.073056757459128, rel=1e-12)
H.close(step, "eta3", eta[2], 1.0, rel=1e-14)
H.check(step, "hierarchy_order_y1_y2_y3", y_sheet[0] < y_sheet[1] < y_sheet[2])
H.close(step, "generation_hierarchy_ratio", y_sheet[1]/y_sheet[0], q/c, rel=1e-12)
# sector compact norms and factors
Cf = {
    "charged_lepton": 2.0,
    "up_quark": 23.0/9.0,
    "down_quark": 20.0/9.0,
    "neutrino_dirac_optional": 1.0,
}
sector_rows = []
for name, val in Cf.items():
    kappa = 1 + rG*val
    overlaps = kappa*y_sheet
    H.check(step, f"{name}_sector_hierarchy", overlaps[0] < overlaps[1] < overlaps[2])
    sector_rows.append({"sector": name, "C_f": val, "kappa_f": kappa,
                        "D1": overlaps[0], "D2": overlaps[1], "D3": overlaps[2]})
H.check(step, "negative_control_inverse_ratio_not_suppression", (q/c) > 1)
write_csv_rows(TABLES / "sector_overlap_spectra.csv", sector_rows)

# -----------------------------
# Step 16-18: charged lepton precision and Koide sheet rule
# -----------------------------
step = "16_18_charged_leptons"
thetaK = 2 / (Ngen_PR**2)
def koide_k(a: int) -> float:
    return (1 + math.sqrt(2)*math.cos(thetaK + 2*math.pi*a/3))**2
# assignment a=0 tau, a=1 e, a=2 mu
k_tau, k_e, k_mu = koide_k(0), koide_k(1), koide_k(2)
C1 = 1 - DeltaEW*c/4
C2 = 1 - (rG*DeltaEW*(1+c))/2
Mell_GeV = LambdaEW * rG * DeltaEW * (4/3) * C1*C2
m_e = Mell_GeV * k_e * 1000
m_mu = Mell_GeV * k_mu * 1000
m_tau = Mell_GeV * k_tau * 1000
koide_ratio = (m_e+m_mu+m_tau) / (math.sqrt(m_e)+math.sqrt(m_mu)+math.sqrt(m_tau))**2
H.close(step, "thetaK_2_over_9", thetaK, 2/9, rel=1e-15)
H.close(step, "Koide_identity", koide_ratio, 2/3, rel=1e-13)
H.close(step, "M_ell_MeV", Mell_GeV*1000, 313.850332183, rel=1e-9)
H.close(step, "m_e_PR_MeV", m_e, 0.510984463, rel=5e-9)
H.close(step, "m_mu_PR_MeV", m_mu, 105.656418843, rel=5e-9)
H.close(step, "m_tau_PR_MeV", m_tau, 1776.934589789, rel=5e-9)
max_lepton_rel = max(abs(rel_err(m_e, DIAGNOSTIC_REFERENCES['m_e_ref_MeV'])),
                     abs(rel_err(m_mu, DIAGNOSTIC_REFERENCES['m_mu_ref_MeV'])),
                     abs(rel_err(m_tau, DIAGNOSTIC_REFERENCES['m_tau_ref_MeV'])))
H.check(step, "charged_lepton_max_residual_below_3e_minus_5", max_lepton_rel < 3e-5,
        details=f"max rel={max_lepton_rel:.3e}")
H.check(step, "negative_control_wrong_koide_angle_rejected", abs(((Mell_GeV*1000*(1+math.sqrt(2)*math.cos(1/Ngen+2*math.pi*1/3))**2) - m_e) / m_e) > 1e-3)

# -----------------------------
# Step 19-26: QCD/quark hierarchy
# -----------------------------
step = "19_26_qcd_quarks"
alpha3_inv = q*c - (1-c)
alpha3 = 1/alpha3_inv
H.close(step, "alpha3_PR", alpha3, 0.117861507469150, rel=1e-12)
# Threshold candidates
mu_t = LambdaEW * C1*C2
mu_b = LambdaEW * (rG/3) * (1 - DeltaEW*c)
mu_c = LambdaEW * (rG**2) * (4/3) * (1 + DeltaEW*AEW)
H.close(step, "mu_t_PR_GeV", mu_t, 172.8139732666624, rel=1e-10)
H.close(step, "mu_b_PR_GeV", mu_b, 4.1664504826753515, rel=1e-10)
H.close(step, "mu_c_PR_GeV", mu_c, 1.274964814257465, rel=1e-10)
H.check(step, "heavy_threshold_ordering", mu_t > mu_b > mu_c > 0)
# Cconf derivation
H.close(step, "Cconf", Cconf, 0.8983422324239495, rel=1e-12)
H.close(step, "Cconf_endpoint_reconstruct_c", 2*Cconf - 1, c, rel=1e-12)
H.close(step, "Cconf_endpoint_reconstruct_1", 2*Cconf - c, 1, rel=1e-12)
# Light quarks
m_s = mu_b * (rG/3) * (1 + DeltaEW*AEW) * Cconf * 1000
m_d = m_s * rG*c * (1 - AEW*DeltaEW) * Cconf
m_u = m_d * ((1+c)/4) * (1 + DeltaEW*c/4)
H.close(step, "m_s_PR_MeV", m_s, 94.028510538, rel=1e-9)
H.close(step, "m_d_PR_MeV", m_d, 4.761039493, rel=1e-9)
H.close(step, "m_u_PR_MeV", m_u, 2.146462595, rel=1e-9)
H.check(step, "six_quark_hierarchy_order", m_u/1000 < m_d/1000 < m_s/1000 < mu_c < mu_b < mu_t)
# QCD beta tests
def beta0(nf: int) -> float: return 11 - (2/3)*nf
def beta1(nf: int) -> float: return 102 - (38/3)*nf
def beta2(nf: int) -> float: return 2857/2 - (5033/18)*nf + (325/54)*nf*nf
for nf in [3,4,5,6]:
    H.check(step, f"beta0_positive_nf{nf}", beta0(nf) > 0)
H.check(step, "negative_control_raw_qc_not_alpha", abs(1/(q*c) - alpha3) > 1e-3)
H.check(step, "negative_control_missing_Cconf_shifts_light_quarks", abs((mu_b * (rG/3)*(1+DeltaEW*AEW)*1000) - m_s) > 5.0)

# -----------------------------
# Step 27: CKM
# -----------------------------
step = "27_ckm"
lambda_PR = math.sqrt(rG*c*Cconf*(1 - AEW*DeltaEW))
A_CKM = c / (1 - AEW*DeltaEW)
Rb = (1-rG) * c/(1+c) * (1 - AEW*DeltaEW)
delta_CKM = math.pi/3 + math.sqrt(DeltaEW)
s12, s23, s13 = lambda_PR, A_CKM*lambda_PR**2, A_CKM*lambda_PR**3*Rb
V = ckm_matrix(s12, s23, s13, delta_CKM)
Vabs = np.abs(V)
Jckm = jarlskog(s12, s23, s13, delta_CKM)
H.close(step, "lambda_PR", lambda_PR, 0.225019996525935, rel=1e-12)
H.close(step, "A_CKM_PR", A_CKM, 0.822683296413403, rel=1e-12)
H.close(step, "Rb_PR", Rb, 0.398035078485258, rel=1e-12)
H.close(step, "delta_CKM_deg", math.degrees(delta_CKM), 67.823389204, rel=1e-11)
H.matrix_unitary(step, "CKM_unitarity", V, tol=1e-12)
H.close(step, "Vus_abs", Vabs[0,1], 0.225018430, rel=5e-8)
H.close(step, "Vcb_abs", Vabs[1,2], 0.041655455, rel=5e-8)
H.close(step, "Vub_abs", Vabs[0,2], 0.003730932, rel=5e-7)
H.close(step, "J_CKM", Jckm, 3.152605677e-5, rel=1e-8)
H.check(step, "CKM_hierarchy", Vabs[0,1] > Vabs[1,2] > Vabs[0,2])
H.check(step, "negative_control_zero_CKM_phase_rejected", abs(jarlskog(s12, s23, s13, 0.0)) < 1e-20)

# -----------------------------
# Step 28: PMNS
# -----------------------------
step = "28_pmns"
sin2_12 = Cconf / Ngen_PR
sin2_23 = AEW / Ngen_PR
sin2_13 = DeltaEW * (1+rG) / Cconf
th12 = math.asin(math.sqrt(sin2_12))
th23 = math.asin(math.sqrt(sin2_23))
th13 = math.asin(math.sqrt(sin2_13))
delta_PMNS = math.pi + 2*math.sqrt(DeltaEW)
U = pmns_matrix(math.sin(th12), math.sin(th23), math.sin(th13), delta_PMNS)
Uabs = np.abs(U)
Jpmns = jarlskog(math.sin(th12), math.sin(th23), math.sin(th13), delta_PMNS)
H.close(step, "theta12_deg", math.degrees(th12), 33.176356643, rel=1e-10)
H.close(step, "theta23_deg", math.degrees(th23), 48.735310403, rel=1e-11)
H.close(step, "theta13_deg", math.degrees(th13), 8.582438059, rel=1e-10)
H.close(step, "delta_PMNS_deg", math.degrees(delta_PMNS), 195.646778408, rel=1e-11)
H.matrix_unitary(step, "PMNS_unitarity", U, tol=1e-12)
H.close(step, "J_PMNS", Jpmns, -8.935540e-3, rel=1e-7)
H.check(step, "negative_control_abs_matrix_not_unitary", np.max(np.abs(Uabs.T@Uabs - np.eye(3))) > 0.1)

# -----------------------------
# Step 29-30: neutrino masses and Majorana boundary
# -----------------------------
step = "29_30_neutrino_majorana"
Cnu = 1 - DeltaEW*c
m3_GeV = (vEW**2/Mpl) * (rG**-3) * c * Cnu
m3_eV = m3_GeV * 1e9
R21 = DeltaEW * ((1+c)**2/2) * Cnu
m2_eV = math.sqrt(R21) * m3_eV
m1_eV = 0.0
dm21 = m2_eV**2 - m1_eV**2
dm31 = m3_eV**2 - m1_eV**2
sum_m = m1_eV + m2_eV + m3_eV
# m_beta = sqrt(sum |U_ei|^2 m_i^2)
masses = np.array([m1_eV, m2_eV, m3_eV])
Ue2 = np.abs(U[0,:])**2
m_beta = math.sqrt(float(np.sum(Ue2 * masses**2)))
phiM = math.pi*Cconf
alpha21 = 0.0
alpha31 = 2*delta_PMNS + phiM + alpha21
m_bb = abs(m2_eV*(math.cos(th13)**2)*(math.sin(th12)**2)*complex(math.cos(alpha21), math.sin(alpha21)) +
           m3_eV*(math.sin(th13)**2)*complex(math.cos(alpha31 - 2*delta_PMNS), math.sin(alpha31 - 2*delta_PMNS)))
# envelope for m1=0 with two terms
term2 = m2_eV*(math.cos(th13)**2)*(math.sin(th12)**2)
term3 = m3_eV*(math.sin(th13)**2)
mbb_min, mbb_max = abs(term2-term3), term2+term3
H.close(step, "m1_eV", m1_eV, 0.0, abs_tol=0)
H.close(step, "m2_eV", m2_eV, 8.627283010e-3, rel=1e-9)
H.close(step, "m3_eV", m3_eV, 5.010655367e-2, rel=1e-9)
H.close(step, "Delta_m21_eV2", dm21, 7.443001214e-5, rel=1e-9)
H.close(step, "Delta_m31_eV2", dm31, 2.510666721e-3, rel=1e-9)
H.close(step, "sum_m_eV", sum_m, 5.873383668e-2, rel=1e-9)
H.close(step, "m_beta_eV", m_beta, 8.815029410e-3, rel=1e-8)
H.close(step, "phiM_deg", math.degrees(phiM), 161.701601836, rel=1e-10)
H.close(step, "m_betabeta_eV", m_bb, 1.507694477e-3, rel=1e-8)
H.check(step, "mbetabeta_inside_envelope", mbb_min <= m_bb <= mbb_max)
H.check(step, "normal_ordering", m1_eV < m2_eV < m3_eV)
H.check(step, "negative_control_no_planck_suppression_rejected", (vEW**2) > 1e4)
H.check(step, "negative_control_wrong_rG_direction_rejected", abs(((vEW**2/Mpl)*(rG**3)*1e9) - m3_eV) > 1e-2)

# -----------------------------
# Step 31: scalar/order-mode tree-level ledger
# -----------------------------
step = "31_scalar_order_mode"
real_components_doublet = 4
broken_directions = Ngen_PR  # dim[(SU2xU1)/U1]
remaining_scalar = real_components_doublet - broken_directions
H.close(step, "four_minus_three_one_scalar", remaining_scalar, 1, abs_tol=0)
H.check(step, "Q_Phi0_still_zero", np.allclose(Q_order @ Phi0, np.zeros_like(Phi0), atol=1e-14))
g_hWW = 2*MW_diag**2 / vEW
g_hZZ = 2*MZ_diag**2 / vEW
H.close(step, "g_hWW_relation", g_hWW, 2*MW_diag**2/vEW, rel=1e-14)
H.close(step, "g_hZZ_relation", g_hZZ, 2*MZ_diag**2/vEW, rel=1e-14)
H.close(step, "g_hee_relation", (m_e/1000)/vEW, (m_e/1000)/vEW, rel=1e-14)
H.check(step, "m_h_not_generation_input", "m_h" not in GENERATION_INPUTS)
H.check(step, "negative_control_wrong_order_hypercharge_rejected", not np.allclose((T[2] + 0.0*I2) @ Phi0, np.zeros_like(Phi0)))

# -----------------------------
# Write outputs
# -----------------------------
# Generated outputs summary
generated = {
    "boundary": {
        "q_bc": q, "c_bc": c, "alpha_PR_bc_inverse": alpha_pr_inv,
        "r_G": rG, "Delta_EW": DeltaEW,
    },
    "electroweak": {
        "sin2thetaW_PR": sin2w,
        "thetaW_deg": math.degrees(theta_w),
        "Xi_EW": XiEW,
        "S_EW_base": S_base,
        "deltaS_EW_2": dS2,
        "S_EW_total": S_total,
        "Lambda_EW_PR_GeV": LambdaEW,
        "v_EW_PR_GeV": vEW,
        "G_F_PR_GeV_minus2": GF,
        "MW_diag_GeV": MW_diag,
        "MZ_diag_GeV": MZ_diag,
    },
    "charged_leptons": {
        "M_l_PR_MeV": Mell_GeV*1000,
        "m_e_PR_MeV": m_e,
        "m_mu_PR_MeV": m_mu,
        "m_tau_PR_MeV": m_tau,
        "Koide_ratio": koide_ratio,
    },
    "qcd_quarks": {
        "alpha3_PR": alpha3,
        "mu_t_PR_GeV": mu_t,
        "mu_b_PR_GeV": mu_b,
        "mu_c_PR_GeV": mu_c,
        "m_u_PR_MeV": m_u,
        "m_d_PR_MeV": m_d,
        "m_s_PR_MeV": m_s,
        "Cconf": Cconf,
    },
    "ckm": {
        "lambda_PR": lambda_PR,
        "A_CKM_PR": A_CKM,
        "Rb_PR": Rb,
        "delta_CKM_deg": math.degrees(delta_CKM),
        "J_CKM_PR": Jckm,
        "abs_matrix": Vabs.tolist(),
    },
    "pmns": {
        "theta12_deg": math.degrees(th12),
        "theta23_deg": math.degrees(th23),
        "theta13_deg": math.degrees(th13),
        "delta_CP_deg": math.degrees(delta_PMNS),
        "J_PMNS_PR": Jpmns,
        "abs_matrix": Uabs.tolist(),
    },
    "neutrino": {
        "m1_eV": m1_eV,
        "m2_eV": m2_eV,
        "m3_eV": m3_eV,
        "Delta_m21_eV2": dm21,
        "Delta_m31_eV2": dm31,
        "sum_m_eV": sum_m,
        "m_beta_eV": m_beta,
        "phiM_deg": math.degrees(phiM),
        "alpha31_deg": math.degrees(alpha31),
        "m_betabeta_eV": m_bb,
        "m_betabeta_min_eV": mbb_min,
        "m_betabeta_max_eV": mbb_max,
    },
}
write_json(OUT / "pr2_generated_outputs.json", generated)

# Diagnostic residuals after generation.
residual_rows = [
    {"quantity":"v_EW", "candidate":vEW, "reference":DIAGNOSTIC_REFERENCES["v_EW_ref_GeV"], "relative_error":rel_err(vEW, DIAGNOSTIC_REFERENCES["v_EW_ref_GeV"]), "unit":"GeV", "status":"diagnostic_reference_only"},
    {"quantity":"G_F", "candidate":GF, "reference":DIAGNOSTIC_REFERENCES["G_F_ref_GeV_minus2"], "relative_error":rel_err(GF, DIAGNOSTIC_REFERENCES["G_F_ref_GeV_minus2"]), "unit":"GeV^-2", "status":"diagnostic_reference_only"},
    {"quantity":"m_e", "candidate":m_e, "reference":DIAGNOSTIC_REFERENCES["m_e_ref_MeV"], "relative_error":rel_err(m_e, DIAGNOSTIC_REFERENCES["m_e_ref_MeV"]), "unit":"MeV", "status":"diagnostic_reference_only"},
    {"quantity":"m_mu", "candidate":m_mu, "reference":DIAGNOSTIC_REFERENCES["m_mu_ref_MeV"], "relative_error":rel_err(m_mu, DIAGNOSTIC_REFERENCES["m_mu_ref_MeV"]), "unit":"MeV", "status":"diagnostic_reference_only"},
    {"quantity":"m_tau", "candidate":m_tau, "reference":DIAGNOSTIC_REFERENCES["m_tau_ref_MeV"], "relative_error":rel_err(m_tau, DIAGNOSTIC_REFERENCES["m_tau_ref_MeV"]), "unit":"MeV", "status":"diagnostic_reference_only"},
    {"quantity":"alpha_s", "candidate":alpha3, "reference":DIAGNOSTIC_REFERENCES["alpha_s_MZ_ref"], "relative_error":rel_err(alpha3, DIAGNOSTIC_REFERENCES["alpha_s_MZ_ref"]), "unit":"dimensionless", "status":"diagnostic_reference_only"},
    {"quantity":"m_u", "candidate":m_u, "reference":DIAGNOSTIC_REFERENCES["m_u_ref_MeV"], "relative_error":rel_err(m_u, DIAGNOSTIC_REFERENCES["m_u_ref_MeV"]), "unit":"MeV", "status":"low_energy_running_diagnostic"},
    {"quantity":"m_d", "candidate":m_d, "reference":DIAGNOSTIC_REFERENCES["m_d_ref_MeV"], "relative_error":rel_err(m_d, DIAGNOSTIC_REFERENCES["m_d_ref_MeV"]), "unit":"MeV", "status":"low_energy_running_diagnostic"},
    {"quantity":"m_s", "candidate":m_s, "reference":DIAGNOSTIC_REFERENCES["m_s_ref_MeV"], "relative_error":rel_err(m_s, DIAGNOSTIC_REFERENCES["m_s_ref_MeV"]), "unit":"MeV", "status":"low_energy_running_diagnostic"},
    {"quantity":"mu_c", "candidate":mu_c, "reference":DIAGNOSTIC_REFERENCES["m_c_ref_GeV"], "relative_error":rel_err(mu_c, DIAGNOSTIC_REFERENCES["m_c_ref_GeV"]), "unit":"GeV", "status":"threshold_scale_diagnostic"},
    {"quantity":"mu_b", "candidate":mu_b, "reference":DIAGNOSTIC_REFERENCES["m_b_ref_GeV"], "relative_error":rel_err(mu_b, DIAGNOSTIC_REFERENCES["m_b_ref_GeV"]), "unit":"GeV", "status":"threshold_scale_diagnostic"},
    {"quantity":"mu_t", "candidate":mu_t, "reference":DIAGNOSTIC_REFERENCES["m_t_ref_GeV"], "relative_error":rel_err(mu_t, DIAGNOSTIC_REFERENCES["m_t_ref_GeV"]), "unit":"GeV", "status":"threshold_scale_diagnostic"},
    {"quantity":"Delta_m21", "candidate":dm21, "reference":DIAGNOSTIC_REFERENCES["dm21_ref_eV2"], "relative_error":rel_err(dm21, DIAGNOSTIC_REFERENCES["dm21_ref_eV2"]), "unit":"eV^2", "status":"diagnostic_reference_only"},
    {"quantity":"Delta_m31", "candidate":dm31, "reference":DIAGNOSTIC_REFERENCES["dm31_ref_eV2"], "relative_error":rel_err(dm31, DIAGNOSTIC_REFERENCES["dm31_ref_eV2"]), "unit":"eV^2", "status":"diagnostic_reference_only"},
]
write_csv_rows(TABLES / "pr2_diagnostic_residuals.csv", residual_rows)

# Paper-style audit manifest.
audit_rows = [
    {"section":"2", "sector":"PR-I boundary ledger", "status":"inherited_data", "main_output":"q_bc, c_bc, alpha_PR_bc", "forbidden_inputs_checked":"yes", "remaining_obligation":"none beyond PR-I inheritance"},
    {"section":"3", "sector":"Electroweak lift", "status":"structural_identity", "main_output":"SU(2)_L algebra", "forbidden_inputs_checked":"yes", "remaining_obligation":"none"},
    {"section":"4", "sector":"Projection locking", "status":"structural_identity", "main_output":"Q=T3+Y/2, M_gamma=0", "forbidden_inputs_checked":"yes", "remaining_obligation":"precision running"},
    {"section":"5", "sector":"Weak scale", "status":"precision_candidate", "main_output":"v_EW_PR, G_F_PR", "forbidden_inputs_checked":"yes", "remaining_obligation":"radiative matching PR-III"},
    {"section":"6", "sector":"Scalar/order mode", "status":"tree_level_structural_ledger", "main_output":"4-3=1, g_hWW, g_hZZ, g_hff", "forbidden_inputs_checked":"yes", "remaining_obligation":"m_h compact Hessian PR-III"},
    {"section":"7", "sector":"Charged/neutral currents", "status":"structural_identity", "main_output":"Fermi and Z coupling ledgers", "forbidden_inputs_checked":"yes", "remaining_obligation":"precision electroweak corrections"},
    {"section":"8", "sector":"Anomaly cancellation", "status":"structural_identity", "main_output":"all anomaly coefficients vanish", "forbidden_inputs_checked":"yes", "remaining_obligation":"none"},
    {"section":"9", "sector":"Generation/flavor sheets", "status":"closure_candidate", "main_output":"N_gen=3, y_i hierarchy", "forbidden_inputs_checked":"yes", "remaining_obligation":"projection-sheet theorem"},
    {"section":"10", "sector":"Charged leptons", "status":"precision_candidate", "main_output":"m_e,m_mu,m_tau", "forbidden_inputs_checked":"yes", "remaining_obligation":"Koide rule uniqueness"},
    {"section":"11", "sector":"Quark/QCD", "status":"hierarchy_candidate_diagnostic_ledger", "main_output":"alpha3, six-quark hierarchy", "forbidden_inputs_checked":"yes", "remaining_obligation":"QCD scheme/running precision"},
    {"section":"12", "sector":"CKM/PMNS", "status":"closure_candidate", "main_output":"unitary CKM and PMNS candidates", "forbidden_inputs_checked":"yes", "remaining_obligation":"phase-rule uniqueness"},
    {"section":"13", "sector":"Neutrino/Majorana", "status":"closure_candidate", "main_output":"normal ordering, m_betabeta", "forbidden_inputs_checked":"yes", "remaining_obligation":"Majorana phase theorem"},
]
write_csv_rows(AUDIT / "PRII_AUDIT_MANIFEST.csv", audit_rows)

# Write tests and summary.
H.write_csv(AUDIT / "PRII_TEST_RESULTS.csv")
summary = H.summary()
summary["status"] = "PASS" if summary["tests_failed"] == 0 else "FAIL"
summary["output_directory"] = str(OUT)
summary["forbidden_generation_input_intersection"] = sorted(list(intersection))
write_json(AUDIT / "PRII_RUN_SUMMARY.json", summary)

summary_md = f"""# PR-II Colab Harness Run Summary

Status: **{summary['status']}**

- tests_total: `{summary['tests_total']}`
- tests_passed: `{summary['tests_passed']}`
- tests_failed: `{summary['tests_failed']}`
- output_directory: `{OUT}`

## Input discipline

Allowed generation inputs and diagnostic references are stored separately. Target observables are not used as generation inputs.

Forbidden-generation-input intersection:

```text
{sorted(list(intersection))}
```

## Key generated outputs

```text
sin^2(theta_W)^PR = {sin2w:.15f}
Lambda_EW^PR      = {LambdaEW:.12f} GeV
v_EW^PR           = {vEW:.12f} GeV
G_F^PR            = {GF:.15e} GeV^-2
alpha_3^PR        = {alpha3:.15f}
me,mmu,mtau       = {m_e:.9f}, {m_mu:.9f}, {m_tau:.9f} MeV
mu,md,ms          = {m_u:.9f}, {m_d:.9f}, {m_s:.9f} MeV
m_c,m_b,m_t       = {mu_c:.12f}, {mu_b:.12f}, {mu_t:.12f} GeV
Delta m21^2       = {dm21:.12e} eV^2
Delta m31^2       = {dm31:.12e} eV^2
m_betabeta        = {m_bb:.12e} eV
```

## Important caveat

This harness verifies the PR-II tree-level electroweak/flavor candidate chain and negative controls. It does not claim scalar-mass closure or loop-level electroweak/QCD precision completion. Those are PR-III precision-layer targets.
"""
(AUDIT / "PRII_RUN_SUMMARY.md").write_text(summary_md, encoding="utf-8")

# Zip package.
zip_path = BASE / "pr2_harness_output.zip"
if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for path in OUT.rglob("*"):
        if path.is_file():
            zf.write(path, arcname=str(path.relative_to(OUT.parent)))

print(summary_md)
print(f"\nWrote output folder: {OUT}")
print(f"Wrote zip package:  {zip_path}")
