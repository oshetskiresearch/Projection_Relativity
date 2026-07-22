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
# Projection Relativity Mass-Inflation Stability Tester
# Nonlinear counter-streaming null-flux effective harness
#
# Purpose:
#   Test whether PR finite-core saturation remains bounded under
#   Poisson-Israel-type counter-streaming ingoing/outgoing flux.
#
# Output:
#   /content/pr_mass_inflation_stability/
#       pr_mass_inflation_single_case.png
#       pr_mass_inflation_scan_logmax.png
#       pr_mass_inflation_scan_stability.png
#       pr_mass_inflation_scan_summary.csv
#       pr_mass_inflation_single_case.csv
#       pr_mass_inflation_report.json
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import shutil
from pathlib import Path

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Constants from PR radial branch
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

MU2_MIN = 3.052966743096  # radial spectral gap
RMAX = 1.0                # dimensionless curvature ceiling
M0 = 1.0                  # normalized initial mass
C_LIGHT = 1.0             # normalized units
G_NEWTON = 1.0            # normalized units

OUTDIR = Path("/content/pr_mass_inflation_stability")
OUTDIR.mkdir(parents=True, exist_ok=True)

PUBLIC_REPO = Path("/content/Projection_Relativity")
REPO_RESULTS = PUBLIC_REPO / "plots/projection_relativity_I/generated/mass_inflation_stability"
REPO_CODE = PUBLIC_REPO / "plots/projection_relativity_I/code"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Plot formatting
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

plt.rcParams.update({
    "text.usetex": False,
    "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.size": 13,
    "axes.facecolor": "white",
    "figure.facecolor": "white",
})

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Core model
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def spectral_gate(y, p=8):
    """
    Nonlinear opening of the internal PR spectral-response channel.

    y is the exterior attempted stress/curvature ratio.
    gate -> 0 below saturation
    gate -> 1 near/above saturation
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
        r_c(M) = (G M / c^2 Rmax)^(1/3)
    with G=c=Rmax=1.
    """
    return (G_NEWTON * M / (C_LIGHT**2 * RMAX)) ** (1.0 / 3.0)


def rho_core_ratio(M):
    """
    Since r_c^3 = M/Rmax in normalized units,
    M/r_c^3 remains equal to Rmax.
    This ratio should remain 1.
    """
    rc = rc_of_M(M)
    return M / (rc**3 * RMAX)


def simulate_case(
    kappa=1.0,
    flux_amp=1e-6,
    response_gain=1.0,
    tau_end=60.0,
    dt=0.01,
    p_gate=8,
    y0=1e-14,
    cap=1e80,
    store=True,
):
    """
    Effective nonlinear mass-inflation stress test.

    Classical channel:
        dy/dtau = 2 kappa y + source

    PR channel:
        dy/dtau =
            2 kappa y
            + source * (1 - gate)
            - Gamma_X(gate) * y

        dB_c/dtau =
            source * gate
            + Gamma_X(gate) * y

    where:
        gate = y^p/(1+y^p)
        Gamma_X = response_gain * mu_min^2 * gate

    Interpretation:
        - y is the exterior projected stress/curvature attempt.
        - gate opens the internal spectral-response channel near saturation.
        - absorbed energy updates the finite-core ledger B_c.
        - total mass M increases, so r_c(M) increases.
        - rho_core remains bounded by construction through r_c(M).
    """

    n_steps = int(np.ceil(tau_end / dt)) + 1

    y_pr = float(y0)
    y_classical = float(y0)
    ledger = 0.0
    M = M0

    max_y_pr = y_pr
    max_y_classical = y_classical
    max_K_ratio = 0.0
    min_rho_ratio = np.inf
    max_rho_ratio = 0.0
    hit_cap_pr = False
    hit_cap_classical = False

    tail_start = int(0.80 * n_steps)
    tail_first_y = None
    tail_last_y = None

    rows = []

    for i in range(n_steps):
        tau = i * dt

        # Counter-streaming flux source.
        # Tiny persistent flux plus a finite burst, so we test both background
        # accretion and impulsive infall.
        burst = 1.0 + 9.0 * np.exp(-0.5 * ((tau - 0.35 * tau_end) / (0.08 * tau_end)) ** 2)
        source = (flux_amp ** 2) * burst

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Classical mass inflation proxy
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        dy_classical = 2.0 * kappa * y_classical + source
        y_classical = y_classical + dt * dy_classical

        if (not np.isfinite(y_classical)) or y_classical > cap:
            y_classical = cap
            hit_cap_classical = True

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # PR spectral-response channel
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        gate = spectral_gate(y_pr, p=p_gate)
        gamma_X = response_gain * MU2_MIN * gate

        exterior_source = source * (1.0 - gate)
        direct_ledger_source = source * gate
        spectral_absorption = gamma_X * y_pr

        dy_pr = 2.0 * kappa * y_pr + exterior_source - spectral_absorption
        y_pr = y_pr + dt * dy_pr

        if y_pr < 0:
            y_pr = 0.0

        if (not np.isfinite(y_pr)) or y_pr > cap:
            y_pr = cap
            hit_cap_pr = True

        # Core ledger and radius update
        absorbed = max(0.0, direct_ledger_source + spectral_absorption)
        ledger += dt * absorbed
        M = M0 + ledger
        rc = rc_of_M(M)
        rho_ratio = rho_core_ratio(M)

        # Projected curvature ratio.
        # Saturating map: K_PR/Rmax remains below 1 even when attempted
        # exterior stress grows.
        K_ratio = y_pr / (1.0 + y_pr)

        max_y_pr = max(max_y_pr, y_pr)
        max_y_classical = max(max_y_classical, y_classical)
        max_K_ratio = max(max_K_ratio, K_ratio)
        min_rho_ratio = min(min_rho_ratio, rho_ratio)
        max_rho_ratio = max(max_rho_ratio, rho_ratio)

        if i == tail_start:
            tail_first_y = max(y_pr, 1e-300)
        if i == n_steps - 1:
            tail_last_y = max(y_pr, 1e-300)

        if store and (i % max(1, int(0.05 / dt)) == 0 or i == n_steps - 1):
            rows.append({
                "tau": tau,
                "source": source,
                "gate": gate,
                "gamma_X": gamma_X,
                "y_pr": y_pr,
                "y_classical": y_classical,
                "K_PR_over_Rmax": K_ratio,
                "ledger_Bc": ledger,
                "M_total": M,
                "r_c": rc,
                "rho_core_over_rho_max": rho_ratio,
            })

    # Tail growth diagnostic
    if tail_first_y is None:
        tail_first_y = max(y_pr, 1e-300)
    if tail_last_y is None:
        tail_last_y = max(y_pr, 1e-300)

    tail_duration = max(dt, tau_end * 0.20)
    tail_log_slope = (np.log(tail_last_y) - np.log(tail_first_y)) / tail_duration

    theory_stable = (response_gain * MU2_MIN) > (2.0 * kappa)

    # Numerical stability criterion:
    # - no cap hit
    # - projected stress not running away in the tail
    # - bounded projected curvature
    # The tail threshold is deliberately conservative.
    runaway_tail = (tail_log_slope > 0.02 and tail_last_y > 1.0)
    numerical_stable = (
        (not hit_cap_pr)
        and (not runaway_tail)
        and np.isfinite(max_y_pr)
        and (max_K_ratio <= 1.0 + 1e-12)
        and (max_rho_ratio <= 1.0 + 1e-10)
        and (min_rho_ratio >= 1.0 - 1e-10)
    )

    result = {
        "kappa": float(kappa),
        "flux_amp": float(flux_amp),
        "response_gain": float(response_gain),
        "mu2_min": float(MU2_MIN),
        "gamma_X_max": float(response_gain * MU2_MIN),
        "stability_margin_gamma_minus_2kappa": float(response_gain * MU2_MIN - 2.0 * kappa),
        "theory_stable": bool(theory_stable),
        "numerical_stable": bool(numerical_stable),
        "hit_cap_pr": bool(hit_cap_pr),
        "hit_cap_classical": bool(hit_cap_classical),
        "tail_log_slope": float(tail_log_slope),
        "max_y_pr": float(max_y_pr),
        "max_y_classical": float(max_y_classical),
        "log10_max_y_pr": float(np.log10(max(max_y_pr, 1e-300))),
        "log10_max_y_classical": float(np.log10(max(max_y_classical, 1e-300))),
        "max_K_PR_over_Rmax": float(max_K_ratio),
        "min_rho_core_over_rho_max": float(min_rho_ratio),
        "max_rho_core_over_rho_max": float(max_rho_ratio),
        "final_y_pr": float(y_pr),
        "final_y_classical": float(y_classical),
        "final_ledger_Bc": float(ledger),
        "final_M_total": float(M),
        "final_r_c": float(rc_of_M(M)),
    }

    if store:
        return result, pd.DataFrame(rows)

    return result, None


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Baseline single run
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

baseline_result, baseline_df = simulate_case(
    kappa=1.0,
    flux_amp=1e-5,
    response_gain=1.0,
    tau_end=60.0,
    dt=0.01,
    p_gate=8,
    store=True,
)

baseline_csv = OUTDIR / "pr_mass_inflation_single_case.csv"
baseline_df.to_csv(baseline_csv, index=False)

print("BASELINE RESULT")
print(json.dumps(baseline_result, indent=2))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Baseline plot
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

fig, ax = plt.subplots(figsize=(10, 6))

eps = 1e-300
ax.plot(baseline_df["tau"], np.log10(baseline_df["y_classical"] + eps), label="classical mass-inflation proxy")
ax.plot(baseline_df["tau"], np.log10(baseline_df["y_pr"] + eps), label="PR exterior projected channel")
ax.plot(baseline_df["tau"], baseline_df["K_PR_over_Rmax"], label=r"$K_{\rm PR}/R_{\max}$")
ax.plot(baseline_df["tau"], baseline_df["r_c"], label=r"$r_c(M)$")

ax.set_xlabel(r"dimensionless time $\tau$")
ax.set_ylabel("log stress / bounded ratios")
ax.set_title("PR mass-inflation stability test: baseline counter-streaming flux")
ax.legend(frameon=True)
ax.grid(True, alpha=0.3)

single_png = OUTDIR / "pr_mass_inflation_single_case.png"
single_pdf = OUTDIR / "pr_mass_inflation_single_case.pdf"
fig.savefig(single_png, dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(single_pdf, bbox_inches="tight", facecolor="white")
plt.show()

print("Saved baseline plot:", single_png)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Parameter scan
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

kappas = np.linspace(0.10, 1.90, 37)
fluxes = np.logspace(-10, -2, 17)

scan_rows = []

for kappa in kappas:
    for flux_amp in fluxes:
        result, _ = simulate_case(
            kappa=float(kappa),
            flux_amp=float(flux_amp),
            response_gain=1.0,
            tau_end=60.0,
            dt=0.01,
            p_gate=8,
            store=False,
        )
        scan_rows.append(result)

scan_df = pd.DataFrame(scan_rows)
scan_csv = OUTDIR / "pr_mass_inflation_scan_summary.csv"
scan_df.to_csv(scan_csv, index=False)

critical_kappa = MU2_MIN / 2.0

below = scan_df[scan_df["kappa"] < critical_kappa]
above = scan_df[scan_df["kappa"] >= critical_kappa]

all_below_stable = bool(below["numerical_stable"].all()) if len(below) else False
any_above_unstable = bool((~above["numerical_stable"]).any()) if len(above) else False

report = {
    "tester": "Projection Relativity mass-inflation stability tester",
    "model": "nonlinear effective counter-streaming null-flux harness",
    "mu2_min": MU2_MIN,
    "response_gain": 1.0,
    "gamma_X_max": MU2_MIN,
    "critical_kappa_gamma_over_2": critical_kappa,
    "baseline": baseline_result,
    "scan_cases": int(len(scan_df)),
    "stable_cases": int(scan_df["numerical_stable"].sum()),
    "unstable_cases": int((~scan_df["numerical_stable"]).sum()),
    "all_cases_below_critical_kappa_stable": all_below_stable,
    "above_critical_kappa_contains_instability": any_above_unstable,
    "pass_condition": "all scanned cases with 2*kappa < mu2_min remain bounded, K_PR/Rmax<=1, rho_core/rho_max=1",
    "overall_pass": bool(all_below_stable),
}

report_json = OUTDIR / "pr_mass_inflation_report.json"
with open(report_json, "w") as f:
    json.dump(report, f, indent=2)

print("\nSCAN REPORT")
print(json.dumps(report, indent=2))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Heatmap: log10 max PR exterior channel
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

pivot_logmax = scan_df.pivot(index="flux_amp", columns="kappa", values="log10_max_y_pr").sort_index()

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(
    pivot_logmax.values,
    aspect="auto",
    origin="lower",
    extent=[
        scan_df["kappa"].min(),
        scan_df["kappa"].max(),
        np.log10(scan_df["flux_amp"].min()),
        np.log10(scan_df["flux_amp"].max()),
    ],
)
ax.axvline(critical_kappa, linestyle="--", linewidth=1.5, label=r"$2\kappa=\mu_{\min}^2$")
ax.set_xlabel(r"inner-horizon blueshift parameter $\kappa$")
ax.set_ylabel(r"$\log_{10}$ flux amplitude")
ax.set_title(r"PR scan: $\log_{10}\max(y_{\rm PR})$")
ax.legend(frameon=True)
cbar = fig.colorbar(im, ax=ax)
cbar.set_label(r"$\log_{10}\max(y_{\rm PR})$")

scan_log_png = OUTDIR / "pr_mass_inflation_scan_logmax.png"
scan_log_pdf = OUTDIR / "pr_mass_inflation_scan_logmax.pdf"
fig.savefig(scan_log_png, dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(scan_log_pdf, bbox_inches="tight", facecolor="white")
plt.show()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Heatmap: numerical stability
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

pivot_stable = scan_df.pivot(index="flux_amp", columns="kappa", values="numerical_stable").sort_index()

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(
    pivot_stable.values.astype(float),
    aspect="auto",
    origin="lower",
    vmin=0,
    vmax=1,
    extent=[
        scan_df["kappa"].min(),
        scan_df["kappa"].max(),
        np.log10(scan_df["flux_amp"].min()),
        np.log10(scan_df["flux_amp"].max()),
    ],
)
ax.axvline(critical_kappa, linestyle="--", linewidth=1.5, label=r"$2\kappa=\mu_{\min}^2$")
ax.set_xlabel(r"inner-horizon blueshift parameter $\kappa$")
ax.set_ylabel(r"$\log_{10}$ flux amplitude")
ax.set_title("PR scan: numerical stability map")
ax.legend(frameon=True)
cbar = fig.colorbar(im, ax=ax)
cbar.set_label("stable = 1, unstable = 0")

scan_stable_png = OUTDIR / "pr_mass_inflation_scan_stability.png"
scan_stable_pdf = OUTDIR / "pr_mass_inflation_scan_stability.pdf"
fig.savefig(scan_stable_png, dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(scan_stable_pdf, bbox_inches="tight", facecolor="white")
plt.show()

print("\nSaved outputs:")
for p in [
    baseline_csv,
    single_png,
    single_pdf,
    scan_csv,
    scan_log_png,
    scan_log_pdf,
    scan_stable_png,
    scan_stable_pdf,
    report_json,
]:
    print(p)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Optional: copy into repo if present
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

if REPO_RESULTS.parent.exists():
    REPO_RESULTS.mkdir(parents=True, exist_ok=True)
    for p in OUTDIR.glob("*"):
        shutil.copy2(p, REPO_RESULTS / p.name)
    print("\nCopied results into repo:", REPO_RESULTS)

if REPO_CODE.parent.exists():
    REPO_CODE.mkdir(parents=True, exist_ok=True)
    print("Repo code directory exists:", REPO_CODE)
    print("You can later save this notebook cell as:")
    print(REPO_CODE / "pr_mass_inflation_stability_tester.py")
