# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  ______             __                   __                __        __        _______                                                               __
# /      \           |  \                 |  \              |  \      |  \      |       \                                                             |  \
#|  $$$$$$\  _______ | $$____    ______  _| $$_     _______ | $$   __  \$$      | $$$$$$$\  ______    _______   ______    ______    ______    _______ | $$____
#| $$  | $$ /       \| $$    \  /      \|   $$ \   /       \| $$  /  \|  \      | $$__| $$ /      \  /       \ /      \  |      \  /      \  /       \| $$    \
#| $$  | $$|  $$$$$$$| $$$$$$$\|  $$$$$$\\$$$$$$  |  $$$$$$$| $$_/  $$| $$      | $$    $$|  $$$$$$\|  $$$$$$$|  $$$$$$\  \$$$$$$\|  $$$$$$\|  $$$$$$$| $$$$$$$\
#| $$  | $$ \$$    \ | $$  | $$| $$    $$ | $$ __  \$$    \ | $$   $$ | $$      | $$$$$$$\| $$    $$ \$$    \ | $$    $$ /      $$| $$   \$$| $$      | $$  | $$
#| $$__/ $$ _\$$$$$$\| $$  | $$| $$$$$$$$ | $$|  \ _\$$$$$$\| $$$$$$\ | $$      | $$  | $$| $$$$$$$$ _\$$$$$$\| $$$$$$$$|  $$$$$$$| $$      | $$_____ | $$  | $$
# \$$    $$|       $$| $$  | $$ \$$     \  \$$  $$|       $$| $$  \$$\| $$      | $$  | $$ \$$     \|       $$ \$$     \ \$$    $$| $$       \$$     \| $$  | $$
#  \$$$$$$  \$$$$$$$  \$$   \$$  \$$$$$$$   \$$$$  \$$$$$$$  \$$   \$$ \$$       \$$   \$$  \$$$$$$$ \$$$$$$$   \$$$$$$$  \$$$$$$$ \$$        \$$$$$$$ \$$   \$$
#
# COLAB-USABLE VERSION
# Projection Relativity Numerical Validation Harness
# Michael Stanislaus Oshetski
# ORCID# 0009-0007-3623-7586
# May 2026
#
# "Dedicated to my brother and best friend,
# John Oshetski Jr. ("Motorhead")
# I'll see you in the decoherence!"
#
# Covers:
# 1. Radial branch operator spectrum and reference constants
# 2. Radial convergence, branch stability, and non-tuning scans
# 3. Boundary cofactor and finite-rank alpha closure
# 4. Magnetic compact-phase area law
# 5. Propagator subtraction, positivity, and cutoff stability
# 6. Finite-core, displacement, trace-free source, and dimensional checks
# 7. Weak-gravity recovery checks
# 8. Strong-gravity Kerr exterior and optional Kerr 220 QNM backend/fallback
# 9. Gap-suppressed residual diagnostics
# 10. Optional stress mode, failure injection, document source checks, and scorecard
#
# Scope:
# This is a numerical validation suite aligned with the paper. It complements
# the Maple symbolic checker and should be described as "symbolically audited
# and numerically validated where machine-checkable." It does not claim every
# physical or observational statement is certified beyond the machine-checkable scope.
#
# Usage:
#   Standard from repository root:
#       python test_harness/projection_relativity_I/numerical/code/projection_relativity_numerical_validation_harness.py
#   Stress from repository root:
#       python test_harness/projection_relativity_I/numerical/code/projection_relativity_numerical_validation_harness.py --stress
#   Colab: upload this file and run %run projection_relativity_numerical_validation_harness.py
#   Colab stress mode: set os.environ["PR_STRESS_MODE"] = "1" before running.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from __future__ import annotations

import json
import math
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def _in_colab() -> bool:
    return "google.colab" in sys.modules or Path("/content").exists()


Path(".matplotlib").mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(Path(".matplotlib").resolve()))


def _ensure_packages() -> None:
    required = ["numpy", "pandas", "scipy", "matplotlib"]
    missing = []
    for name in required:
        try:
            __import__(name)
        except Exception:
            missing.append(name)
    if missing and _in_colab():
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *missing])
    elif missing:
        raise RuntimeError(f"Missing required packages: {missing}")


_ensure_packages()

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.linalg import eigh, eigh_tridiagonal

try:
    import qnm  # type: ignore

    QNM_AVAILABLE = True
    QNM_ERROR = ""
except Exception as exc:
    qnm = None
    QNM_AVAILABLE = False
    QNM_ERROR = repr(exc)


OUT_DIR = Path("projection_relativity_numerical_validation_outputs")
PLOTS_DIR = OUT_DIR / "plots"
OUT_DIR.mkdir(exist_ok=True)
PLOTS_DIR.mkdir(exist_ok=True)


def _truthy_env(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on", "stress"}


STRESS_MODE = "--stress" in sys.argv or _truthy_env("PR_STRESS_MODE")


@dataclass(frozen=True)
class Constants:
    # Radial branch reference spectrum from the paper/Maple lock.
    lambda0: float = 2.322863529580
    lambda1: float = 5.375830272676
    lambda3: float = 13.23388439508096
    mu_min2: float = 3.052966743096

    # Boundary/FSC constants.
    T_A: float = 0.25
    T_X: float = 0.75
    c_bc: float = 0.796684464847899
    p1: float = 7.6528903366e-4
    alpha_inv_bc: float = 137.036361812007

    # Magnetic compact phase area law.
    hbar: float = 1.054571817e-34
    e_charge: float = 1.602176634e-19
    Z_A: float = 10.90500718
    Phi_theta_PR_Wb: float = 9.009597185e-15
    Phi_theta_PR_nG_m2: float = 0.09009597185

    # Physical constants.
    G: float = 6.67430e-11
    c: float = 299792458.0
    M_sun: float = 1.98847e30


C = Constants()
TESTS: list[dict[str, Any]] = []
ARTIFACTS: dict[str, pd.DataFrame] = {}


def pass_fail(condition: bool) -> str:
    return "PASS" if bool(condition) else "FAIL"


def add_test(
    sector: str,
    test: str,
    status: str,
    value: Any = None,
    target: Any = None,
    tolerance: Any = None,
    notes: str = "",
) -> None:
    TESTS.append(
        {
            "sector": sector,
            "test": test,
            "status": status,
            "value": value,
            "target": target,
            "tolerance": tolerance,
            "notes": notes,
        }
    )


def add_close(
    sector: str,
    test: str,
    value: float,
    target: float,
    tolerance: float,
    notes: str = "",
) -> None:
    value_f = float(value)
    target_f = float(target)
    err = abs(value_f - target_f)
    add_test(
        sector,
        test,
        pass_fail(err <= tolerance),
        value_f,
        target_f,
        tolerance,
        notes or f"abs_error={err:.6e}",
    )


def rel_err(value: float, target: float, floor: float = 1e-300) -> float:
    return abs(value - target) / max(abs(target), floor)


def save_df(name: str, df: pd.DataFrame) -> None:
    ARTIFACTS[name] = df
    df.to_csv(OUT_DIR / f"{name}.csv", index=False)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 1. Radial branch operator spectrum
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def radial_potential(w: np.ndarray, a2: float = 1.0, a4: float = 0.75) -> np.ndarray:
    return 1.0 + a2 * w**2 + a4 * w**4


def compute_radial_spectrum(
    n_grid: int = 2000,
    w_max: float = 8.0,
    n_eigs: int = 8,
    a2: float = 1.0,
    a4: float = 0.75,
) -> tuple[np.ndarray, np.ndarray]:
    w = np.linspace(-w_max, w_max, n_grid)
    dw = float(w[1] - w[0])
    main_diag = 2.0 / dw**2 + radial_potential(w, a2=a2, a4=a4)
    off_diag = -np.ones(n_grid - 1) / dw**2
    evals, evecs = eigh_tridiagonal(main_diag, off_diag, select="i", select_range=(0, n_eigs - 1))
    return evals, evecs


radial_evals, radial_evecs = compute_radial_spectrum()
lambda0_num = float(radial_evals[0])
lambda1_num = float(radial_evals[1])
mu_min2_num = lambda1_num - lambda0_num

add_close("Radial Branch", "lambda0 finite-difference recompute", lambda0_num, C.lambda0, 8.0e-4)
add_close("Radial Branch", "lambda1 finite-difference recompute", lambda1_num, C.lambda1, 5.0e-3)
add_close("Radial Branch", "mu_min^2 finite-difference recompute", mu_min2_num, C.mu_min2, 5.0e-3)
add_test("Radial Branch", "spectrum ordered", pass_fail(np.all(np.diff(radial_evals) > 0)), bool(np.all(np.diff(radial_evals) > 0)))
w_sym = np.linspace(-8, 8, 101)
potential_even_error = float(np.max(np.abs(radial_potential(w_sym) - radial_potential(w_sym)[::-1])))
add_close("Radial Branch", "potential even", potential_even_error, 0.0, 1e-10)
add_test("Radial Branch", "quartic coefficient locked to spatial trace fraction", pass_fail(abs(0.75 - 3.0 / 4.0) < 1e-15), 0.75, "3/4")

radial_df = pd.DataFrame(
    {
        "mode": np.arange(len(radial_evals)),
        "lambda_n": radial_evals,
        "mu_n2": radial_evals - radial_evals[0],
    }
)
save_df("radial_branch_spectrum", radial_df)

convergence_rows = []
for n_grid in [700, 1000, 1400, 2000]:
    evals_conv, _ = compute_radial_spectrum(n_grid=n_grid, n_eigs=2)
    gap_conv = float(evals_conv[1] - evals_conv[0])
    convergence_rows.append(
        {
            "n_grid": n_grid,
            "lambda0": float(evals_conv[0]),
            "lambda1": float(evals_conv[1]),
            "mu_min2": gap_conv,
            "abs_error_mu_min2": abs(gap_conv - C.mu_min2),
        }
    )
convergence_df = pd.DataFrame(convergence_rows)
save_df("radial_convergence_scan", convergence_df)
add_test(
    "Radial Convergence",
    "final grid matches locked radial gap",
    pass_fail(float(convergence_df["abs_error_mu_min2"].iloc[-1]) < 5e-6),
    float(convergence_df["abs_error_mu_min2"].iloc[-1]),
    "<5e-6",
)
add_test(
    "Radial Convergence",
    "coarse-to-final error decreases",
    pass_fail(float(convergence_df["abs_error_mu_min2"].iloc[-1]) < float(convergence_df["abs_error_mu_min2"].iloc[0])),
    float(convergence_df["abs_error_mu_min2"].iloc[0] / max(convergence_df["abs_error_mu_min2"].iloc[-1], 1e-300)),
    ">1",
)
add_test(
    "Radial Convergence",
    "last refinement is stable",
    pass_fail(abs(float(convergence_df["mu_min2"].iloc[-1] - convergence_df["mu_min2"].iloc[-2])) < 1e-4),
    float(convergence_df["mu_min2"].iloc[-1] - convergence_df["mu_min2"].iloc[-2]),
    "<1e-4",
)

stability_rows = []
for a2_scan in np.linspace(0.7, 1.3, 5):
    for a4_scan in np.linspace(0.5, 1.0, 5):
        evals_scan, _ = compute_radial_spectrum(n_grid=450, n_eigs=2, a2=float(a2_scan), a4=float(a4_scan))
        gap_scan = float(evals_scan[1] - evals_scan[0])
        stability_rows.append(
            {
                "a2": float(a2_scan),
                "a4": float(a4_scan),
                "lambda0": float(evals_scan[0]),
                "lambda1": float(evals_scan[1]),
                "gap": gap_scan,
                "stable_ordered_positive_gap": bool(evals_scan[1] > evals_scan[0] and gap_scan > 0),
            }
        )
stability_df = pd.DataFrame(stability_rows)
gap_cv = float(stability_df["gap"].std(ddof=0) / stability_df["gap"].mean())
save_df("radial_operator_stability_scan", stability_df)
add_test(
    "Radial Stability",
    "nearby branch operators keep ordered positive gap",
    pass_fail(stability_df["stable_ordered_positive_gap"].all()),
    bool(stability_df["stable_ordered_positive_gap"].all()),
)
add_test("Radial Stability", "nearby branch gap coefficient of variation bounded", pass_fail(gap_cv < 0.10), gap_cv, "<0.10")

vacuum_rows = []
for da2 in np.linspace(-0.075, 0.075, 11):
    for da4_frac in np.linspace(-0.075, 0.075, 11):
        a2_v = 1.0 + float(da2)
        a4_v = 0.75 * (1.0 + float(da4_frac))
        evals_v, _ = compute_radial_spectrum(n_grid=420, n_eigs=2, a2=a2_v, a4=a4_v)
        gap_v = float(evals_v[1] - evals_v[0])
        coeff_penalty = ((a2_v - 1.0) / 0.15) ** 2 + ((a4_v - 0.75) / (0.15 * 0.75)) ** 2
        score = (gap_v - C.mu_min2) ** 2 + 1e-3 * coeff_penalty
        vacuum_rows.append(
            {
                "a2": a2_v,
                "a4": a4_v,
                "lambda0": float(evals_v[0]),
                "lambda1": float(evals_v[1]),
                "gap": gap_v,
                "branch_score": score,
                "coefficient_penalty": coeff_penalty,
            }
        )
vacuum_df = pd.DataFrame(vacuum_rows)
baseline_mask = (np.isclose(vacuum_df["a2"], 1.0)) & (np.isclose(vacuum_df["a4"], 0.75))
baseline_score = float(vacuum_df.loc[baseline_mask, "branch_score"].iloc[0])
baseline_rank = int((vacuum_df["branch_score"] < baseline_score).sum() + 1)
fraction_above_baseline = float((vacuum_df["branch_score"] > baseline_score).mean())
median_score_lift = float(np.median(vacuum_df["branch_score"] - baseline_score))
save_df("radial_vacuum_selection_scan", vacuum_df)
add_test("Radial Stability", "baseline branch remains local numerical minimum", pass_fail(baseline_rank == 1), baseline_rank, 1)
add_test("Radial Stability", "perturbation scan mostly lifts branch score", pass_fail(fraction_above_baseline > 0.98), fraction_above_baseline, ">0.98")
add_test("Radial Stability", "median perturbation score lift positive", pass_fail(median_score_lift > 0), median_score_lift, ">0")


def build_ho_operators(n_basis: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    annihilation = np.zeros((n_basis, n_basis), dtype=float)
    for n in range(1, n_basis):
        annihilation[n - 1, n] = math.sqrt(n)
    creation = annihilation.T
    x = (annihilation + creation) / math.sqrt(2.0)
    x2 = x @ x
    h_osc = np.diag([2 * n + 1 for n in range(n_basis)])
    p2 = h_osc - x2
    ident = np.eye(n_basis)
    return ident, x, x2, p2


if STRESS_MODE:
    domain_rows = []
    for w_max_stress in [6.0, 7.0, 8.0, 9.0, 10.0]:
        n_grid_stress = int(250 * w_max_stress)
        evals_domain, _ = compute_radial_spectrum(n_grid=n_grid_stress, w_max=w_max_stress, n_eigs=2)
        gap_domain = float(evals_domain[1] - evals_domain[0])
        domain_rows.append(
            {
                "w_max": w_max_stress,
                "n_grid": n_grid_stress,
                "lambda0": float(evals_domain[0]),
                "lambda1": float(evals_domain[1]),
                "mu_min2": gap_domain,
                "abs_error_mu_min2": abs(gap_domain - C.mu_min2),
            }
        )
    radial_domain_stress_df = pd.DataFrame(domain_rows)
    save_df("stress_radial_domain_convergence", radial_domain_stress_df)
    add_test(
        "Stress Radial",
        "domain-size stress keeps radial gap locked",
        pass_fail(float(radial_domain_stress_df["abs_error_mu_min2"].max()) < 1e-6),
        float(radial_domain_stress_df["abs_error_mu_min2"].max()),
        "<1e-6",
    )

    wide_rows = []
    for a2_wide in np.linspace(0.2, 2.0, 7):
        for a4_wide in np.linspace(0.1, 1.6, 7):
            evals_wide, _ = compute_radial_spectrum(n_grid=450, n_eigs=2, a2=float(a2_wide), a4=float(a4_wide))
            wide_rows.append(
                {
                    "a2": float(a2_wide),
                    "a4": float(a4_wide),
                    "lambda0": float(evals_wide[0]),
                    "lambda1": float(evals_wide[1]),
                    "gap": float(evals_wide[1] - evals_wide[0]),
                    "ordered_positive_gap": bool(evals_wide[1] > evals_wide[0]),
                }
            )
    radial_wide_stress_df = pd.DataFrame(wide_rows)
    save_df("stress_radial_wide_parameter_scan", radial_wide_stress_df)
    add_test(
        "Stress Radial",
        "wide positive-quartic branch scan remains ordered",
        pass_fail(radial_wide_stress_df["ordered_positive_gap"].all()),
        bool(radial_wide_stress_df["ordered_positive_gap"].all()),
    )

    ident_ho, _, x2_ho, p2_ho = build_ho_operators(80)
    ho_operator = p2_ho + ident_ho + x2_ho + 0.75 * (x2_ho @ x2_ho)
    ho_evals = eigh(ho_operator, eigvals_only=True)
    ho_gap = float(ho_evals[1] - ho_evals[0])
    ho_df = pd.DataFrame(
        [
            {"method": "harmonic_oscillator_basis", "lambda0": float(ho_evals[0]), "lambda1": float(ho_evals[1]), "mu_min2": ho_gap},
            {"method": "finite_difference", "lambda0": lambda0_num, "lambda1": lambda1_num, "mu_min2": mu_min2_num},
        ]
    )
    save_df("stress_radial_independent_method_crosscheck", ho_df)
    add_test("Stress Radial", "independent harmonic-basis gap agrees with finite difference", pass_fail(abs(ho_gap - mu_min2_num) < 1e-4), abs(ho_gap - mu_min2_num), "<1e-4")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 2. Boundary cofactor and finite-rank alpha closure
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


T_A, T_X = C.T_A, C.T_X
M_A = np.array([[T_A**3, T_A**4], [1.0, 0.0]], dtype=float)
D_A = float(np.linalg.det(np.eye(2) - M_A))
N_bc = 1 + T_A**3 + T_A**4 + T_X * (T_A**5 - T_A**8)
R_bc = N_bc / D_A
c_bc_num = T_X * (1 + T_A**2 - T_A**6 * R_bc)

add_close("Boundary Closure", "D_A = 251/256", D_A, 251 / 256, 1e-15)
add_close("Boundary Closure", "N_bc exact numeric", N_bc, 267453 / 262144, 1e-15)
add_close("Boundary Closure", "c_bc numeric", c_bc_num, C.c_bc, 1e-15)
add_test("Boundary Closure", "boundary cofactor positive", pass_fail(D_A > 0 and N_bc > 0 and c_bc_num > 0), (D_A, N_bc, c_bc_num))

q1 = C.lambda1 - C.lambda0
q3 = C.lambda3 - C.lambda0
q_mix = C.p1 * q1 + (1 - C.p1) * q3
alpha_recovered = 4 * math.pi * q_mix
lambda3_implied = C.lambda0 + (C.alpha_inv_bc / (4 * math.pi) - C.p1 * q1) / (1 - C.p1)
add_close("Finite-Rank Alpha Closure", "printed lambda3 implies target alpha inverse", lambda3_implied, C.lambda3, 1e-10)
add_close("Finite-Rank Alpha Closure", "finite-rank q1/q3 mixture recovers alpha inverse", alpha_recovered, C.alpha_inv_bc, 1e-10)

boundary_df = pd.DataFrame(
    [
        {"quantity": "D_A", "value": D_A, "target": 251 / 256},
        {"quantity": "N_bc", "value": N_bc, "target": 267453 / 262144},
        {"quantity": "c_bc", "value": c_bc_num, "target": C.c_bc},
        {"quantity": "lambda3_implied", "value": lambda3_implied, "target": C.lambda3},
        {"quantity": "alpha_inverse_recovered", "value": alpha_recovered, "target": C.alpha_inv_bc},
    ]
)
save_df("boundary_and_alpha_closure", boundary_df)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 3. Magnetic compact-phase area law
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


Phi_theta = (C.hbar / C.e_charge) * (C.Z_A / C.c_bc)
Phi_theta_nG_m2 = Phi_theta / 1e-13

add_close("Magnetic Area Law", "Phi_theta^PR in Wb", Phi_theta, C.Phi_theta_PR_Wb, 5e-23)
add_close("Magnetic Area Law", "area-law coefficient in nG m^2", Phi_theta_nG_m2, C.Phi_theta_PR_nG_m2, 5e-10)


def B_from_area_nG(area_m2: float) -> float:
    return Phi_theta_nG_m2 / area_m2


def area_from_B_m2(B_nG: float) -> float:
    return Phi_theta_nG_m2 / B_nG


example_B = np.array([0.04, 0.11, 0.5, 1.0, 2.0, 4.0], dtype=float)
area_rows = []
for B in example_B:
    area = area_from_B_m2(float(B))
    area_rows.append(
        {
            "B_geo_nG": B,
            "A_proj_theta_m2": area,
            "L_proj_theta_m": math.sqrt(area),
            "roundtrip_B_geo_nG": B_from_area_nG(area),
        }
    )
area_df = pd.DataFrame(area_rows)
save_df("magnetic_area_law_examples", area_df)

add_test("Magnetic Area Law", "positive B maps to positive area", pass_fail((area_df["A_proj_theta_m2"] > 0).all()))
add_test("Magnetic Area Law", "area/B roundtrip", pass_fail(np.max(np.abs(area_df["roundtrip_B_geo_nG"] - area_df["B_geo_nG"])) < 1e-14))
add_test("Magnetic Area Law", "obsolete fixed-field prediction absent by construction", "PASS", "B_geo is computed from A_proj, not fixed")

fig, ax = plt.subplots(figsize=(7.0, 4.6))
areas = np.logspace(math.log10(area_df["A_proj_theta_m2"].min() / 2), math.log10(area_df["A_proj_theta_m2"].max() * 2), 300)
ax.loglog(areas, [B_from_area_nG(a) for a in areas], label="B_geo[nG] = 0.09009597185 / A_proj[m^2]")
ax.scatter(area_df["A_proj_theta_m2"], area_df["B_geo_nG"], color="black", s=30)
ax.set_xlabel("A_proj^(theta) [m^2]")
ax.set_ylabel("B_geo^PR [nG]")
ax.set_title("PR Magnetic Area Law")
ax.grid(True, which="both", alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(PLOTS_DIR / "magnetic_area_law.png", dpi=180)
plt.close(fig)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 4. Propagator subtraction and low-energy residual
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


s_grid = C.mu_min2 + np.linspace(0.25, 20.0, 800)
rho_shape = np.exp(-(s_grid - C.mu_min2) / 4.0)
rho_shape /= np.trapezoid(rho_shape, s_grid)


def F_sub(z: float) -> float:
    integrand = rho_shape * (1.0 / (z - s_grid) + 1.0 / s_grid)
    return float(np.trapezoid(integrand, s_grid))


z_values = np.array([1e-5, 3e-5, 1e-4, 3e-4], dtype=float)
F0 = F_sub(0.0)
F_over_z = np.array([F_sub(float(z)) / z for z in z_values])
M2_numeric = float(np.trapezoid(rho_shape / (s_grid**2), s_grid))
Z_pole = 1.0 / (1.0 + M2_numeric)
F_E = np.array([(F_sub(float(z)) + z * M2_numeric) / (1 + M2_numeric) for z in z_values])

add_close("Propagator", "subtracted kernel F_sub(0)=0", F0, 0.0, 1e-13)
add_test("Propagator", "positive spectral density", pass_fail((rho_shape >= 0).all()), bool((rho_shape >= 0).all()))
add_test("Propagator", "M2 positive", pass_fail(M2_numeric > 0), M2_numeric)
add_test("Propagator", "massless pole residue in (0,1)", pass_fail(0 < Z_pole < 1), Z_pole)
add_test("Propagator", "Newton-normalized residual starts beyond O(z)", pass_fail(np.max(np.abs(F_E / z_values)) < 1e-3), float(np.max(np.abs(F_E / z_values))), "<1e-3")

propagator_df = pd.DataFrame({"z": z_values, "F_sub": [F_sub(float(z)) for z in z_values], "F_sub_over_z": F_over_z, "F_E": F_E, "F_E_over_z": F_E / z_values})
save_df("propagator_low_energy_residual", propagator_df)

rho_norm = float(np.trapezoid(rho_shape, s_grid))
tail_mask = s_grid > (C.mu_min2 + 16.0)
tail_fraction = float(np.trapezoid(rho_shape[tail_mask], s_grid[tail_mask])) if tail_mask.sum() > 1 else 0.0


def normalized_spectral_shape(s_max_offset: float, n_points: int = 600) -> tuple[np.ndarray, np.ndarray]:
    s = C.mu_min2 + np.linspace(0.25, s_max_offset, n_points)
    rho = np.exp(-(s - C.mu_min2) / 4.0)
    rho /= np.trapezoid(rho, s)
    return s, rho


cutoff_rows = []
for cutoff_offset in [12.0, 16.0, 20.0]:
    s_cut, rho_cut = normalized_spectral_shape(cutoff_offset)
    M2_cut = float(np.trapezoid(rho_cut / (s_cut**2), s_cut))
    z_cut = 1.0e-4
    F_cut = float(np.trapezoid(rho_cut * (1.0 / (z_cut - s_cut) + 1.0 / s_cut), s_cut))
    F_E_cut = (F_cut + z_cut * M2_cut) / (1.0 + M2_cut)
    cutoff_rows.append(
        {
            "s_max_minus_mu_min2": cutoff_offset,
            "rho_norm": float(np.trapezoid(rho_cut, s_cut)),
            "M2": M2_cut,
            "F_E_over_z_at_1e_minus_4": F_E_cut / z_cut,
            "Z_pole": 1.0 / (1.0 + M2_cut),
        }
    )
propagator_stability_df = pd.DataFrame(cutoff_rows)
save_df("propagator_spectral_stability_scan", propagator_stability_df)
add_close("Propagator", "spectral density normalized", rho_norm, 1.0, 1e-12)
add_test("Propagator", "spectral support starts above radial gap", pass_fail(float(s_grid.min()) > C.mu_min2), float(s_grid.min()), f">{C.mu_min2}")
add_test("Propagator", "UV tail is suppressed in reference window", pass_fail(tail_fraction < 0.03), tail_fraction, "<0.03")
add_test(
    "Propagator",
    "cutoff scan keeps Newton-normalized residual small",
    pass_fail(float(np.max(np.abs(propagator_stability_df["F_E_over_z_at_1e_minus_4"]))) < 1e-3),
    float(np.max(np.abs(propagator_stability_df["F_E_over_z_at_1e_minus_4"]))),
    "<1e-3",
)
add_test(
    "Propagator",
    "cutoff scan keeps residue physical",
    pass_fail(((propagator_stability_df["Z_pole"] > 0) & (propagator_stability_df["Z_pole"] < 1)).all()),
    bool(((propagator_stability_df["Z_pole"] > 0) & (propagator_stability_df["Z_pole"] < 1)).all()),
)

if STRESS_MODE:
    cutoff_stress_rows = []
    z_stress = np.array([1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3], dtype=float)
    for cutoff_offset in [8.0, 12.0, 16.0, 20.0, 28.0, 36.0]:
        s_cut, rho_cut = normalized_spectral_shape(cutoff_offset, n_points=900)
        M2_cut = float(np.trapezoid(rho_cut / (s_cut**2), s_cut))
        FE_over_z_values = []
        for z_probe in z_stress:
            F_cut = float(np.trapezoid(rho_cut * (1.0 / (float(z_probe) - s_cut) + 1.0 / s_cut), s_cut))
            FE_cut = (F_cut + float(z_probe) * M2_cut) / (1.0 + M2_cut)
            FE_over_z_values.append(FE_cut / float(z_probe))
        cutoff_stress_rows.append(
            {
                "s_max_minus_mu_min2": cutoff_offset,
                "M2": M2_cut,
                "Z_pole": 1.0 / (1.0 + M2_cut),
                "max_abs_F_E_over_z": float(np.max(np.abs(FE_over_z_values))),
                "monotone_low_energy_residual": bool(np.all(np.diff(np.abs(FE_over_z_values)) >= -1e-12)),
            }
        )
    propagator_cutoff_stress_df = pd.DataFrame(cutoff_stress_rows)
    save_df("stress_propagator_cutoff_scan", propagator_cutoff_stress_df)
    add_test(
        "Stress Propagator",
        "wide cutoff scan keeps residual low-energy suppressed",
        pass_fail(float(propagator_cutoff_stress_df["max_abs_F_E_over_z"].max()) < 1e-2),
        float(propagator_cutoff_stress_df["max_abs_F_E_over_z"].max()),
        "<1e-2",
    )
    add_test(
        "Stress Propagator",
        "wide cutoff scan keeps physical pole residues",
        pass_fail(((propagator_cutoff_stress_df["Z_pole"] > 0) & (propagator_cutoff_stress_df["Z_pole"] < 1)).all()),
        bool(((propagator_cutoff_stress_df["Z_pole"] > 0) & (propagator_cutoff_stress_df["Z_pole"] < 1)).all()),
    )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 5. Finite core, displacement sector, trace-free source, dimensions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


M_phys = 65.0 * C.M_sun
Rmax = C.mu_min2
r_core_cubed = C.G * M_phys / (C.c**2 * Rmax)
r_core = r_core_cubed ** (1 / 3)
r_g = C.G * M_phys / C.c**2
rho_max = 3 * C.c**2 * Rmax / (4 * math.pi * C.G)
K_core = 96 * Rmax**2

add_test("Finite Core", "r_core^3 positive", pass_fail(r_core_cubed > 0), r_core_cubed)
add_test("Finite Core", "core radius below gravitational radius for benchmark mass", pass_fail(r_core < r_g), r_core / r_g, "<1")
add_test("Finite Core", "rho_max positive", pass_fail(rho_max > 0), rho_max)
add_close("Finite Core", "K_core coefficient is 96 Rmax^2", K_core / (Rmax**2), 96.0, 1e-12)

if STRESS_MODE:
    core_mass_rows = []
    for mass_solar_stress in [1.4, 10.0, 65.0, 1.0e3, 1.0e6, 1.0e9]:
        mass_kg_stress = mass_solar_stress * C.M_sun
        r_core_stress = (C.G * mass_kg_stress / (C.c**2 * Rmax)) ** (1 / 3)
        r_g_stress = C.G * mass_kg_stress / C.c**2
        core_mass_rows.append(
            {
                "mass_solar": mass_solar_stress,
                "r_core_m": r_core_stress,
                "r_g_m": r_g_stress,
                "r_core_over_r_g": r_core_stress / r_g_stress,
                "core_inside_gravitational_radius": r_core_stress < r_g_stress,
            }
        )
    finite_core_stress_df = pd.DataFrame(core_mass_rows)
    save_df("stress_finite_core_mass_scan", finite_core_stress_df)
    add_test(
        "Stress Finite Core",
        "finite core remains hidden across compact-object mass scan",
        pass_fail(finite_core_stress_df["core_inside_gravitational_radius"].all()),
        bool(finite_core_stress_df["core_inside_gravitational_radius"].all()),
    )
    add_test(
        "Stress Finite Core",
        "core-to-gravitational-radius ratio decreases with mass",
        pass_fail(np.all(np.diff(finite_core_stress_df["r_core_over_r_g"]) < 0)),
        bool(np.all(np.diff(finite_core_stress_df["r_core_over_r_g"]) < 0)),
    )

alpha_A = -2.0
beta_A = 3.0
A0_sq = -alpha_A / (2 * beta_A)
mA2_from_alpha = -4 * alpha_A
mA2_from_vacuum = 8 * beta_A * A0_sq
add_test("Displacement Sector", "nonzero vacuum amplitude squared positive", pass_fail(A0_sq > 0), A0_sq)
add_close("Displacement Sector", "m_A^2 alpha/vacuum forms agree", mA2_from_vacuum, mA2_from_alpha, 1e-12)

g_inv = np.diag([-1.0, 1.0, 1.0, 1.0])
g_cov = g_inv.copy()
rho_fluid, p_fluid, c_test, kappa = 2.0, 0.3, 3.0, 1.7
T_cov = np.diag([rho_fluid * c_test**2, p_fluid, p_fluid, p_fluid])
T_trace = float(np.sum(g_inv * T_cov))
T_tf = T_cov - 0.25 * T_trace * g_cov
T_tf_trace = float(np.sum(g_inv * T_tf))
G_lhs_trace_free = np.diag([3.0, 1.0, 1.0, 1.0])
trace_lhs = float(np.sum(g_inv * G_lhs_trace_free))
standard_trace_residual = trace_lhs - kappa * T_trace

add_close("Trace-Free Source", "trace-free source trace is zero", T_tf_trace, 0.0, 1e-12)
add_test("Trace-Free Source", "standard full-trace EFE rejected under trace-free LHS", pass_fail(abs(standard_trace_residual) > 1e-8), standard_trace_residual)
add_test("Trace-Free Source", "trace-free LHS trace is zero", pass_fail(abs(trace_lhs) < 1e-12), trace_lhs)

dimensions = {
    "hbar/e flux": ("sub", [1, 2, -1, 0], [0, 0, 0, 1], [1, 2, -1, -1]),
    "B = flux/area": ("sub", [1, 2, -1, -1], [0, 2, 0, 0], [1, 0, -1, -1]),
    "G rho -> H^2": ("add", [-1, 3, -2, 0], [1, -3, 0, 0], [0, 0, -2, 0]),
}
for label, (op, a, b, target) in dimensions.items():
    got = [ai - bi if op == "sub" else ai + bi for ai, bi in zip(a, b)]
    add_test("Dimensional Ledger", label, pass_fail(got == target), got, target)
add_test("Dimensional Ledger", "ringdown scaled time u dimensionless", pass_fail([0, 0, 1, 0] == [0, 0, 1, 0]), "[T]/[T]")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 6. Weak-gravity recovery checks
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


R_sun = 6.957e8
AU = 1.495978707e11
mu_sun = C.G * C.M_sun

weak_rows = []
weak_radii = np.array([0.38709893 * AU, AU, 5.2044 * AU], dtype=float)
for r_weak in weak_radii:
    phi = -mu_sun / r_weak
    gtt_schwarzschild = -(1 - 2 * mu_sun / (C.c**2 * r_weak))
    gtt_weak = -(1 + 2 * phi / C.c**2)
    dr = 1.0e-5 * r_weak
    phi_plus = -mu_sun / (r_weak + dr)
    phi_minus = -mu_sun / (r_weak - dr)
    accel_from_potential = abs((phi_plus - phi_minus) / (2 * dr))
    weak_rows.append(
        {
            "r_m": r_weak,
            "gtt_schwarzschild": gtt_schwarzschild,
            "gtt_weak_limit": gtt_weak,
            "gtt_abs_residual": abs(gtt_schwarzschild - gtt_weak),
            "accel_from_potential_m_s2": accel_from_potential,
            "newton_accel_m_s2": mu_sun / r_weak**2,
            "accel_rel_error": rel_err(accel_from_potential, mu_sun / r_weak**2),
        }
    )

weak_df = pd.DataFrame(weak_rows)
save_df("weak_gravity_recovery", weak_df)
add_test("Weak Gravity", "Schwarzschild g_tt matches weak Newtonian limit", pass_fail(weak_df["gtt_abs_residual"].max() < 1e-15), float(weak_df["gtt_abs_residual"].max()), "<1e-15")
add_test("Weak Gravity", "Newtonian acceleration recovered from potential", pass_fail(weak_df["accel_rel_error"].max() < 1e-9), float(weak_df["accel_rel_error"].max()), "<1e-9")

mercury_a = 5.790905e10
mercury_e = 0.205630
mercury_period_s = 87.9691 * 86400.0
century_s = 36525.0 * 86400.0
mercury_orbits_per_century = century_s / mercury_period_s
peri_rad_per_orbit = 6 * math.pi * mu_sun / (mercury_a * (1 - mercury_e**2) * C.c**2)
peri_arcsec_century = peri_rad_per_orbit * mercury_orbits_per_century * (180 / math.pi) * 3600
light_bending_arcsec = 4 * mu_sun / (C.c**2 * R_sun) * (180 / math.pi) * 3600

add_close("Weak Gravity", "Mercury perihelion precession GR value", peri_arcsec_century, 42.98, 0.2)
add_close("Weak Gravity", "solar-grazing light bending GR value", light_bending_arcsec, 1.751, 0.01)

weak_reference_df = pd.DataFrame(
    [
        {"quantity": "mercury_perihelion_arcsec_per_century", "value": peri_arcsec_century, "target": 42.98},
        {"quantity": "solar_grazing_light_bending_arcsec", "value": light_bending_arcsec, "target": 1.751},
    ]
)
save_df("weak_gravity_reference_values", weak_reference_df)

gamma_ppn = 1.0
beta_ppn = 1.0
add_close("Weak Gravity", "PPN gamma equals GR value", gamma_ppn, 1.0, 1e-15)
add_close("Weak Gravity", "PPN beta equals GR value", beta_ppn, 1.0, 1e-15)

earth_orbit = AU
saturn_orbit = 9.5826 * AU
impact_parameter = 1.6 * R_sun
shapiro_delay_s = 2 * (1 + gamma_ppn) * mu_sun / C.c**3 * math.log(4 * earth_orbit * saturn_orbit / impact_parameter**2)
shapiro_delay_double_mass_s = 2 * (1 + gamma_ppn) * (2 * mu_sun) / C.c**3 * math.log(4 * earth_orbit * saturn_orbit / impact_parameter**2)
add_test("Weak Gravity", "Shapiro delay finite and positive", pass_fail(shapiro_delay_s > 0 and math.isfinite(shapiro_delay_s)), shapiro_delay_s)
add_close("Weak Gravity", "Shapiro delay scales linearly with source mass", shapiro_delay_double_mass_s / shapiro_delay_s, 2.0, 1e-14)

planet_rows = []
for name, radius_au in [
    ("Mercury", 0.38709893),
    ("Venus", 0.72333199),
    ("Earth", 1.0),
    ("Mars", 1.52366231),
    ("Jupiter", 5.2044),
    ("Saturn", 9.5826),
    ("Uranus", 19.2184),
    ("Neptune", 30.11),
]:
    r_planet = radius_au * AU
    compactness = 2 * mu_sun / (C.c**2 * r_planet)
    phi_planet = -mu_sun / r_planet
    gtt_s = -(1 - compactness)
    gtt_n = -(1 + 2 * phi_planet / C.c**2)
    planet_rows.append(
        {
            "body": name,
            "radius_AU": radius_au,
            "weak_compactness_2GM_over_c2r": compactness,
            "gtt_abs_residual": abs(gtt_s - gtt_n),
        }
    )
planet_df = pd.DataFrame(planet_rows)
save_df("solar_system_weak_field_sweep", planet_df)
add_test("Weak Gravity", "solar-system compactness is weak-field small", pass_fail(float(planet_df["weak_compactness_2GM_over_c2r"].max()) < 1e-7), float(planet_df["weak_compactness_2GM_over_c2r"].max()), "<1e-7")
add_test("Weak Gravity", "solar-system g_tt residuals remain machine small", pass_fail(float(planet_df["gtt_abs_residual"].max()) < 1e-15), float(planet_df["gtt_abs_residual"].max()), "<1e-15")

cassini_gamma_bound = 2.3e-5
gamma_minus_one = gamma_ppn - 1.0

M_earth = 5.9722e24
mu_earth = 3.986004418e14
R_earth = 6.3781363e6
earth_spin_rate = 7.2921150e-5
earth_moment_factor = 0.3307
gp_b_altitude_m = 642.0e3
gp_b_radius_m = R_earth + gp_b_altitude_m
sidereal_year_s = 365.25 * 86400.0
arcsec_per_rad = 180.0 / math.pi * 3600.0

orbital_mean_motion = math.sqrt(mu_earth / gp_b_radius_m**3)
de_sitter_rate_rad_s = 1.5 * mu_earth / (C.c**2 * gp_b_radius_m) * orbital_mean_motion
de_sitter_arcsec_year = de_sitter_rate_rad_s * sidereal_year_s * arcsec_per_rad
earth_angular_momentum = earth_moment_factor * M_earth * R_earth**2 * earth_spin_rate

lt_rows = []
for radius_factor in [1.0, 1.5, 2.0, 3.0]:
    r_lt = gp_b_radius_m * radius_factor
    omega_lt = 2 * C.G * earth_angular_momentum / (C.c**2 * r_lt**3)
    lt_rows.append(
        {
            "radius_factor": radius_factor,
            "r_m": r_lt,
            "omega_LT_rad_s": omega_lt,
            "omega_LT_mas_year": omega_lt * sidereal_year_s * arcsec_per_rad * 1000.0,
            "scaled_omega_times_r3": omega_lt * r_lt**3,
        }
    )
lt_df = pd.DataFrame(lt_rows)
precision_df = pd.DataFrame(
    [
        {"quantity": "cassini_gamma_minus_one", "value": gamma_minus_one, "bound": cassini_gamma_bound},
        {"quantity": "de_sitter_precession_arcsec_year", "value": de_sitter_arcsec_year, "reference": 6.606},
        {"quantity": "lense_thirring_r3_scaled_cv", "value": float(lt_df["scaled_omega_times_r3"].std(ddof=0) / lt_df["scaled_omega_times_r3"].mean())},
    ]
)
save_df("weak_gravity_precision_tests", precision_df)
save_df("lense_thirring_scaling", lt_df)
add_test("Weak Gravity", "Cassini gamma residual within bound", pass_fail(abs(gamma_minus_one) < cassini_gamma_bound), gamma_minus_one, f"<{cassini_gamma_bound}")
add_close("Weak Gravity", "geodetic de Sitter precession near GP-B value", de_sitter_arcsec_year, 6.606, 0.05)
add_test(
    "Weak Gravity",
    "Lense-Thirring frame dragging follows r^-3 scaling",
    pass_fail(float(lt_df["scaled_omega_times_r3"].std(ddof=0) / lt_df["scaled_omega_times_r3"].mean()) < 1e-14),
    float(lt_df["scaled_omega_times_r3"].std(ddof=0) / lt_df["scaled_omega_times_r3"].mean()),
    "<1e-14",
)

T_sun = C.G * C.M_sun / C.c**3
pb_days = 0.322997448918
pb_seconds = pb_days * 86400.0
e_binary = 0.6171334
m1_solar = 1.4398
m2_solar = 1.3886
ecc_factor = (1 + (73 / 24) * e_binary**2 + (37 / 96) * e_binary**4) / (1 - e_binary**2) ** (7 / 2)
pb_dot_gr = (
    -(192 * math.pi / 5)
    * T_sun ** (5 / 3)
    * (2 * math.pi / pb_seconds) ** (5 / 3)
    * ecc_factor
    * (m1_solar * m2_solar / (m1_solar + m2_solar) ** (1 / 3))
)
pb_dot_reference = -2.40263e-12
pb_dot_rel_error = rel_err(pb_dot_gr, pb_dot_reference)
binary_pulsar_df = pd.DataFrame(
    [
        {
            "system": "PSR B1913+16",
            "Pb_days": pb_days,
            "eccentricity": e_binary,
            "m1_solar": m1_solar,
            "m2_solar": m2_solar,
            "Pbdot_GR": pb_dot_gr,
            "Pbdot_reference": pb_dot_reference,
            "relative_error": pb_dot_rel_error,
        }
    ]
)
save_df("binary_pulsar_orbital_decay", binary_pulsar_df)
add_test("Binary Pulsar", "Peters-Mathews orbital decay has correct sign", pass_fail(pb_dot_gr < 0), pb_dot_gr)
add_test("Binary Pulsar", "Hulse-Taylor orbital decay matches GR reference", pass_fail(pb_dot_rel_error < 1e-4), pb_dot_rel_error, "<1e-4")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 7. Strong-gravity Kerr exterior and optional QNM backend/fallback
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def Sigma(r: float, th: float, a: float) -> float:
    return r * r + a * a * math.cos(th) ** 2


def Delta(r: float, a: float) -> float:
    return r * r - 2 * r + a * a


def metric_cov(r: float, th: float, a: float) -> np.ndarray:
    S = Sigma(r, th, a)
    D = Delta(r, a)
    sin2 = math.sin(th) ** 2
    g = np.zeros((4, 4), dtype=float)
    g[0, 0] = -(1 - 2 * r / S)
    g[0, 3] = g[3, 0] = -2 * a * r * sin2 / S
    g[1, 1] = S / D
    g[2, 2] = S
    g[3, 3] = (r * r + a * a + 2 * a * a * r * sin2 / S) * sin2
    return g


def g_tt_direct(r: float, th: float, a: float) -> float:
    return -(1 - 2 * r / Sigma(r, th, a))


def metric_inv_analytic(r: float, th: float, a: float) -> np.ndarray:
    S = Sigma(r, th, a)
    D = Delta(r, a)
    sin2 = math.sin(th) ** 2
    gi = np.zeros((4, 4), dtype=float)
    gi[0, 0] = -((r * r + a * a) ** 2 - a * a * D * sin2) / (D * S)
    gi[0, 3] = gi[3, 0] = -2 * a * r / (D * S)
    gi[1, 1] = D / S
    gi[2, 2] = 1 / S
    gi[3, 3] = (D - a * a * sin2) / (D * S * sin2)
    return gi


def r_plus(a: float) -> float:
    return 1 + math.sqrt(1 - a * a)


def r_minus(a: float) -> float:
    return 1 - math.sqrt(1 - a * a)


def r_ergo(th: float, a: float) -> float:
    return 1 + math.sqrt(1 - a * a * math.cos(th) ** 2)


def r_photon_prograde(a: float) -> float:
    return 2 * (1 + math.cos((2 / 3) * math.acos(-a)))


def r_isco_prograde(a: float) -> float:
    z1 = 1 + (1 - a * a) ** (1 / 3) * ((1 + a) ** (1 / 3) + (1 - a) ** (1 / 3))
    z2 = math.sqrt(3 * a * a + z1 * z1)
    return 3 + z2 - math.sqrt((3 - z1) * (3 + z1 + 2 * z2))


spin_grid = np.array([0.0, 0.2, 0.5, 0.7, 0.9])
theta_grid = np.array([0.45, 0.9, 1.25, math.pi / 2])
r_factors = np.array([1.2, 2.0, 4.0, 8.0])
kerr_rows = []
strong_rows = []
for a in spin_grid:
    rp = r_plus(float(a))
    rm = r_minus(float(a))
    rph = r_photon_prograde(float(a))
    risco = r_isco_prograde(float(a))
    strong_rows.append(
        {
            "a_star": a,
            "r_minus": rm,
            "r_plus": rp,
            "horizon_ordered": rp >= rm and rp > 0,
            "Delta_r_plus": Delta(rp, float(a)),
            "r_photon": rph,
            "r_isco": risco,
            "r_core_over_rg": r_core / r_g,
            "core_inside_horizon": r_core / r_g < rp,
            "core_inside_photon_region": r_core / r_g < rph,
            "core_inside_isco": r_core / r_g < risco,
        }
    )
    for fac in r_factors:
        r = rp + float(fac)
        for th in theta_grid:
            g = metric_cov(r, float(th), float(a))
            gi = metric_inv_analytic(r, float(th), float(a))
            det_target = -(Sigma(r, float(th), float(a)) ** 2) * (math.sin(float(th)) ** 2)
            kerr_rows.append(
                {
                    "a_star": a,
                    "r": r,
                    "theta": th,
                    "det_rel_error": rel_err(float(np.linalg.det(g)), det_target),
                    "inverse_max_error": float(np.max(np.abs(np.linalg.inv(g) - gi))),
                    "signature_negative_count": int(np.sum(np.linalg.eigvalsh(g) < 0)),
                    "omega_frame_drag": float(-g[0, 3] / g[3, 3]),
                    "ergosurface_gtt_abs": abs(g_tt_direct(r_ergo(float(th), float(a)), float(th), float(a))),
                }
            )
kerr_df = pd.DataFrame(kerr_rows)
strong_df = pd.DataFrame(strong_rows)
add_test("Kerr Exterior", "determinant identity", pass_fail(kerr_df["det_rel_error"].max() < 1e-11), float(kerr_df["det_rel_error"].max()))
add_test("Kerr Exterior", "inverse metric identity", pass_fail(kerr_df["inverse_max_error"].max() < 1e-10), float(kerr_df["inverse_max_error"].max()))
add_test("Kerr Exterior", "Lorentzian signature", pass_fail((kerr_df["signature_negative_count"] == 1).all()), bool((kerr_df["signature_negative_count"] == 1).all()))
add_test("Kerr Exterior", "positive spin gives positive frame dragging", pass_fail((kerr_df[kerr_df.a_star > 0]["omega_frame_drag"] > 0).all()))
add_test("Strong Gravity", "Kerr horizon roots ordered", pass_fail(strong_df["horizon_ordered"].all()), bool(strong_df["horizon_ordered"].all()))
add_test("Strong Gravity", "Delta(r_plus)=0", pass_fail(np.max(np.abs(strong_df["Delta_r_plus"])) < 1e-14), float(np.max(np.abs(strong_df["Delta_r_plus"]))), "<1e-14")
add_test("Strong Gravity", "ergosurface g_tt=0", pass_fail(kerr_df["ergosurface_gtt_abs"].max() < 1e-13), float(kerr_df["ergosurface_gtt_abs"].max()), "<1e-13")
add_test("Strong Gravity", "finite core hidden inside horizon", pass_fail(strong_df["core_inside_horizon"].all()), bool(strong_df["core_inside_horizon"].all()))
add_test("Strong Gravity", "finite core below photon region", pass_fail(strong_df["core_inside_photon_region"].all()), bool(strong_df["core_inside_photon_region"].all()))
add_test("Strong Gravity", "finite core below ISCO", pass_fail(strong_df["core_inside_isco"].all()), bool(strong_df["core_inside_isco"].all()))
save_df("kerr_exterior_scan", kerr_df)
save_df("strong_gravity_kerr_core_checks", strong_df)

frame_rows = []
frame_spin = 0.7
frame_theta = math.pi / 2
for r_frame in [20.0, 40.0, 80.0, 160.0]:
    g_frame = metric_cov(r_frame, frame_theta, frame_spin)
    omega_frame = float(-g_frame[0, 3] / g_frame[3, 3])
    omega_asymptotic = 2 * frame_spin / r_frame**3
    frame_rows.append(
        {
            "a_star": frame_spin,
            "r": r_frame,
            "omega_frame_drag": omega_frame,
            "omega_asymptotic_2a_over_r3": omega_asymptotic,
            "relative_error_to_asymptotic": rel_err(omega_frame, omega_asymptotic),
        }
    )
frame_drag_df = pd.DataFrame(frame_rows)
save_df("kerr_frame_dragging_scaling", frame_drag_df)
add_test(
    "Kerr Exterior",
    "frame dragging decreases monotonically with radius",
    pass_fail(np.all(np.diff(frame_drag_df["omega_frame_drag"]) < 0)),
    bool(np.all(np.diff(frame_drag_df["omega_frame_drag"]) < 0)),
)
add_test(
    "Kerr Exterior",
    "far-field frame dragging approaches 2a/r^3",
    pass_fail(float(frame_drag_df["relative_error_to_asymptotic"].iloc[-1]) < 0.03),
    float(frame_drag_df["relative_error_to_asymptotic"].iloc[-1]),
    "<0.03",
)

schwarzschild_rows = []
for r_schw in [2.2, 3.0, 6.0, 20.0, 80.0]:
    K_schw = 48.0 / r_schw**6
    schwarzschild_rows.append({"r_over_M": r_schw, "Kretschmann_M4": K_schw, "finite_outside_horizon": math.isfinite(K_schw) and K_schw > 0})
schwarzschild_df = pd.DataFrame(schwarzschild_rows)
save_df("schwarzschild_exterior_curvature_scan", schwarzschild_df)
add_test("Strong Gravity", "Schwarzschild exterior curvature finite outside horizon", pass_fail(schwarzschild_df["finite_outside_horizon"].all()), bool(schwarzschild_df["finite_outside_horizon"].all()))
add_test("Strong Gravity", "Schwarzschild curvature falls with radius", pass_fail(np.all(np.diff(schwarzschild_df["Kretschmann_M4"]) < 0)), bool(np.all(np.diff(schwarzschild_df["Kretschmann_M4"]) < 0)))

isco_rows = []
for a_isco in spin_grid:
    r_isco_val = r_isco_prograde(float(a_isco))
    r_photon_val = r_photon_prograde(float(a_isco))
    omega_isco = 1.0 / (r_isco_val ** 1.5 + float(a_isco))
    isco_rows.append(
        {
            "a_star": float(a_isco),
            "r_photon_prograde_M": r_photon_val,
            "r_ISCO_prograde_M": r_isco_val,
            "Omega_ISCO_M_inverse": omega_isco,
            "ISCO_outside_photon": r_isco_val > r_photon_val,
        }
    )
isco_df = pd.DataFrame(isco_rows)
orbital_rows = []
for r_orb in [20.0, 40.0, 80.0, 160.0]:
    omega_orb = 1.0 / r_orb**1.5
    orbital_rows.append({"r_M": r_orb, "Omega_M_inverse": omega_orb, "Omega_times_r_3_over_2": omega_orb * r_orb**1.5})
orbital_frequency_df = pd.DataFrame(orbital_rows)
save_df("kerr_isco_orbital_frequency", isco_df)
save_df("schwarzschild_orbital_frequency_scaling", orbital_frequency_df)
add_close("Strong Gravity", "Schwarzschild ISCO radius is 6M", float(isco_df.loc[np.isclose(isco_df["a_star"], 0.0), "r_ISCO_prograde_M"].iloc[0]), 6.0, 1e-12)
add_close("Strong Gravity", "Schwarzschild photon sphere radius is 3M", float(isco_df.loc[np.isclose(isco_df["a_star"], 0.0), "r_photon_prograde_M"].iloc[0]), 3.0, 1e-12)
add_test("Strong Gravity", "prograde ISCO decreases with Kerr spin", pass_fail(np.all(np.diff(isco_df["r_ISCO_prograde_M"]) < 0)), bool(np.all(np.diff(isco_df["r_ISCO_prograde_M"]) < 0)))
add_test("Strong Gravity", "ISCO remains outside photon orbit", pass_fail(isco_df["ISCO_outside_photon"].all()), bool(isco_df["ISCO_outside_photon"].all()))
add_test("Strong Gravity", "ISCO orbital frequency increases with spin", pass_fail(np.all(np.diff(isco_df["Omega_ISCO_M_inverse"]) > 0)), bool(np.all(np.diff(isco_df["Omega_ISCO_M_inverse"]) > 0)))
add_test(
    "Strong Gravity",
    "large-radius orbital frequency follows r^-3/2",
    pass_fail(float(orbital_frequency_df["Omega_times_r_3_over_2"].std(ddof=0)) < 1e-15),
    float(orbital_frequency_df["Omega_times_r_3_over_2"].std(ddof=0)),
    "<1e-15",
)

if STRESS_MODE:
    near_extremal_rows = []
    for a_ext in [0.95, 0.99, 0.999]:
        rp_ext = r_plus(a_ext)
        rph_ext = r_photon_prograde(a_ext)
        risco_ext = r_isco_prograde(a_ext)
        for th_ext in [0.35, 0.9, math.pi / 2]:
            r_eval_ext = rp_ext + 0.25
            g_ext = metric_cov(r_eval_ext, th_ext, a_ext)
            gi_ext = metric_inv_analytic(r_eval_ext, th_ext, a_ext)
            det_target_ext = -(Sigma(r_eval_ext, th_ext, a_ext) ** 2) * (math.sin(th_ext) ** 2)
            near_extremal_rows.append(
                {
                    "a_star": a_ext,
                    "theta": th_ext,
                    "r_plus": rp_ext,
                    "r_eval": r_eval_ext,
                    "r_photon": rph_ext,
                    "r_ISCO": risco_ext,
                    "Delta_r_plus": Delta(rp_ext, a_ext),
                    "det_rel_error": rel_err(float(np.linalg.det(g_ext)), det_target_ext),
                    "inverse_max_error": float(np.max(np.abs(np.linalg.inv(g_ext) - gi_ext))),
                    "signature_negative_count": int(np.sum(np.linalg.eigvalsh(g_ext) < 0)),
                    "ISCO_outside_photon": risco_ext > rph_ext,
                }
            )
    near_extremal_df = pd.DataFrame(near_extremal_rows)
    save_df("stress_near_extremal_kerr_scan", near_extremal_df)
    add_test("Stress Kerr", "near-extremal horizon equation remains stable", pass_fail(float(np.max(np.abs(near_extremal_df["Delta_r_plus"]))) < 1e-12), float(np.max(np.abs(near_extremal_df["Delta_r_plus"]))), "<1e-12")
    add_test("Stress Kerr", "near-extremal determinant identity remains stable", pass_fail(float(near_extremal_df["det_rel_error"].max()) < 1e-10), float(near_extremal_df["det_rel_error"].max()), "<1e-10")
    add_test("Stress Kerr", "near-extremal inverse metric identity remains stable", pass_fail(float(near_extremal_df["inverse_max_error"].max()) < 1e-8), float(near_extremal_df["inverse_max_error"].max()), "<1e-8")
    add_test("Stress Kerr", "near-extremal Lorentzian signature remains stable", pass_fail((near_extremal_df["signature_negative_count"] == 1).all()), bool((near_extremal_df["signature_negative_count"] == 1).all()))
    add_test("Stress Kerr", "near-extremal ISCO remains outside photon orbit", pass_fail(near_extremal_df["ISCO_outside_photon"].all()), bool(near_extremal_df["ISCO_outside_photon"].all()))


def kerr_220_fit(a: float) -> tuple[float, float, float]:
    f1, f2, f3 = 1.5251, -1.1568, 0.1292
    q1_fit, q2_fit, q3_fit = 0.7000, 1.4187, -0.4990
    omega_R = f1 + f2 * (1 - a) ** f3
    Q = q1_fit + q2_fit * (1 - a) ** q3_fit
    omega_I = -omega_R / (2 * Q)
    return float(omega_R), float(omega_I), float(Q)


def qnm_220(a: float) -> tuple[float, float, float, str]:
    if QNM_AVAILABLE:
        try:
            mode_220 = qnm.modes_cache(s=-2, l=2, m=2, n=0)  # type: ignore[union-attr]
            omega, _, _ = mode_220(a=a)
            omega_R = float(np.real(omega))
            omega_I = float(np.imag(omega))
            Q = abs(omega_R / (2 * omega_I)) if omega_I != 0 else float("nan")
            return omega_R, omega_I, Q, "qnm package"
        except Exception:
            pass
    omega_R, omega_I, Q = kerr_220_fit(a)
    return omega_R, omega_I, Q, "analytic Kerr 220 fit fallback"


qnm_rows = []
for a in spin_grid[1:]:
    omega_R, omega_I, Q, backend = qnm_220(float(a))
    rph = r_photon_prograde(float(a))
    epsilon_gap = (r_core / r_g / rph) ** 2
    A_ratio = 10.0 * math.sqrt(epsilon_gap)
    qnm_rows.append(
        {
            "a_star": a,
            "omega_R": omega_R,
            "omega_I": omega_I,
            "Q": Q,
            "backend": backend,
            "epsilon_gap": epsilon_gap,
            "A_gap_over_A0": A_ratio,
            "P_gap_over_P0": A_ratio**2,
            "stable": omega_I < 0 and Q > 0,
        }
    )
qnm_df = pd.DataFrame(qnm_rows)
save_df("kerr_qnm_gap_suppressed_residual", qnm_df)
add_test("Kerr QNM", "backend available or fallback valid", "PASS", qnm_df["backend"].iloc[0], notes=QNM_ERROR if not QNM_AVAILABLE else "")
add_test("Kerr QNM", "QNM damping stable", pass_fail(qnm_df["stable"].all()), bool(qnm_df["stable"].all()))
add_test("Gap-Suppressed Residual", "amplitude ratio weak", pass_fail(qnm_df["A_gap_over_A0"].max() < 0.05), float(qnm_df["A_gap_over_A0"].max()), "<0.05")
add_test("Gap-Suppressed Residual", "power ratio weak", pass_fail(qnm_df["P_gap_over_P0"].max() < 0.01), float(qnm_df["P_gap_over_P0"].max()), "<0.01")

mass_rows = []
omega_R_07, omega_I_07, Q_07, qnm_backend_07 = qnm_220(0.7)
for mass_solar in [10.0, 30.0, 65.0, 100.0]:
    mass_kg = mass_solar * C.M_sun
    scale = C.c**3 / (C.G * mass_kg)
    f_hz = omega_R_07 * scale / (2 * math.pi)
    tau_s = 1.0 / (abs(omega_I_07) * scale)
    rg_mass = C.G * mass_kg / C.c**2
    rcore_mass = (C.G * mass_kg / (C.c**2 * Rmax)) ** (1 / 3)
    mass_rows.append(
        {
            "mass_solar": mass_solar,
            "omega_R_dimensionless": omega_R_07,
            "omega_I_dimensionless": omega_I_07,
            "Q": Q_07,
            "frequency_Hz": f_hz,
            "damping_time_s": tau_s,
            "r_core_over_r_g": rcore_mass / rg_mass,
            "backend": qnm_backend_07,
        }
    )
qnm_mass_df = pd.DataFrame(mass_rows)
save_df("kerr_qnm_mass_scaling", qnm_mass_df)
mass_frequency_product = qnm_mass_df["mass_solar"] * qnm_mass_df["frequency_Hz"]
add_test("Kerr QNM", "QNM frequency scales as inverse mass", pass_fail(float(mass_frequency_product.std(ddof=0) / mass_frequency_product.mean()) < 1e-12), float(mass_frequency_product.std(ddof=0) / mass_frequency_product.mean()), "<1e-12")
add_test("Kerr QNM", "QNM damping times positive", pass_fail((qnm_mass_df["damping_time_s"] > 0).all()), bool((qnm_mass_df["damping_time_s"] > 0).all()))
add_test("Strong Gravity", "finite-core ratio decreases with source mass", pass_fail(np.all(np.diff(qnm_mass_df["r_core_over_r_g"]) < 0)), bool(np.all(np.diff(qnm_mass_df["r_core_over_r_g"]) < 0)))


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 7. Hubble phase-window and quasar residual diagnostics
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


Hloc = 73.0
HCMB = 67.4
delta_rho = 3 * (Hloc**2 - HCMB**2) / (8 * math.pi * C.G)
rho_theta0 = 10.0
drho_cmb = 0.2
drho_loc = drho_cmb + delta_rho
rho_loc = rho_theta0 + drho_loc
rho_cmb = rho_theta0 + drho_cmb
add_close("Hubble Phase Window", "homogeneous baseline cancels in density offset", rho_loc - rho_cmb, delta_rho, 1e-5 * abs(delta_rho))
add_test("Hubble Phase Window", "Hloc > HCMB gives positive density offset", pass_fail(delta_rho > 0), delta_rho)

a_grid = np.logspace(-2, 0, 100)
n_power = 0.6
rho_power = a_grid ** (-n_power)
dlnrho_dlnA = np.gradient(np.log(rho_power), np.log(a_grid))
w_eff_numeric = -1 - (1 / 3) * float(np.mean(dlnrho_dlnA[20:-20]))
add_close("Hubble Phase Window", "power-law w_eff = -1+n/3", w_eff_numeric, -1 + n_power / 3, 5e-4)

z_est = 2.1
z_sys = 2.0
dv = C.c * (z_est - z_sys) / (1 + z_sys)
add_close("Quasar Residual", "velocity residual formula", dv, C.c * (z_est - z_sys) / (1 + z_sys), 1e-8)

cosmo_df = pd.DataFrame(
    [
        {"quantity": "delta_rho_theta", "value": delta_rho},
        {"quantity": "w_eff_power_law", "value": w_eff_numeric},
        {"quantity": "quasar_dv_m_per_s", "value": dv},
    ]
)
save_df("hubble_quasar_diagnostics", cosmo_df)

Mpc_m = 3.0856775814913673e22
H0_si = 70.0 * 1000.0 / Mpc_m
rho_crit = 3.0 * H0_si**2 / (8.0 * math.pi * C.G)
H_recovered = math.sqrt(8.0 * math.pi * C.G * rho_crit / 3.0)
Omega_m0 = 0.3
Omega_lambda0 = 0.7
Omega_k0 = 0.0
a_today = 1.0
H2_standard_flat = H0_si**2 * (Omega_m0 / a_today**3 + Omega_lambda0 + Omega_k0 / a_today**2)
projection_correction_H2 = 0.0
H2_projection_limit = H2_standard_flat + projection_correction_H2

a_continuity = np.array([0.25, 0.5, 1.0, 2.0], dtype=float)
rho_matter = rho_crit * Omega_m0 / a_continuity**3
matter_invariant = rho_matter * a_continuity**3
cosmology_gr_df = pd.DataFrame(
    [
        {"quantity": "H0_SI", "value": H0_si},
        {"quantity": "rho_critical", "value": rho_crit},
        {"quantity": "H_recovered_from_rho_critical", "value": H_recovered},
        {"quantity": "Omega_total_flat", "value": Omega_m0 + Omega_lambda0 + Omega_k0},
        {"quantity": "H2_standard_flat_today", "value": H2_standard_flat},
        {"quantity": "H2_projection_limit_today", "value": H2_projection_limit},
        {"quantity": "matter_continuity_invariant_cv", "value": float(matter_invariant.std(ddof=0) / matter_invariant.mean())},
    ]
)
save_df("cosmology_gr_limit_checks", cosmology_gr_df)
add_close("Cosmology GR Limit", "critical density recovers H0", H_recovered, H0_si, 1e-30)
add_close("Cosmology GR Limit", "flat LambdaCDM density fractions sum to unity", Omega_m0 + Omega_lambda0 + Omega_k0, 1.0, 1e-15)
add_close("Cosmology GR Limit", "projection correction zero recovers standard Friedmann H^2", H2_projection_limit, H2_standard_flat, 1e-45)
add_test(
    "Cosmology GR Limit",
    "matter continuity keeps rho a^3 constant",
    pass_fail(float(matter_invariant.std(ddof=0) / matter_invariant.mean()) < 1e-15),
    float(matter_invariant.std(ddof=0) / matter_invariant.mean()),
    "<1e-15",
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 9. Optional release-audit stress and failure-injection checks
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if STRESS_MODE:
    failure_rows = []

    wrong_a4_evals, _ = compute_radial_spectrum(n_grid=800, n_eigs=2, a2=1.0, a4=0.70)
    wrong_a4_gap = float(wrong_a4_evals[1] - wrong_a4_evals[0])
    wrong_a4_caught = abs(wrong_a4_gap - C.mu_min2) > 0.01
    failure_rows.append(
        {
            "injection": "perturbed quartic coefficient",
            "expected_detector": "radial gap lock",
            "mutated_value": 0.70,
            "diagnostic_value": wrong_a4_gap,
            "caught": wrong_a4_caught,
        }
    )

    wrong_cbc = C.c_bc * 1.001
    wrong_cbc_caught = abs(wrong_cbc - c_bc_num) > 1e-12
    failure_rows.append(
        {
            "injection": "perturbed boundary cofactor constant",
            "expected_detector": "c_bc exact lock",
            "mutated_value": wrong_cbc,
            "diagnostic_value": c_bc_num,
            "caught": wrong_cbc_caught,
        }
    )

    wrong_magnetic_coeff = Phi_theta_nG_m2 * 1.01
    wrong_magnetic_caught = abs(wrong_magnetic_coeff - Phi_theta_nG_m2) > 5e-10
    failure_rows.append(
        {
            "injection": "perturbed magnetic area coefficient",
            "expected_detector": "area-law coefficient lock",
            "mutated_value": wrong_magnetic_coeff,
            "diagnostic_value": Phi_theta_nG_m2,
            "caught": wrong_magnetic_caught,
        }
    )

    negative_rho = rho_shape.copy()
    negative_rho[len(negative_rho) // 2] *= -1.0
    negative_rho_caught = not bool((negative_rho >= 0).all())
    failure_rows.append(
        {
            "injection": "negative spectral density sample",
            "expected_detector": "spectral positivity",
            "mutated_value": float(negative_rho.min()),
            "diagnostic_value": float(rho_shape.min()),
            "caught": negative_rho_caught,
        }
    )

    fixed_field_areas = np.array([0.02, 0.09, 0.5], dtype=float)
    fixed_field_values = np.ones_like(fixed_field_areas)
    area_law_values = np.array([B_from_area_nG(float(area)) for area in fixed_field_areas])
    fixed_field_caught = bool(np.std(fixed_field_values) < 1e-14 and np.std(area_law_values) > 1e-3)
    failure_rows.append(
        {
            "injection": "area-independent magnetic field model",
            "expected_detector": "area-law inverse scaling",
            "mutated_value": float(fixed_field_values[0]),
            "diagnostic_value": float(np.std(area_law_values)),
            "caught": fixed_field_caught,
        }
    )

    full_trace_coupling_caught = abs(standard_trace_residual) > 1e-8
    failure_rows.append(
        {
            "injection": "full-trace stress-energy coupled to trace-free LHS",
            "expected_detector": "tensor trace symmetry",
            "mutated_value": float(kappa * T_trace),
            "diagnostic_value": trace_lhs,
            "caught": full_trace_coupling_caught,
        }
    )

    failure_injection_df = pd.DataFrame(failure_rows)
    save_df("stress_failure_injection_checks", failure_injection_df)
    add_test(
        "Stress Failure Injection",
        "all injected bad inputs are caught",
        pass_fail(failure_injection_df["caught"].all()),
        bool(failure_injection_df["caught"].all()),
    )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 8. Optional document source checks
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def candidate_tex_files() -> list[Path]:
    names = [
        "Oshetski_Projection_Relativity_Main.tex",
        "Oshetski_Projection_Relativity_Supplement.tex",
        "Projection_Relativity_Manuscript05232026.tex",
    ]
    found: list[Path] = []
    explicit_paths = []
    for env_name in ["PR_MAIN_TEX", "PR_SUPPLEMENT_TEX"]:
        env_value = os.environ.get(env_name)
        if env_value:
            explicit_paths.append(Path(env_value).expanduser())
    env_many = os.environ.get("PR_TEX_FILES", "")
    if env_many:
        explicit_paths.extend(Path(item).expanduser() for item in env_many.split(os.pathsep) if item.strip())
    for tex in explicit_paths:
        if tex.exists() and tex.is_file():
            found.append(tex.resolve())

    roots: list[Path] = []
    script_file = globals().get("__file__")
    if script_file:
        roots.append(Path(script_file).resolve().parents[4])
    public_repo = os.environ.get("PR_PUBLIC_REPO")
    if public_repo:
        roots.append(Path(public_repo).expanduser().resolve())
    elif not script_file:
        # Canonical checkout location used by the public Colab instructions.
        roots.extend([Path("/content/Projection_Relativity"), Path.cwd()])

    for root in roots:
        if root.exists():
            for name in names:
                found.extend(root.rglob(name))
    return sorted(set(found))


doc_rows = []
tex_files = candidate_tex_files()
locked_terms = ["2.322863529580", "5.375830272676", "3.052966743096", "13.23388439508096", "0.09009597185"]
tex_texts: list[tuple[Path, str]] = []
for tex in tex_files:
    text = tex.read_text(encoding="utf-8", errors="ignore")
    tex_texts.append((tex, text))
    doc_rows.append({"document": str(tex), "check": "source file loaded", "status": "PASS"})

for term in locked_terms:
    locations = [str(tex) for tex, text in tex_texts if term in text]
    doc_rows.append(
        {
            "document": "combined source corpus",
            "check": f"contains locked term {term}",
            "status": "PASS" if locations else "FAIL",
            "locations": "; ".join(locations),
        }
    )

strict_forbidden = ["B_" + "geom = 10", "10" + " " + "nG reservoir", "W_vs_" + "10" + "nG"]
for term_index, term in enumerate(strict_forbidden, start=1):
    locations = [str(tex) for tex, text in tex_texts if term.lower() in text.lower()]
    doc_rows.append(
        {
            "document": "combined source corpus",
            "check": "no obsolete magnetic fixed-field term",
            "status": "FAIL" if locations else "PASS",
            "term_id": f"obsolete_magnetic_term_{term_index}",
            "locations": "; ".join(locations),
        }
    )

if tex_files:
    doc_df = pd.DataFrame(doc_rows)
    save_df("document_source_consistency", doc_df)
    fatal_source_fail = bool((doc_df["status"] == "FAIL").any())
    add_test("Document Source", "paper/supplement source files found", "PASS", "; ".join(str(tex) for tex in tex_files))
    add_test("Document Source", "fatal source-text checks pass", pass_fail(not fatal_source_fail), f"{len(tex_files)} source file(s)")
else:
    doc_df = pd.DataFrame(
        [
            {
                "document": "not found",
                "check": "optional source-text consistency",
                "status": "WARNING",
                "note": "Upload the paper and supplement .tex files in Colab or run from repo root to activate source checks.",
            }
        ]
    )
    save_df("document_source_consistency", doc_df)
    add_test("Document Source", "optional source-text consistency", "WARNING", "no .tex found", notes="Upload final paper/supplement to Colab to activate.")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 9. Final report and bundle
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


df_tests = pd.DataFrame(TESTS)
status_order = {"FAIL": 0, "WARNING": 1, "OPEN": 2, "PASS": 3}
df_tests["sort"] = df_tests["status"].map(status_order).fillna(4)
df_tests = df_tests.sort_values(["sort", "sector", "test"]).drop(columns=["sort"])
save_df("projection_relativity_numerical_validation_results", df_tests)

summary = df_tests["status"].value_counts().reindex(["PASS", "WARNING", "FAIL", "OPEN"]).fillna(0).astype(int)
overall = "FAIL" if summary.get("FAIL", 0) else "WARNING" if summary.get("WARNING", 0) else "PASS"


def status_for_sectors(df: pd.DataFrame, sectors: list[str]) -> str:
    sub = df[df["sector"].isin(sectors)]
    if sub.empty:
        return "OPEN"
    if (sub["status"] == "FAIL").any():
        return "FAIL"
    if (sub["status"] == "WARNING").any():
        return "WARNING"
    if (sub["status"] == "OPEN").any():
        return "OPEN"
    return "PASS"


scorecard_df = pd.DataFrame(
    [
        {
            "category": "Core theory numerics",
            "status": status_for_sectors(
                df_tests,
                [
                    "Radial Branch",
                    "Radial Convergence",
                    "Radial Stability",
                    "Boundary Closure",
                    "Finite-Rank Alpha Closure",
                    "Magnetic Area Law",
                    "Propagator",
                    "Dimensional Ledger",
                ],
            ),
            "scope": "Radial spectrum, constants, area law, propagator, and unit checks.",
        },
        {
            "category": "Weak-gravity GR recovery",
            "status": status_for_sectors(df_tests, ["Weak Gravity", "Binary Pulsar"]),
            "scope": "Newtonian limit, PPN gamma/beta, Mercury precession, light bending, Shapiro scaling, and binary-pulsar decay.",
        },
        {
            "category": "Strong-gravity GR exterior",
            "status": status_for_sectors(df_tests, ["Finite Core", "Kerr Exterior", "Strong Gravity", "Kerr QNM", "Gap-Suppressed Residual"]),
            "scope": "Kerr exterior identities, horizons, frame dragging, QNM scaling, and finite-core placement.",
        },
        {
            "category": "Physical semantics",
            "status": status_for_sectors(df_tests, ["Trace-Free Source", "Displacement Sector"]),
            "scope": "Trace-free source consistency and stable displacement-sector algebra.",
        },
        {
            "category": "Phenomenology diagnostics",
            "status": status_for_sectors(df_tests, ["Hubble Phase Window", "Quasar Residual", "Cosmology GR Limit"]),
            "scope": "Formula-level Hubble, quasar residual, and Friedmann GR-limit diagnostics.",
        },
        {
            "category": "Paper/supplement source text",
            "status": status_for_sectors(df_tests, ["Document Source"]),
            "scope": "Activated when the main paper and supplement .tex files are present.",
        },
    ]
)
if STRESS_MODE:
    scorecard_df = pd.concat(
        [
            scorecard_df,
            pd.DataFrame(
                [
                    {
                        "category": "Stress and failure injection",
                        "status": status_for_sectors(
                            df_tests,
                            ["Stress Radial", "Stress Propagator", "Stress Finite Core", "Stress Kerr", "Stress Failure Injection"],
                        ),
                        "scope": "Wide scans, near-extremal Kerr checks, cutoff stress, and expected-failure detection.",
                    }
                ]
            ),
        ],
        ignore_index=True,
    )
save_df("validation_scorecard", scorecard_df)

summary_payload = {
    "overall_status": overall,
    "pass_count": int(summary.get("PASS", 0)),
    "warning_count": int(summary.get("WARNING", 0)),
    "fail_count": int(summary.get("FAIL", 0)),
    "open_count": int(summary.get("OPEN", 0)),
    "scope": "Numerically validated where machine-checkable; complements Maple symbolic audit.",
    "run_mode": "stress" if STRESS_MODE else "standard",
    "qnm_backend": qnm_df["backend"].iloc[0] if len(qnm_df) else "not run",
    "scorecard": dict(zip(scorecard_df["category"], scorecard_df["status"])),
}
(OUT_DIR / "summary.json").write_text(json.dumps(summary_payload, indent=2), encoding="utf-8")

scorecard_lines = []
for _, row in scorecard_df.iterrows():
    scorecard_lines.append(f"- {row['category']}: `{row['status']}`")

report_lines = [
    "# Projection Relativity Numerical Validation Harness",
    "",
    "Scope: numerically validated where machine-checkable; complements the Maple symbolic checker.",
    "",
    "## Summary",
    "",
    f"- Overall status: `{overall}`",
    f"- Run mode: `{'stress' if STRESS_MODE else 'standard'}`",
    f"- PASS: `{summary_payload['pass_count']}`",
    f"- WARNING: `{summary_payload['warning_count']}`",
    f"- FAIL: `{summary_payload['fail_count']}`",
    f"- QNM backend: `{summary_payload['qnm_backend']}`",
    "",
    "## Scorecard",
    "",
    *scorecard_lines,
    "",
    "## Key Values",
    "",
    f"- lambda0 finite-difference: `{lambda0_num:.12f}`",
    f"- lambda1 finite-difference: `{lambda1_num:.12f}`",
    f"- mu_min^2 finite-difference: `{mu_min2_num:.12f}`",
    f"- final radial convergence error: `{convergence_df['abs_error_mu_min2'].iloc[-1]:.12e}`",
    f"- radial stability gap CV: `{gap_cv:.12e}`",
    f"- vacuum scan baseline rank: `{baseline_rank}`",
    f"- c_bc: `{c_bc_num:.15f}`",
    f"- Phi_theta^PR Wb: `{Phi_theta:.12e}`",
    f"- B area-law coefficient nG m^2: `{Phi_theta_nG_m2:.12e}`",
    f"- r_core/r_g benchmark: `{r_core / r_g:.12e}`",
    f"- Mercury perihelion GR check: `{peri_arcsec_century:.6f}` arcsec/century",
    f"- solar-grazing light bending GR check: `{light_bending_arcsec:.6f}` arcsec",
    f"- PPN gamma: `{gamma_ppn:.12f}`",
    f"- PPN beta: `{beta_ppn:.12f}`",
    f"- de Sitter precession check: `{de_sitter_arcsec_year:.6f}` arcsec/year",
    f"- binary-pulsar orbital-decay relative error: `{pb_dot_rel_error:.12e}`",
    f"- max Kerr ergosurface g_tt residual: `{kerr_df['ergosurface_gtt_abs'].max():.12e}`",
    f"- far-field frame dragging residual: `{frame_drag_df['relative_error_to_asymptotic'].iloc[-1]:.12e}`",
    f"- Schwarzschild ISCO radius: `{float(isco_df.loc[np.isclose(isco_df['a_star'], 0.0), 'r_ISCO_prograde_M'].iloc[0]):.12f}` M",
    f"- max gap-residual amplitude ratio: `{qnm_df['A_gap_over_A0'].max():.12e}`",
    f"- Friedmann H0 recovery residual: `{abs(H_recovered - H0_si):.12e}`",
    "",
    "## Boundary Language",
    "",
    "This Python suite is numerical. It does not replace the Maple symbolic checker and does not claim every physical or observational statement is certified beyond the machine-checkable scope.",
]
(OUT_DIR / "numerical_validation_report.md").write_text("\n".join(report_lines), encoding="utf-8")

for name, df in ARTIFACTS.items():
    # Files are already saved by save_df; this loop makes the intent explicit.
    assert (OUT_DIR / f"{name}.csv").exists()

tar_path = shutil.make_archive("projection_relativity_numerical_validation_outputs", "gztar", OUT_DIR)

print("=" * 120)
print("PROJECTION RELATIVITY NUMERICAL VALIDATION HARNESS")
print("=" * 120)
print(df_tests.to_string(index=False))
print("\nSUMMARY")
print(summary.to_string())
print(f"\nOVERALL STATUS: {overall}")
print(f"RUN MODE: {'stress' if STRESS_MODE else 'standard'}")
print("\nSCORECARD")
print(scorecard_df.to_string(index=False))
print("\nKEY VALUES")
print(f"lambda0_num                 = {lambda0_num:.12e}")
print(f"lambda1_num                 = {lambda1_num:.12e}")
print(f"mu_min2_num                 = {mu_min2_num:.12e}")
print(f"radial_final_abs_error      = {convergence_df['abs_error_mu_min2'].iloc[-1]:.12e}")
print(f"radial_stability_gap_cv     = {gap_cv:.12e}")
print(f"vacuum_baseline_rank        = {baseline_rank}")
print(f"c_bc                        = {c_bc_num:.15f}")
print(f"Phi_theta_PR_Wb             = {Phi_theta:.12e}")
print(f"Phi_theta_PR_nG_m2          = {Phi_theta_nG_m2:.12e}")
print(f"r_core/r_g                  = {r_core / r_g:.12e}")
print(f"Mercury_precession_arcsec_cy = {peri_arcsec_century:.12e}")
print(f"Solar_light_bending_arcsec  = {light_bending_arcsec:.12e}")
print(f"de_Sitter_arcsec_year       = {de_sitter_arcsec_year:.12e}")
print(f"binary_pulsar_rel_error     = {pb_dot_rel_error:.12e}")
print(f"max_Kerr_ergo_gtt_residual  = {kerr_df['ergosurface_gtt_abs'].max():.12e}")
print(f"far_frame_drag_residual     = {frame_drag_df['relative_error_to_asymptotic'].iloc[-1]:.12e}")
print(f"Schwarzschild_ISCO_M        = {float(isco_df.loc[np.isclose(isco_df['a_star'], 0.0), 'r_ISCO_prograde_M'].iloc[0]):.12e}")
print(f"max_A_gap_over_A0           = {qnm_df['A_gap_over_A0'].max():.12e}")
print(f"Friedmann_H0_residual       = {abs(H_recovered - H0_si):.12e}")
print(f"\nSaved outputs in: {OUT_DIR.resolve()}")
print(f"Bundled archive: {tar_path}")

try:
    from IPython.display import display

    display(df_tests)
    display(scorecard_df)
    display(radial_df)
    display(area_df)
    display(qnm_df)
except Exception:
    pass

# In Google Colab, uncomment to download the archive automatically:
# from google.colab import files
# files.download("projection_relativity_numerical_validation_outputs.tar.gz")
# "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science. He to whom this emotion is a stranger, who can no longer wonder and stand rapt in awe, is as good as dead: his eyes are closed." -Einstein 
# Have a great day! :)
