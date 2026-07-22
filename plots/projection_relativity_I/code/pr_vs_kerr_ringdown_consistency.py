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
# Projection Relativity Full Validation Harness
# Michael Stanislaus Oshetski
# ORCID# 0009-0007-3623-7586
# May 2026
#
# "Dedicated to my brother and best friend,
# John Oshetski Jr. ("Motorhead")
# I'll see you in the decoherence!
#
# What this script does:
#   1. Generates the PR vs Kerr ringdown consistency plot
#
# Generates:
# png_path = outdir / "pr_vs_kerr_ringdown_consistency.png"
# pdf_path = outdir / "pr_vs_kerr_ringdown_consistency.pdf"
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# PR vs Kerr ringdown consistency plot
# Clean Colab cell for Section 11
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 1) Output folder
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
outdir = Path("results/pr_ringdown_kerr_consistency")
outdir.mkdir(parents=True, exist_ok=True)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 2) Kerr-like ringdown inputs
#    Illustrative GW150914-like values. These are visualization inputs,
#    not fit parameters and not observational claims.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
f_kerr = 250.0          # Hz
tau_kerr = 4.2e-3       # s
phi0 = 0.35 * np.pi     # phase
t_max = 0.030           # 30 ms window
npts = 4000

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 3) PR gap-suppression inputs
#    eta is the gap ratio, not the direct waveform correction.
#    The plotted PR residual uses the formal suppression bound.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
mu_min_sq = 3.052966743096

# characteristic dimensionless mode scale from the paper
omega_R_hat = 0.263780
omega_I_hat = 0.053234
omega_hat_sq = omega_R_hat**2 + omega_I_hat**2
eta = omega_hat_sq / mu_min_sq

# Projection-sector suppression factors used in the GW bound.
# C_kerr is left explicit; C_kerr = 1 is the fiducial plot value.
M2_response = 0.25
eps_X_GW = 0.03
C_kerr = 1.0

formal_residual_bound = (
    C_kerr
    * eta
    / ((1.0 + M2_response) * (1.0 - eta))
    * eps_X_GW
)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 4) Time axis
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t = np.linspace(0.0, t_max, npts)
t_ms = 1e3 * t

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 5) Kerr waveform
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
h_kerr_raw = np.exp(-t / tau_kerr) * np.cos(2.0 * np.pi * f_kerr * t + phi0)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 6) PR response
#    A_obs = A_Kerr + A_X, with A_X bounded by the gap-suppressed
#    projection-sector residual. This avoids visually implying that
#    eta itself is the waveform correction.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
residual_envelope = formal_residual_bound * np.exp(-t / tau_kerr)
response_factor = 1.0 + residual_envelope
h_pr_raw = response_factor * h_kerr_raw

# Normalize both to Kerr peak so the overlay is easy to read.
norm = np.max(np.abs(h_kerr_raw))
h_kerr = h_kerr_raw / norm
h_pr = h_pr_raw / norm

delta_h = h_pr - h_kerr
percent_response = 100.0 * residual_envelope

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 7) Plot
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "legend.fontsize": 11,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
})

fig, axes = plt.subplots(
    2, 1,
    figsize=(10, 8),
    sharex=True,
    gridspec_kw={"height_ratios": [2.2, 1.2]}
)

ax1, ax2 = axes

# ---- top panel: waveform overlay ----
ax1.plot(t_ms, h_kerr, "k--", lw=2.3, label="Kerr ringdown")
ax1.plot(t_ms, h_pr, color="tab:blue", lw=2.0, label="PR response")

ax1.set_ylabel("normalized strain")
ax1.set_title("Projection Relativity reproduces the leading Kerr ringdown response")
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper right", frameon=True)

textbox = (
    r"$A_{\rm obs}=A_{\rm Kerr}+A_X$" + "\n" +
    r"$\eta=\hat{\omega}^2/\mu_{\min}^2$" + "\n" +
    rf"$\mu_{{\min}}^2={mu_min_sq:.6f}$" + "\n" +
    rf"$\hat{{\omega}}^2={omega_hat_sq:.6f}$" + "\n" +
    rf"$\eta={eta:.5f}$ gap ratio" + "\n" +
    rf"$\|A_X\|/\|A_{{\rm Kerr}}\|\lesssim {formal_residual_bound:.3e}$" + "\n" +
    rf"peak residual bound = {100.0 * formal_residual_bound:.4f}\%"
)

# Put the information box away from the legend.
ax1.text(
    0.65, 0.5, textbox,
    transform=ax1.transAxes,
    ha="left",
    va="top",
    bbox=dict(
        boxstyle="round,pad=0.40",
        facecolor="white",
        edgecolor="0.70",
        alpha=0.96,
    ),
    fontsize=10.5,
)

# ---- bottom panel: magnified residual and residual bound ----
# The residual is multiplied by 10^4 so the small Kerr-consistent difference is visible.
ax2.plot(
    t_ms,
    1e4 * delta_h,
    color="tab:red",
    lw=2.0,
    label=r"$10^4\times(h_{\rm PR}-h_{\rm Kerr})$",
)
ax2.axhline(0.0, color="0.5", lw=1.0)

ax2b = ax2.twinx()
ax2b.plot(
    t_ms,
    percent_response,
    color="0.35",
    ls="--",
    lw=2.0,
    label=r"formal residual bound [\%]",
)

ax2.set_xlabel("time after ringdown start [ms]")
ax2.set_ylabel(r"$10^4\times\Delta h$")
ax2b.set_ylabel("residual bound [%]")
ax2.grid(True, alpha=0.3)

lines1, labels1 = ax2.get_legend_handles_labels()
lines2, labels2 = ax2b.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc="upper right", frameon=True)

ax2.set_xlim(0.0, t_max * 1e3)

fig.tight_layout()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 8) Save
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
png_path = outdir / "pr_vs_kerr_ringdown_consistency.png"
pdf_path = outdir / "pr_vs_kerr_ringdown_consistency.pdf"

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")

plt.show()

print("Saved:")
print(" -", png_path)
print(" -", pdf_path)
print()
print(f"mu_min^2 = {mu_min_sq:.12f}")
print(f"omega_hat^2 = {omega_hat_sq:.12f}")
print(f"eta gap ratio = {eta:.8f}")
print(f"M2_response = {M2_response:.6f}")
print(f"eps_X_GW = {eps_X_GW:.6f}")
print(f"C_kerr = {C_kerr:.6f}")
print(f"formal peak residual bound = {formal_residual_bound:.10e}")
print(f"formal peak residual bound percent = {100.0 * formal_residual_bound:.6f}%")
