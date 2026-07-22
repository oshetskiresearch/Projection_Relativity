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
#   1. Searches automatically for branch_residual_scan.csv.
#   2. Generates a 2D residual heatmap.
#   3. Generates a black-and-white 1D branch plot along the a2 = 1 slice.
#   4. Saves plots, top competing grid points, and the a2 = 1 slice data.
#
# Requires:input_csv = Path("/content/branch_residual_scan.csv") file!
#   /content/branch_residual_scan.csv
#   /content/results/radial_spectral_gap/branch_residual_scan.csv
#   results/radial_spectral_gap/branch_residual_scan.csv
#
# Generates:
# png_path = outdir / "radial_branch_residual_heatmap.png"
# pdf_path = outdir / "radial_branch_residual_heatmap.pdf"
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Colab/Jupyter inline display when available; harmless in normal Python.
try:
    get_ipython().run_line_magic("matplotlib", "inline")
except Exception:
    pass

from pathlib import Path
from IPython.display import Image, display

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Configuration
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

CANONICAL_A2 = 1.0
CANONICAL_A4 = 0.75

CSV_NAME = "branch_residual_scan.csv"

OUTDIR = Path("results/radial_branch_selection")
OUTDIR.mkdir(parents=True, exist_ok=True)

# Heatmap display settings.
# NOTE: smoothing/interpolation is for display only. Raw minima and top-15
# competing points are always computed from the raw CSV values.
Z_FLOOR = 1e-9
Z_CEILING = 1.0
HEATMAP_LOG_MIN = -8.8
HEATMAP_LOG_MAX = -0.8
HEATMAP_LEVELS = 120
INTERP_FACTOR = 10
INTERP_METHOD = "cubic"  # "linear" is safer; "cubic" is smoother for presentation.


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Input discovery
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def find_branch_residual_csv(filename=CSV_NAME):
    """
    Search common Colab/repo locations for branch_residual_scan.csv.

    Returns
    -------
    pathlib.Path
        Path to the selected CSV.

    Raises
    ------
    FileNotFoundError
        If the CSV cannot be found.
    """
    cwd = Path.cwd()

    candidates = [
        Path("/content") / filename,
        Path("/content/results/radial_spectral_gap") / filename,
        Path("/content/Projection_Relativity/results/radial_spectral_gap") / filename,
        Path("/content/Projection_Relativity/data/projection_relativity_I") / filename,
        cwd / filename,
        cwd / "results/radial_spectral_gap" / filename,
        cwd / "data" / filename,
    ]

    for path in candidates:
        if path.exists() and path.is_file():
            print(f"Using input CSV: {path.resolve()}")
            return path

    # Recursive fallback. Prefer radial_spectral_gap locations, then newest file.
    search_roots = []
    for root in [cwd, Path("/content")]:
        try:
            if root.exists() and root.is_dir() and root not in search_roots:
                search_roots.append(root)
        except Exception:
            pass

    found = []
    for root in search_roots:
        try:
            found.extend([p for p in root.rglob(filename) if p.is_file()])
        except Exception as exc:
            print(f"Search skipped under {root}: {exc}")

    if found:
        def score(path):
            parts = set(path.parts)
            preferred = 1 if "radial_spectral_gap" in parts else 0
            try:
                mtime = path.stat().st_mtime
            except Exception:
                mtime = 0
            return (preferred, mtime)

        found = sorted(found, key=score, reverse=True)
        print("Found candidate CSV files:")
        for p in found[:10]:
            print(" -", p.resolve())
        print(f"Using input CSV: {found[0].resolve()}")
        return found[0]

    raise FileNotFoundError(
        "Could not find branch_residual_scan.csv.\n"
        "Upload it to /content/branch_residual_scan.csv or place it under "
        "results/radial_spectral_gap/branch_residual_scan.csv."
    )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Data loading
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

input_csv = find_branch_residual_csv()

df = pd.read_csv(input_csv)

required_cols = {"a2", "a4", "residual"}
missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"Missing required CSV columns: {missing}")

df = df.copy()
df["a2"] = pd.to_numeric(df["a2"], errors="coerce")
df["a4"] = pd.to_numeric(df["a4"], errors="coerce")
df["residual"] = pd.to_numeric(df["residual"], errors="coerce")
df = df.dropna(subset=["a2", "a4", "residual"])

if df.empty:
    raise ValueError("CSV loaded, but no valid rows remain after numeric cleanup.")

pivot = (
    df.pivot_table(index="a4", columns="a2", values="residual", aggfunc="min")
    .sort_index()
    .sort_index(axis=1)
)

grid_min = df.loc[df["residual"].idxmin()].copy()

x = pivot.columns.to_numpy(dtype=float)
y = pivot.index.to_numpy(dtype=float)
X_raw, Y_raw = np.meshgrid(x, y)

Z_raw_residual = pivot.to_numpy(dtype=float)
Z_log_raw = np.log10(np.clip(Z_raw_residual, Z_FLOOR, Z_CEILING))
Z_log_raw = np.ma.masked_invalid(Z_log_raw)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Display interpolation for smoother heatmap
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def make_smooth_surface(x, y, Z, factor=INTERP_FACTOR, method=INTERP_METHOD):
    """
    Interpolate log-residual grid for smoother display.

    This is visual interpolation only. Raw minima are computed from raw data.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    Z = np.asarray(Z, dtype=float)

    if factor <= 1:
        X, Y = np.meshgrid(x, y)
        return X, Y, np.ma.masked_invalid(Z)

    xi = np.linspace(float(x.min()), float(x.max()), max(len(x) * factor, len(x)))
    yi = np.linspace(float(y.min()), float(y.max()), max(len(y) * factor, len(y)))
    XI, YI = np.meshgrid(xi, yi)

    # Fill any NaNs before interpolation. Prefer nearest valid row/column behavior.
    Z_filled = pd.DataFrame(Z, index=y, columns=x).interpolate(
        axis=0, limit_direction="both"
    ).interpolate(
        axis=1, limit_direction="both"
    ).to_numpy(dtype=float)

    if np.isnan(Z_filled).any():
        # Fall back to no interpolation if the grid is too sparse.
        X, Y = np.meshgrid(x, y)
        return X, Y, np.ma.masked_invalid(Z)

    try:
        from scipy.interpolate import RectBivariateSpline

        kx = min(3 if method == "cubic" else 1, len(y) - 1)
        ky = min(3 if method == "cubic" else 1, len(x) - 1)

        spline = RectBivariateSpline(y, x, Z_filled, kx=kx, ky=ky)
        ZI = spline(yi, xi)

        # Avoid visual overshoot beyond intended log color range.
        ZI = np.clip(ZI, HEATMAP_LOG_MIN, HEATMAP_LOG_MAX)

        return XI, YI, np.ma.masked_invalid(ZI)

    except Exception as exc:
        print(f"Interpolation fallback to raw grid: {exc}")
        X, Y = np.meshgrid(x, y)
        return X, Y, np.ma.masked_invalid(Z)


X_plot, Y_plot, Z_plot = make_smooth_surface(x, y, np.asarray(Z_log_raw.filled(np.nan)))


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Plot 1: Smooth 2D heatmap
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

fig, ax = plt.subplots(figsize=(9, 7))

levels = np.linspace(HEATMAP_LOG_MIN, HEATMAP_LOG_MAX, HEATMAP_LEVELS)

im = ax.contourf(
    X_plot,
    Y_plot,
    Z_plot,
    levels=levels,
    cmap="viridis",
    vmin=HEATMAP_LOG_MIN,
    vmax=HEATMAP_LOG_MAX,
    extend="both",
)

# Light contour guide lines make the smooth gradient easier to read.
guide_levels = np.linspace(HEATMAP_LOG_MIN, HEATMAP_LOG_MAX, 17)
ax.contour(
    X_plot,
    Y_plot,
    Z_plot,
    levels=guide_levels,
    colors="white",
    linewidths=0.25,
    alpha=0.25,
)

ax.scatter(
    [CANONICAL_A2],
    [CANONICAL_A4],
    facecolors="none",
    edgecolors="black",
    marker="o",
    s=170,
    linewidths=1.2,
    zorder=4,
    label=r"projection-trace branch $(1,3/4)$",
)

ax.scatter(
    [grid_min["a2"]],
    [grid_min["a4"]],
    color="#1f77b4",
    marker="o",
    s=85,
    zorder=5,
    label="raw grid minimum",
)

ax.scatter(
    [CANONICAL_A2],
    [CANONICAL_A4],
    color="#ff7f0e",
    marker="x",
    s=120,
    linewidths=2.0,
    zorder=6,
    label="analytic branch point",
)

ax.set_xlabel(r"quadratic coefficient $a_2$")
ax.set_ylabel(r"quartic coefficient $a_4$")
ax.set_title("Radial Branch Selection: Closure Residual Landscape")

ax.set_xlim(float(x.min()), float(x.max()))
ax.set_ylim(float(y.min()), float(y.max()))

ax.legend(
    loc="upper right",
    frameon=True,
    facecolor="white",
    edgecolor="0.8",
    framealpha=0.92,
    fontsize=10,
)

cbar = fig.colorbar(im, ax=ax, ticks=np.arange(HEATMAP_LOG_MIN, HEATMAP_LOG_MAX + 0.1, 1.0))
cbar.set_label(r"$\log_{10} \mathcal{R}_X(a_2,a_4)$")

heatmap_png = OUTDIR / "radial_branch_residual_heatmap_smooth.png"
heatmap_pdf = OUTDIR / "radial_branch_residual_heatmap_smooth.pdf"

fig.tight_layout()
fig.savefig(heatmap_png, dpi=300, bbox_inches="tight")
fig.savefig(heatmap_pdf, bbox_inches="tight")
plt.show()

print("Saved smooth 2D heatmap:")
print(" -", heatmap_png.resolve())
print(" -", heatmap_pdf.resolve())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Plot 2: Black-and-white 1D a4 branch plot at fixed a2 ≈ 1
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

a2_values = np.sort(df["a2"].unique())
a2_slice_value = float(a2_values[np.argmin(np.abs(a2_values - CANONICAL_A2))])

slice_df = (
    df[np.isclose(df["a2"], a2_slice_value)]
    .sort_values("a4")
    .copy()
)

if slice_df.empty:
    raise ValueError(f"No data found for nearest a2 slice {a2_slice_value}.")

slice_df["log10_residual"] = np.log10(np.clip(slice_df["residual"], Z_FLOOR, None))
slice_min = slice_df.loc[slice_df["residual"].idxmin()].copy()

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    slice_df["a4"],
    slice_df["log10_residual"],
    color="black",
    linewidth=1.6,
    marker="o",
    markersize=4.5,
    markerfacecolor="white",
    markeredgecolor="black",
    label=rf"$a_2={a2_slice_value:.6g}$ slice",
)

ax.axvline(
    CANONICAL_A4,
    color="black",
    linestyle="--",
    linewidth=1.4,
    label=r"projection trace $a_4=3/4$",
)

ax.scatter(
    [slice_min["a4"]],
    [slice_min["log10_residual"]],
    s=95,
    facecolors="black",
    edgecolors="black",
    zorder=5,
    label="slice minimum",
)

ax.set_xlabel(r"quartic coefficient $a_4$")
ax.set_ylabel(r"$\log_{10}\mathcal{R}_X(1,a_4)$")
ax.set_title("Radial Branch Closure Along the Unit-Stiffness Branch")

ax.grid(True, color="0.75", linewidth=0.6, alpha=0.75)
ax.legend(frameon=True, facecolor="white", edgecolor="0.7")

branch_1d_png = OUTDIR / "radial_branch_a4_residual_bw.png"
branch_1d_pdf = OUTDIR / "radial_branch_a4_residual_bw.pdf"

fig.tight_layout()
fig.savefig(branch_1d_png, dpi=300, bbox_inches="tight")
fig.savefig(branch_1d_pdf, bbox_inches="tight")
plt.show()

print("Saved black-and-white 1D branch plot:")
print(" -", branch_1d_png.resolve())
print(" -", branch_1d_pdf.resolve())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Raw-grid reporting outputs
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

df_rank = df.copy()
df_rank["distance_from_canonical"] = np.sqrt(
    (df_rank["a2"] - CANONICAL_A2) ** 2
    + (df_rank["a4"] - CANONICAL_A4) ** 2
)
df_rank["log10_residual"] = np.log10(np.clip(df_rank["residual"], Z_FLOOR, None))

top15 = df_rank.sort_values("residual").head(15).copy()

top15_csv = OUTDIR / "radial_branch_top15_competing_grid_points.csv"
slice_csv = OUTDIR / "radial_branch_a2_unit_slice.csv"

top15.to_csv(top15_csv, index=False)
slice_df.to_csv(slice_csv, index=False)

print("\nRaw-grid minimum:")
display(pd.DataFrame([grid_min]))

print("\nTop 15 grid points by closure residual:")
display(top15[["a2", "a4", "residual", "log10_residual", "distance_from_canonical"]])

print("\nBest point on the nearest a2=1 slice:")
display(pd.DataFrame([slice_min])[["a2", "a4", "residual", "log10_residual"]])

print("\nSaved data tables:")
print(" -", top15_csv.resolve())
print(" -", slice_csv.resolve())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Force Colab display from saved files
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

print("\nDisplaying saved plot files:")
display(Image(filename=str(heatmap_png)))
display(Image(filename=str(branch_1d_png)))


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Suggested captions for paper use
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

print("Main-body caption for the 1D plot:")
print(r"""
\caption{
\label{fig:radial_branch_a4_residual}
\textbf{Radial branch closure along the unit-stiffness branch.}
With \(a_2=1\) fixed by unit local radial stiffness, the closure residual
\(\mathcal R_X\) is minimized at \(a_4=3/4\). This confirms that the
projection-trace radial branch \(V_{X,\star}(w)=1+w^2+\frac34w^4\) closes
the PR reference radial spectral vector.
}
""")

print("Caption for the 2D heatmap:")
print(r"""
\caption{
\label{fig:radial_branch_residual_landscape}
\textbf{Radial branch-selection residual landscape.}
The positive quartic family \(V_X(w)=1+a_2w^2+a_4w^4\) was scanned against
the PR radial closure vector. The raw residual minimum occurs at
\((a_2,a_4)=(1,3/4)\), matching the projection-trace radial branch.
The smooth color field is used only for visual interpolation of the sampled
grid; branch selection is fixed analytically by unit radial stiffness and the
\(3+1\) projection trace.
}
""")
