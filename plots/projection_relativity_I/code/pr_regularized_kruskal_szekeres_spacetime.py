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
#
# Covers:
# pr_regularized_kruskal_szekeres_spacetime plot generation
#
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import shutil

plt.rcParams.update({
    "text.usetex": False,
    "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "font.size": 14,
    "axes.facecolor": "white",
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

def plot_regularized_kruskal_pr_clean(save_to_repo=False):
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Setup
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    fig, ax = plt.subplots(figsize=(11, 11))
    xmax = 2.0

    # Colors: mostly black/gray for paper-readiness
    horizon_color = "black"
    core_color = "black"
    grid_color = "#9A9A9A"
    axis_color = "black"

    # Output paths
    out_png = Path("/content/pr_regularized_kruskal_szekeres_spacetime.png")
    out_pdf = Path("/content/pr_regularized_kruskal_szekeres_spacetime.pdf")
    out_svg = Path("/content/pr_regularized_kruskal_szekeres_spacetime.svg")

    repo_fig_dir = Path("/content/Projection_Relativity/plots/projection_relativity_I")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Helper functions
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def label_on_plot(x, y, text, rotation=0, fontsize=13, ha="center", va="center", zorder=20):
        ax.text(
            x, y, text,
            rotation=rotation,
            fontsize=fontsize,
            ha=ha,
            va=va,
            color="black",
            bbox=dict(
                boxstyle="round,pad=0.18",
                facecolor="white",
                edgecolor="none",
                alpha=1.0,
            ),
            zorder=zorder,
        )

    def tangent_angle_top(U, C):
        V = np.sqrt(U**2 + C)
        slope = U / V
        return np.degrees(np.arctan(slope))

    def tangent_angle_bottom(U, C):
        Vabs = np.sqrt(U**2 + C)
        slope = -U / Vabs
        return np.degrees(np.arctan(slope))

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Coordinate convention
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # We use units where the horizon radius 2M is normalized to 1.
    # Classical Schwarzschild interior singularity would be at
    # V^2 - U^2 = 1.
    #
    # PR replaces that singular endpoint by a finite saturation
    # boundary at r = r_c, with 0 < r_c < 2M.
    # In normalized units, rbar_c = r_c/(2M).
    # The interior constant-r hyperbola is:
    # V^2 - U^2 = (1 - rbar_c) exp(rbar_c).
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    rbar_c = 0.70
    C_rc = (1.0 - rbar_c) * np.exp(rbar_c)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 1. Constant t lines
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    slopes = [-0.85, -0.65, -0.45, -0.25, 0.0, 0.25, 0.45, 0.65, 0.85]

    for a in slopes:
        ax.plot(
            [-xmax, xmax],
            [-a * xmax, a * xmax],
            color=grid_color,
            lw=0.9,
            zorder=1,
        )
        ax.plot(
            [-a * xmax, a * xmax],
            [-xmax, xmax],
            color=grid_color,
            lw=0.9,
            zorder=1,
        )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 2. Constant r hyperbolas
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # Exterior regions I and III: U^2 - V^2 = const
    for C in [0.25, 0.50, 0.80, 1.10, 1.45, 1.75]:
        U_pos = np.linspace(C, xmax, 300)
        V_pos = np.sqrt(U_pos**2 - C**2)

        ax.plot(U_pos, V_pos, color=grid_color, lw=0.9, zorder=1)
        ax.plot(U_pos, -V_pos, color=grid_color, lw=0.9, zorder=1)
        ax.plot(-U_pos, V_pos, color=grid_color, lw=0.9, zorder=1)
        ax.plot(-U_pos, -V_pos, color=grid_color, lw=0.9, zorder=1)

    # Interior regions II and IV: V^2 - U^2 = const
    # Only draw interior curves below the saturation core.
    interior_constants = np.linspace(0.12, C_rc * 0.88, 5)

    for C in interior_constants:
        U_top = np.linspace(-np.sqrt(xmax**2 - C), np.sqrt(xmax**2 - C), 300)
        V_top = np.sqrt(U_top**2 + C)

        ax.plot(U_top, V_top, color=grid_color, lw=0.9, zorder=1)
        ax.plot(U_top, -V_top, color=grid_color, lw=0.9, zorder=1)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 3. Event horizons, r = 2M
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # V = U and V = -U
    ax.plot([-xmax, xmax], [-xmax, xmax], color=horizon_color, lw=1.8, zorder=4)
    ax.plot([-xmax, xmax], [xmax, -xmax], color=horizon_color, lw=1.8, zorder=4)

    # Put r=2M labels directly on horizon lines, in black.
    horizon_label_kwargs = dict(fontsize=13, zorder=25)

    label_on_plot(
        -1.02, 1.02,
        r"$r=2M$",
        rotation=-45,
        **horizon_label_kwargs
    )
    label_on_plot(
        1.02, 1.02,
        r"$r=2M$",
        rotation=45,
        **horizon_label_kwargs
    )
    label_on_plot(
        -1.02, -1.02,
        r"$r=2M$",
        rotation=45,
        **horizon_label_kwargs
    )
    label_on_plot(
        1.02, -1.02,
        r"$r=2M$",
        rotation=-45,
        **horizon_label_kwargs
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 4. PR finite saturation core
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    U_core = np.linspace(-np.sqrt(xmax**2 - C_rc), np.sqrt(xmax**2 - C_rc), 600)
    V_core = np.sqrt(U_core**2 + C_rc)

    # Erase unphysical classical singularity zones.
    # This keeps the plot white and explicitly removes the GR r=0 region.
    ax.fill_between(U_core, V_core, xmax + 0.5, color="white", zorder=5)
    ax.fill_between(U_core, -xmax - 0.5, -V_core, color="white", zorder=5)

    # Draw saturated finite-core boundaries.
    ax.plot(
        U_core, V_core,
        color=core_color,
        lw=4.0,
        solid_capstyle="round",
        zorder=7,
    )
    ax.plot(
        U_core, -V_core,
        color=core_color,
        lw=4.0,
        solid_capstyle="round",
        zorder=7,
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 5. Labels on the saturation lines
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # Upper-left core label placed directly on the saturation line.
    U_lbl_top = -1.20
    V_lbl_top = np.sqrt(U_lbl_top**2 + C_rc)
    rot_top = tangent_angle_top(U_lbl_top, C_rc)

    label_on_plot(
        U_lbl_top,
        V_lbl_top,
        r"Saturated spectral core  $(r=r_c)$",
        rotation=rot_top,
        fontsize=13,
        zorder=30,
    )

    # Lower-left curvature/gap label placed directly on the lower saturation line.
    U_lbl_bot = -1.10
    V_lbl_bot = -np.sqrt(U_lbl_bot**2 + C_rc)
    rot_bot = tangent_angle_bottom(U_lbl_bot, C_rc)

    label_on_plot(
        U_lbl_bot,
        V_lbl_bot,
        r"$\mu_{\min}^2>0\Rightarrow R_{\max}<\infty,\quad K_{\rm PR}<\infty$",
        rotation=rot_bot,
        fontsize=12,
        zorder=30,
    )

    # Formula label, kept away from axes and curves.
    label_on_plot(
        1.15,
        1.85,
        r"$r_c=\left(\dfrac{G_NM}{c^2R_{\max}}\right)^{1/3}$",
        rotation=0,
        fontsize=15,
        zorder=30,
    )

    # Optional small explanatory label in the erased white region.
    label_on_plot(
        0.0,
        1.84,
        r"no $r=0$ singular boundary",
        rotation=0,
        fontsize=12,
        zorder=30,
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 6. Axes
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ax.annotate(
        "",
        xy=(xmax + 0.22, 0),
        xytext=(-xmax - 0.22, 0),
        arrowprops=dict(arrowstyle="->", lw=1.4, color=axis_color),
        zorder=10,
    )
    ax.annotate(
        "",
        xy=(0, xmax + 0.22),
        xytext=(0, -xmax - 0.22),
        arrowprops=dict(arrowstyle="->", lw=1.4, color=axis_color),
        zorder=10,
    )

    ax.text(
        xmax + 0.27, 0,
        r"$U$",
        fontsize=22,
        va="center",
        ha="left",
        zorder=20,
    )
    ax.text(
        0, xmax + 0.27,
        r"$V$",
        fontsize=22,
        ha="center",
        va="bottom",
        zorder=20,
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 7. Region labels
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Slightly off the axes so they do not overwrite the axis lines.
    ax.text(1.46, 0.12, "I", fontsize=20, ha="center", va="center", zorder=20)
    ax.text(-1.46, 0.12, "III", fontsize=20, ha="center", va="center", zorder=20)
    ax.text(0.00, 0.36, "II", fontsize=20, ha="center", va="center", zorder=20)
    ax.text(0.00, -0.36, "IV", fontsize=20, ha="center", va="center", zorder=20)

    # Optional constant-line labels, positioned near edges and not over axes.
    label_on_plot(
        1.74,
        1.08,
        r"$t=\mathrm{constant}$",
        rotation=32,
        fontsize=11,
        zorder=22,
    )
    label_on_plot(
        1.65,
        -1.28,
        r"$r=\mathrm{constant}$",
        rotation=-22,
        fontsize=11,
        zorder=22,
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 8. Title and formatting
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ax.set_title(
        "Projection Relativity: Regularized Kruskal--Szekeres Spacetime",
        fontsize=16,
        pad=20,
    )

    ax.set_xlim(-xmax - 0.32, xmax + 0.32)
    ax.set_ylim(-xmax - 0.32, xmax + 0.32)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 9. Save
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    plt.savefig(out_png, dpi=400, bbox_inches="tight", facecolor="white")
    plt.savefig(out_pdf, bbox_inches="tight", facecolor="white")
    plt.savefig(out_svg, bbox_inches="tight", facecolor="white")
    plt.show()

    print("Saved:")
    print(out_png)
    print(out_pdf)
    print(out_svg)

    # Optional copy into repo
    if save_to_repo and repo_fig_dir.exists():
        repo_fig_dir.mkdir(parents=True, exist_ok=True)
        for p in [out_png, out_pdf, out_svg]:
            shutil.copy2(p, repo_fig_dir / p.name)
            print("Copied to repo:", repo_fig_dir / p.name)
    else:
        print("Repo figure directory not found or save_to_repo=False. Files remain in /content.")

if __name__ == "__main__":
    plot_regularized_kruskal_pr_clean(save_to_repo=True)
