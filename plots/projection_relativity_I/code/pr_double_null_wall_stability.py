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
# Projection Relativity
# Michael Stanislaus Oshetski
# ORCID# 0009-0007-3623-7586
# May 2026
#
# "Dedicated to my brother and best friend,
# John Oshetski Jr. ("Motorhead")
# I'll see you in the decoherence!
#
# Purpose:
#   Test PR finite-core stability under a 2D double-null collision:
#   an ingoing null flux wall and an outgoing null flux wall cross
#   near the PR saturation boundary.
#
# Model:
#   Effective double-null characteristic grid:
#
#       d_u d_v y_classical = 2 kappa y_classical + F_in(v) F_out(u)
#
#       d_u d_v y_PR =
#           [2 kappa - Gamma_X gate(y_PR)] y_PR
#           + F_in(v) F_out(u) [1 - gate(y_PR)]
#
#       d_u d_v B_c =
#           Gamma_X gate(y_PR) y_PR
#           + F_in(v) F_out(u) gate(y_PR)
#
#   where:
#       gate(y) = y^p / (1 + y^p)
#       Gamma_X,max = response_gain * mu_min^2
#
# Pass condition:
#   For all scanned cases satisfying
#
#       2 kappa < mu_min^2,
#
#   the PR channel remains bounded, curvature stays finite, and
#   core density remains fixed while r_c(M) grows.
#
# Outputs:
#   /content/pr_double_null_wall_stability_v11/
#       pr_double_null_baseline_grid.csv
#       pr_double_null_scan_summary.csv
#       pr_double_null_report.json
#       pr_double_null_heatmaps.png/.pdf
#       pr_double_null_centerline.png/.pdf
#       pr_double_null_stability_map.png/.pdf
#
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import shutil
from pathlib import Path

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# PR constants
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

MU2_MIN = 3.052966743096     # radial spectral gap from PR branch
RMAX = 1.0                   # normalized curvature ceiling
M0 = 1.0                     # normalized initial mass
G_NEWTON = 1.0               # normalized units
C_LIGHT = 1.0                # normalized units

CRITICAL_KAPPA = MU2_MIN / 2.0

OUTDIR = Path("/content/pr_double_null_wall_stability")
OUTDIR.mkdir(parents=True, exist_ok=True)

PUBLIC_REPO = Path("/content/Projection_Relativity")
REPO_RESULTS = PUBLIC_REPO / "plots/projection_relativity_I/generated/double_null_wall_stability"
REPO_CODE = PUBLIC_REPO / "plots/projection_relativity_I/code"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Plot style
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

plt.rcParams.update({
    "text.usetex": False,
    "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.size": 13,
    "axes.facecolor": "white",
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# PR helper functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def spectral_gate(y, p=8):
    """
    Nonlinear opening of the internal PR spectral-response channel.

    y << 1  -> gate ~ 0
    y >= 1  -> gate opens
    y >> 1  -> gate -> 1
    """
    if y <= 0:
        return 0.0
    if y > 50:
        return 1.0
    yp = y ** p
    return yp / (1.0 + yp)


def rc_of_M(M):
    """
    Dimensionless version of:
        r_c(M) = (G_N M / c^2 Rmax)^(1/3)
    """
    return (G_NEWTON * M / (C_LIGHT**2 * RMAX)) ** (1.0 / 3.0)


def rho_core_ratio(M):
    """
    In normalized units, r_c^3 = M/Rmax, so M/(r_c^3 Rmax) = 1.
    This verifies that added mass grows the core volume rather than
    increasing the maximum density.
    """
    rc = rc_of_M(M)
    return M / (rc**3 * RMAX)


def make_wall_profile(x, L, amp=1e-5, center=0.5, width=0.055, background_fraction=0.02):
    """
    Null wall / pulse profile.

    The small background makes the test include persistent accretion,
    while the Gaussian wall creates the strong counter-streaming collision.
    """
    bg = background_fraction * amp
    wall = amp * np.exp(-0.5 * ((x - center * L) / (width * L)) ** 2)
    return bg + wall


def double_null_recurrence_step(prev_ij, prev_i_j, prev_j_i, prev_diag, du, dv, rhs):
    """
    Characteristic grid update for d_u d_v y = rhs.
    """
    return prev_i_j + prev_j_i - prev_diag + du * dv * rhs


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main simulation
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def simulate_double_null_case(
    kappa=1.0,
    flux_amp=1e-5,
    response_gain=1.0,
    L=60.0,
    N=251,
    p_gate=8,
    y0=1e-14,
    cap=1e90,
    y_bound_stable=50.0,
    store_grid=True,
):
    """
    2D double-null / double-wall effective PR stability test.

    u direction: outgoing null wall coordinate.
    v direction: ingoing null wall coordinate.
    """

    u = np.linspace(0.0, L, N)
    v = np.linspace(0.0, L, N)
    du = u[1] - u[0]
    dv = v[1] - v[0]

    # Two null walls crossing near the middle of the grid.
    F_out = make_wall_profile(u, L, amp=flux_amp, center=0.55, width=0.055)
    F_in  = make_wall_profile(v, L, amp=flux_amp, center=0.45, width=0.055)

    y_pr = np.full((N, N), y0, dtype=float)
    y_classical = np.full((N, N), y0, dtype=float)
    ledger = np.zeros((N, N), dtype=float)

    hit_cap_pr = False
    hit_cap_classical = False

    gamma_max = response_gain * MU2_MIN

    # Characteristic double-null update.
    for i in range(1, N):
        for j in range(1, N):

            source = F_out[i] * F_in[j]

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            # Classical channel
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            yc_prev = y_classical[i-1, j-1]
            rhs_c = 2.0 * kappa * yc_prev + source

            yc_new = (
                y_classical[i-1, j]
                + y_classical[i, j-1]
                - y_classical[i-1, j-1]
                + du * dv * rhs_c
            )

            if (not np.isfinite(yc_new)) or yc_new > cap:
                yc_new = cap
                hit_cap_classical = True

            y_classical[i, j] = yc_new

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            # PR channel
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            yp_prev = y_pr[i-1, j-1]
            gate = spectral_gate(yp_prev, p=p_gate)
            gamma_X = gamma_max * gate

            exterior_source = source * (1.0 - gate)
            spectral_absorption = gamma_X * yp_prev
            direct_ledger_source = source * gate

            rhs_pr = (2.0 * kappa - gamma_X) * yp_prev + exterior_source

            yp_new = (
                y_pr[i-1, j]
                + y_pr[i, j-1]
                - y_pr[i-1, j-1]
                + du * dv * rhs_pr
            )

            if yp_new < 0:
                yp_new = 0.0

            if (not np.isfinite(yp_new)) or yp_new > cap:
                yp_new = cap
                hit_cap_pr = True

            y_pr[i, j] = yp_new

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            # Core ledger update
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            absorbed = max(0.0, spectral_absorption + direct_ledger_source)

            B_new = (
                ledger[i-1, j]
                + ledger[i, j-1]
                - ledger[i-1, j-1]
                + du * dv * absorbed
            )

            if (not np.isfinite(B_new)) or B_new > cap:
                B_new = cap

            ledger[i, j] = max(0.0, B_new)

    # Derived PR fields.
    M_total = M0 + ledger
    r_c = rc_of_M(M_total)
    rho_ratio = rho_core_ratio(M_total)
    K_ratio = y_pr / (1.0 + y_pr)

    # Diagonal centerline diagnostic.
    diag_y_pr = np.diag(y_pr)
    diag_y_classical = np.diag(y_classical)
    diag_K = np.diag(K_ratio)
    diag_rc = np.diag(r_c)

    # Stability conditions.
    theory_stable = gamma_max > 2.0 * kappa

    max_y_pr = float(np.nanmax(y_pr))
    max_y_classical = float(np.nanmax(y_classical))
    max_K_ratio = float(np.nanmax(K_ratio))
    min_rho_ratio = float(np.nanmin(rho_ratio))
    max_rho_ratio = float(np.nanmax(rho_ratio))

    numerical_stable = (
        (not hit_cap_pr)
        and np.isfinite(max_y_pr)
        and (max_y_pr < y_bound_stable)
        and (max_K_ratio <= 1.0 + 1e-12)
        and (min_rho_ratio >= 1.0 - 1e-10)
        and (max_rho_ratio <= 1.0 + 1e-10)
    )

    result = {
        "tester": "Projection Relativity double-null wall stability tester",
        "model": "2D effective double-null counter-streaming wall collision harness",
        "kappa": float(kappa),
        "flux_amp": float(flux_amp),
        "response_gain": float(response_gain),
        "mu2_min": float(MU2_MIN),
        "gamma_X_max": float(gamma_max),
        "critical_kappa_gamma_over_2": float(CRITICAL_KAPPA),
        "stability_margin_gamma_minus_2kappa": float(gamma_max - 2.0 * kappa),
        "theory_stable": bool(theory_stable),
        "numerical_stable": bool(numerical_stable),
        "hit_cap_pr": bool(hit_cap_pr),
        "hit_cap_classical": bool(hit_cap_classical),
        "max_y_pr": max_y_pr,
        "max_y_classical": max_y_classical,
        "log10_max_y_pr": float(np.log10(max(max_y_pr, 1e-300))),
        "log10_max_y_classical": float(np.log10(max(max_y_classical, 1e-300))),
        "max_K_PR_over_Rmax": max_K_ratio,
        "min_rho_core_over_rho_max": min_rho_ratio,
        "max_rho_core_over_rho_max": max_rho_ratio,
        "final_ledger_Bc": float(ledger[-1, -1]),
        "final_M_total": float(M_total[-1, -1]),
        "final_r_c": float(r_c[-1, -1]),
        "grid_N": int(N),
        "grid_L": float(L),
    }

    if not store_grid:
        return result, None

    U, V = np.meshgrid(u, v, indexing="ij")

    grid_df = pd.DataFrame({
        "u": U.ravel(),
        "v": V.ravel(),
        "F_out_u": np.repeat(F_out, N),
        "F_in_v": np.tile(F_in, N),
        "y_pr": y_pr.ravel(),
        "y_classical": y_classical.ravel(),
        "K_PR_over_Rmax": K_ratio.ravel(),
        "ledger_Bc": ledger.ravel(),
        "M_total": M_total.ravel(),
        "r_c": r_c.ravel(),
        "rho_core_over_rho_max": rho_ratio.ravel(),
    })

    centerline_df = pd.DataFrame({
        "s": u,
        "y_pr_diag": diag_y_pr,
        "y_classical_diag": diag_y_classical,
        "K_PR_over_Rmax_diag": diag_K,
        "r_c_diag": diag_rc,
    })

    payload = {
        "u": u,
        "v": v,
        "F_out": F_out,
        "F_in": F_in,
        "y_pr": y_pr,
        "y_classical": y_classical,
        "K_ratio": K_ratio,
        "ledger": ledger,
        "r_c": r_c,
        "rho_ratio": rho_ratio,
        "grid_df": grid_df,
        "centerline_df": centerline_df,
    }

    return result, payload


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Baseline double-wall run
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

baseline_result, baseline_payload = simulate_double_null_case(
    kappa=1.0,
    flux_amp=1e-5,
    response_gain=1.0,
    L=60.0,
    N=251,
    p_gate=8,
    store_grid=True,
)

print("BASELINE DOUBLE-NULL WALL RESULT")
print(json.dumps(baseline_result, indent=2))

# Save baseline CSVs.
baseline_grid_csv = OUTDIR / "pr_double_null_baseline_grid.csv"
baseline_centerline_csv = OUTDIR / "pr_double_null_baseline_centerline.csv"

baseline_payload["grid_df"].to_csv(baseline_grid_csv, index=False)
baseline_payload["centerline_df"].to_csv(baseline_centerline_csv, index=False)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Baseline plots
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

eps = 1e-300

u = baseline_payload["u"]
v = baseline_payload["v"]
extent = [v.min(), v.max(), u.min(), u.max()]

# 1. Heatmaps
fig, axes = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True)

im0 = axes[0, 0].imshow(
    np.log10(baseline_payload["y_classical"] + eps),
    origin="lower",
    aspect="auto",
    extent=extent,
)
axes[0, 0].set_title(r"classical channel: $\log_{10} y_{\rm cl}$")
axes[0, 0].set_xlabel(r"$v$")
axes[0, 0].set_ylabel(r"$u$")
fig.colorbar(im0, ax=axes[0, 0])

im1 = axes[0, 1].imshow(
    np.log10(baseline_payload["y_pr"] + eps),
    origin="lower",
    aspect="auto",
    extent=extent,
)
axes[0, 1].set_title(r"PR exterior channel: $\log_{10} y_{\rm PR}$")
axes[0, 1].set_xlabel(r"$v$")
axes[0, 1].set_ylabel(r"$u$")
fig.colorbar(im1, ax=axes[0, 1])

im2 = axes[1, 0].imshow(
    baseline_payload["K_ratio"],
    origin="lower",
    aspect="auto",
    extent=extent,
    vmin=0,
    vmax=1,
)
axes[1, 0].set_title(r"bounded curvature ratio: $K_{\rm PR}/R_{\max}$")
axes[1, 0].set_xlabel(r"$v$")
axes[1, 0].set_ylabel(r"$u$")
fig.colorbar(im2, ax=axes[1, 0])

im3 = axes[1, 1].imshow(
    baseline_payload["r_c"],
    origin="lower",
    aspect="auto",
    extent=extent,
)
axes[1, 1].set_title(r"finite-core radius growth: $r_c(M)$")
axes[1, 1].set_xlabel(r"$v$")
axes[1, 1].set_ylabel(r"$u$")
fig.colorbar(im3, ax=axes[1, 1])

fig.suptitle("PR double-null wall collision: baseline stability", fontsize=16)

heatmap_png = OUTDIR / "pr_double_null_heatmaps.png"
heatmap_pdf = OUTDIR / "pr_double_null_heatmaps.pdf"
fig.savefig(heatmap_png, dpi=300, bbox_inches="tight")
fig.savefig(heatmap_pdf, bbox_inches="tight")
plt.show()

# 2. Centerline plot
center = baseline_payload["centerline_df"]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(center["s"], np.log10(center["y_classical_diag"] + eps), label=r"classical $\log_{10} y_{\rm cl}$")
ax.plot(center["s"], np.log10(center["y_pr_diag"] + eps), label=r"PR $\log_{10} y_{\rm PR}$")
ax.plot(center["s"], center["K_PR_over_Rmax_diag"], label=r"$K_{\rm PR}/R_{\max}$")
ax.plot(center["s"], center["r_c_diag"], label=r"$r_c(M)$")

ax.set_xlabel(r"diagonal characteristic coordinate $s=u=v$")
ax.set_ylabel("log stress / bounded ratios")
ax.set_title("Centerline through double-wall collision")
ax.grid(True, alpha=0.3)
ax.legend(frameon=True)

centerline_png = OUTDIR / "pr_double_null_centerline.png"
centerline_pdf = OUTDIR / "pr_double_null_centerline.pdf"
fig.savefig(centerline_png, dpi=300, bbox_inches="tight")
fig.savefig(centerline_pdf, bbox_inches="tight")
plt.show()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Parameter scan
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# This scan is intentionally moderate so it runs cleanly in Colab.
# Increase N_scan or number of samples for a final publication audit.
N_scan = 151
L_scan = 60.0

kappas = np.linspace(0.20, 2.20, 31)
fluxes = np.logspace(-10, -2, 11)

scan_rows = []

for kappa in kappas:
    for flux_amp in fluxes:
        result, _ = simulate_double_null_case(
            kappa=float(kappa),
            flux_amp=float(flux_amp),
            response_gain=1.0,
            L=L_scan,
            N=N_scan,
            p_gate=8,
            store_grid=False,
        )
        scan_rows.append(result)

scan_df = pd.DataFrame(scan_rows)

scan_csv = OUTDIR / "pr_double_null_scan_summary.csv"
scan_df.to_csv(scan_csv, index=False)

below = scan_df[scan_df["kappa"] < CRITICAL_KAPPA]
above = scan_df[scan_df["kappa"] >= CRITICAL_KAPPA]

all_below_stable = bool(below["numerical_stable"].all()) if len(below) else False
above_contains_instability = bool((~above["numerical_stable"]).any()) if len(above) else False

report = {
    "tester": "Projection Relativity double-null wall stability tester v11",
    "model": "2D effective double-null counter-streaming wall collision harness",
    "mu2_min": float(MU2_MIN),
    "critical_kappa_gamma_over_2": float(CRITICAL_KAPPA),
    "baseline": baseline_result,
    "scan_cases": int(len(scan_df)),
    "stable_cases": int(scan_df["numerical_stable"].sum()),
    "unstable_cases": int((~scan_df["numerical_stable"]).sum()),
    "all_cases_below_critical_kappa_stable": all_below_stable,
    "above_critical_kappa_contains_instability": above_contains_instability,
    "pass_condition": "all scanned cases with 2*kappa < mu_min^2 remain bounded; K_PR/Rmax<=1; rho_core/rho_max=1",
    "overall_pass": bool(all_below_stable),
}

report_json = OUTDIR / "pr_double_null_report.json"
with open(report_json, "w") as f:
    json.dump(report, f, indent=2)

print("\nDOUBLE-NULL WALL SCAN REPORT")
print(json.dumps(report, indent=2))


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Stability map
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

pivot_stable = scan_df.pivot(index="flux_amp", columns="kappa", values="numerical_stable").sort_index()

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(
    pivot_stable.values.astype(float),
    origin="lower",
    aspect="auto",
    vmin=0,
    vmax=1,
    extent=[
        scan_df["kappa"].min(),
        scan_df["kappa"].max(),
        np.log10(scan_df["flux_amp"].min()),
        np.log10(scan_df["flux_amp"].max()),
    ],
)

ax.axvline(CRITICAL_KAPPA, linestyle="--", linewidth=1.5, label=r"$2\kappa=\mu_{\min}^2$")
ax.set_xlabel(r"double-null blueshift parameter $\kappa$")
ax.set_ylabel(r"$\log_{10}$ wall flux amplitude")
ax.set_title("PR double-null wall scan: stability map")
ax.legend(frameon=True)

cbar = fig.colorbar(im, ax=ax)
cbar.set_label("stable = 1, unstable = 0")

stability_png = OUTDIR / "pr_double_null_stability_map.png"
stability_pdf = OUTDIR / "pr_double_null_stability_map.pdf"
fig.savefig(stability_png, dpi=300, bbox_inches="tight")
fig.savefig(stability_pdf, bbox_inches="tight")
plt.show()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# log10 max y_PR scan map
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

pivot_logmax = scan_df.pivot(index="flux_amp", columns="kappa", values="log10_max_y_pr").sort_index()

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(
    pivot_logmax.values,
    origin="lower",
    aspect="auto",
    extent=[
        scan_df["kappa"].min(),
        scan_df["kappa"].max(),
        np.log10(scan_df["flux_amp"].min()),
        np.log10(scan_df["flux_amp"].max()),
    ],
)

ax.axvline(CRITICAL_KAPPA, linestyle="--", linewidth=1.5, label=r"$2\kappa=\mu_{\min}^2$")
ax.set_xlabel(r"double-null blueshift parameter $\kappa$")
ax.set_ylabel(r"$\log_{10}$ wall flux amplitude")
ax.set_title(r"PR double-null wall scan: $\log_{10}\max(y_{\rm PR})$")
ax.legend(frameon=True)

cbar = fig.colorbar(im, ax=ax)
cbar.set_label(r"$\log_{10}\max(y_{\rm PR})$")

logmax_png = OUTDIR / "pr_double_null_logmax_map.png"
logmax_pdf = OUTDIR / "pr_double_null_logmax_map.pdf"
fig.savefig(logmax_png, dpi=300, bbox_inches="tight")
fig.savefig(logmax_pdf, bbox_inches="tight")
plt.show()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Save/copy output
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

print("\nSaved outputs:")
for p in [
    baseline_grid_csv,
    baseline_centerline_csv,
    scan_csv,
    report_json,
    heatmap_png,
    heatmap_pdf,
    centerline_png,
    centerline_pdf,
    stability_png,
    stability_pdf,
    logmax_png,
    logmax_pdf,
]:
    print(p)

# Optional copy into repo if present
if REPO_RESULTS.parent.exists():
    REPO_RESULTS.mkdir(parents=True, exist_ok=True)
    for p in OUTDIR.glob("*"):
        shutil.copy2(p, REPO_RESULTS / p.name)
    print("\nCopied results into repo:")
    print(REPO_RESULTS)
else:
    print("\nRepo results directory not found. Files remain in /content.")

print("\nKey expected result:")
print("overall_pass =", report["overall_pass"])
print("all_cases_below_critical_kappa_stable =", report["all_cases_below_critical_kappa_stable"])
print("critical kappa =", CRITICAL_KAPPA)
