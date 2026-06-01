#!/usr/bin/env python3
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
# I'll see you in the decoherence!"
#
# Covers:
# solve_radial_gap.py
# scan_branch_residuals.py
# branch_closure_vector_scan.py
#
# Combined single-file runner for:
# 1. radial spectral gap solve,
# 2. branch residual scan,
# 3. branch closure-vector scan,
# 4. gzip-compressed Colab results archive.
#
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
Single-file Colab runner for the Projection Relativity radial branch checks.

No other local Python files are required. This file contains the full content
needed from:

    solve_radial_gap.py
    scan_branch_residuals.py
    branch_closure_vector_scan.py

Colab usage:

    !python radial_branch_colab_runner.py

Fast test:

    !python radial_branch_colab_runner.py --quick

Outputs:

    pr_radial_branch_results/radial_gap_result.csv
    pr_radial_branch_results/branch_residual_scan.csv
    pr_radial_branch_results/branch_closure_vector_scan.csv
    pr_radial_branch_results.tar.gz
"""

from __future__ import annotations

import argparse
import tarfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.linalg import eigh_tridiagonal


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# solve_radial_gap.py content
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


@dataclass
class RadialGapResult:
    a2: float
    a4: float
    L: float
    N: int
    lambda0: float
    lambda1: float
    mu_min_sq: float


def solve_radial_gap(
    a2: float = 1.0,
    a4: float = 0.75,
    L: float = 8.0,
    N: int = 4000,
) -> RadialGapResult:
    """Solve the low-lying radial spectrum for V(w)=1+a2*w^2+a4*w^4."""
    if N < 100:
        raise ValueError("N should be at least 100 for a meaningful finite-difference solve.")
    if L <= 0:
        raise ValueError("L must be positive.")

    # Interior grid. Dirichlet boundaries at -L and +L are excluded.
    x = np.linspace(-L, L, N + 2)[1:-1]
    dx = x[1] - x[0]

    # -d^2/dw^2 finite-difference tridiagonal.
    kinetic_diag = np.full(N, 2.0 / dx**2)
    kinetic_off = np.full(N - 1, -1.0 / dx**2)

    V = 1.0 + a2 * x**2 + a4 * x**4
    diag = kinetic_diag + V

    vals = eigh_tridiagonal(diag, kinetic_off, select="i", select_range=(0, 1))[0]
    lambda0, lambda1 = float(vals[0]), float(vals[1])

    return RadialGapResult(
        a2=float(a2),
        a4=float(a4),
        L=float(L),
        N=int(N),
        lambda0=lambda0,
        lambda1=lambda1,
        mu_min_sq=lambda1 - lambda0,
    )


def write_radial_gap(outdir: Path, a2: float, a4: float, L: float, N: int) -> RadialGapResult:
    result = solve_radial_gap(a2=a2, a4=a4, L=L, N=N)
    out_path = outdir / "radial_gap_result.csv"
    pd.DataFrame([result.__dict__]).to_csv(out_path, index=False)

    print("\nProjection Relativity radial spectral gap")
    print("-----------------------------------------")
    print(f"a2        = {result.a2:.12g}")
    print(f"a4        = {result.a4:.12g}")
    print(f"L         = {result.L:.12g}")
    print(f"N         = {result.N}")
    print(f"lambda_0  = {result.lambda0:.12f}")
    print(f"lambda_1  = {result.lambda1:.12f}")
    print(f"mu_min^2  = {result.mu_min_sq:.12f}")
    print(f"Saved     = {out_path}")

    return result


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# scan_branch_residuals.py content
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


CANONICAL_A2 = 1.0
CANONICAL_A4 = 0.75
CANONICAL_GAP = 3.052966743096


def gap_residual(mu_min_sq: float, target: float = CANONICAL_GAP) -> float:
    """Simple normalized residual against the canonical spectral gap."""
    return abs(mu_min_sq - target) / target


def run_branch_residual_scan(
    a2_min: float = 0.6,
    a2_max: float = 1.4,
    a2_steps: int = 17,
    a4_min: float = 0.35,
    a4_max: float = 1.15,
    a4_steps: int = 17,
    L: float = 8.0,
    N: int = 1500,
) -> pd.DataFrame:
    rows = []

    for a2 in np.linspace(a2_min, a2_max, a2_steps):
        for a4 in np.linspace(a4_min, a4_max, a4_steps):
            try:
                result = solve_radial_gap(a2=float(a2), a4=float(a4), L=L, N=N)
                rows.append(
                    {
                        "a2": a2,
                        "a4": a4,
                        "lambda0": result.lambda0,
                        "lambda1": result.lambda1,
                        "mu_min_sq": result.mu_min_sq,
                        "residual": gap_residual(result.mu_min_sq),
                    }
                )
            except Exception as exc:
                rows.append(
                    {
                        "a2": a2,
                        "a4": a4,
                        "lambda0": np.nan,
                        "lambda1": np.nan,
                        "mu_min_sq": np.nan,
                        "residual": np.nan,
                        "error": str(exc),
                    }
                )

    return pd.DataFrame(rows)


def write_branch_residual_scan(outdir: Path, L: float, N: int, a2_steps: int, a4_steps: int) -> pd.DataFrame:
    print("\nRunning branch residual scan...")
    df = run_branch_residual_scan(L=L, N=N, a2_steps=a2_steps, a4_steps=a4_steps)
    out_path = outdir / "branch_residual_scan.csv"
    df.to_csv(out_path, index=False)

    best = df.dropna(subset=["residual"]).sort_values("residual").head(10)
    print("Saved:", out_path)
    print("Top branch candidates:")
    print(best.to_string(index=False))
    return df


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# branch_closure_vector_scan.py content
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


A2_STAR = 1.0
A4_STAR = 0.75
LAMBDA0_STAR = 2.322863529580
LAMBDA1_STAR = 5.375830272676
GAP_STAR = 3.052966743096


@dataclass
class ClosureVector:
    lambda0: float
    lambda1: float
    gap: float
    trace_a2_residual: float
    trace_a4_residual: float


def closure_vector(a2: float, a4: float, L: float, N: int) -> ClosureVector:
    """Compute a reconstructed PR radial closure vector."""
    result = solve_radial_gap(a2=a2, a4=a4, L=L, N=N)
    return ClosureVector(
        lambda0=result.lambda0,
        lambda1=result.lambda1,
        gap=result.mu_min_sq,
        trace_a2_residual=a2 - A2_STAR,
        trace_a4_residual=a4 - A4_STAR,
    )


def weighted_closure_residual(vec: ClosureVector) -> float:
    """Compute normalized closure-vector residual."""
    r0 = (vec.lambda0 - LAMBDA0_STAR) / LAMBDA0_STAR
    r1 = (vec.lambda1 - LAMBDA1_STAR) / LAMBDA1_STAR
    rg = (vec.gap - GAP_STAR) / GAP_STAR
    ra2 = vec.trace_a2_residual
    ra4 = vec.trace_a4_residual / A4_STAR

    return float(np.sqrt(r0**2 + r1**2 + rg**2 + ra2**2 + ra4**2))


def run_branch_closure_vector_scan(
    a2_min: float = 0.5,
    a2_max: float = 1.5,
    a2_steps: int = 41,
    a4_min: float = 0.25,
    a4_max: float = 1.25,
    a4_steps: int = 41,
    L: float = 8.0,
    N: int = 1200,
) -> pd.DataFrame:
    rows = []

    for a2 in np.linspace(a2_min, a2_max, a2_steps):
        for a4 in np.linspace(a4_min, a4_max, a4_steps):
            try:
                vec = closure_vector(float(a2), float(a4), L=L, N=N)
                rows.append(
                    {
                        "a2": a2,
                        "a4": a4,
                        "lambda0": vec.lambda0,
                        "lambda1": vec.lambda1,
                        "gap": vec.gap,
                        "trace_a2_residual": vec.trace_a2_residual,
                        "trace_a4_residual": vec.trace_a4_residual,
                        "closure_residual": weighted_closure_residual(vec),
                    }
                )
            except Exception as exc:
                rows.append(
                    {
                        "a2": a2,
                        "a4": a4,
                        "lambda0": np.nan,
                        "lambda1": np.nan,
                        "gap": np.nan,
                        "trace_a2_residual": np.nan,
                        "trace_a4_residual": np.nan,
                        "closure_residual": np.nan,
                        "error": str(exc),
                    }
                )

    return pd.DataFrame(rows)


def write_branch_closure_vector_scan(outdir: Path, L: float, N: int, a2_steps: int, a4_steps: int) -> pd.DataFrame:
    print("\nRunning branch closure-vector scan...")
    df = run_branch_closure_vector_scan(L=L, N=N, a2_steps=a2_steps, a4_steps=a4_steps)
    out_path = outdir / "branch_closure_vector_scan.csv"
    df.to_csv(out_path, index=False)

    best = df.dropna(subset=["closure_residual"]).sort_values("closure_residual").head(10)
    print("Saved:", out_path)
    print("Top branch closure-vector candidates:")
    print(best.to_string(index=False))
    return df


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Colab-safe runner and gzip folder archive
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def make_gzipped_results_folder(outdir: Path, archive_path: Path) -> Path:
    """Write a .tar.gz archive containing the complete results folder."""
    outdir = outdir.resolve()
    archive_path = archive_path.resolve()
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    if archive_path.exists():
        archive_path.unlink()

    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(outdir, arcname=outdir.name)

    return archive_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run all PR radial branch checks from one Colab-safe file.")
    parser.add_argument("--mode", choices=["gap", "residual", "closure", "all"], default="all")
    parser.add_argument("--outdir", default="pr_radial_branch_results")
    parser.add_argument("--archive", default="pr_radial_branch_results.tar.gz")
    parser.add_argument("--a2", type=float, default=1.0)
    parser.add_argument("--a4", type=float, default=0.75)
    parser.add_argument("--L", type=float, default=8.0)
    parser.add_argument("--gap-N", dest="gap_N", type=int, default=4000)
    parser.add_argument("--scan-N", dest="scan_N", type=int, default=1500)
    parser.add_argument("--closure-N", dest="closure_N", type=int, default=1200)
    parser.add_argument("--scan-a2-steps", type=int, default=17)
    parser.add_argument("--scan-a4-steps", type=int, default=17)
    parser.add_argument("--closure-a2-steps", type=int, default=41)
    parser.add_argument("--closure-a4-steps", type=int, default=41)
    parser.add_argument("--quick", action="store_true", help="Use smaller grids for a fast smoke test.")
    parser.add_argument("--no-archive", action="store_true", help="Do not create the .tar.gz results archive.")
    parser.add_argument("--download", action="store_true", help="If running in Colab, download the .tar.gz archive.")
    return parser


def maybe_download_in_colab(path: Path) -> None:
    try:
        from google.colab import files  # type: ignore
    except Exception:
        print("Not running in Colab, so automatic download was skipped.")
        return
    files.download(str(path))


def main() -> None:
    parser = build_parser()
    args, unknown = parser.parse_known_args()
    if unknown:
        print("Ignoring notebook/runtime arguments:", " ".join(unknown))

    if args.quick:
        args.gap_N = min(args.gap_N, 1000)
        args.scan_N = min(args.scan_N, 600)
        args.closure_N = min(args.closure_N, 600)
        args.scan_a2_steps = min(args.scan_a2_steps, 9)
        args.scan_a4_steps = min(args.scan_a4_steps, 9)
        args.closure_a2_steps = min(args.closure_a2_steps, 11)
        args.closure_a4_steps = min(args.closure_a4_steps, 11)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if args.mode in ("gap", "all"):
        write_radial_gap(outdir, a2=args.a2, a4=args.a4, L=args.L, N=args.gap_N)

    if args.mode in ("residual", "all"):
        write_branch_residual_scan(
            outdir,
            L=args.L,
            N=args.scan_N,
            a2_steps=args.scan_a2_steps,
            a4_steps=args.scan_a4_steps,
        )

    if args.mode in ("closure", "all"):
        write_branch_closure_vector_scan(
            outdir,
            L=args.L,
            N=args.closure_N,
            a2_steps=args.closure_a2_steps,
            a4_steps=args.closure_a4_steps,
        )

    print("\nDone.")
    print("Output folder:", outdir.resolve())

    if not args.no_archive:
        archive_path = make_gzipped_results_folder(outdir, Path(args.archive))
        print("Gzipped results folder:", archive_path.resolve())
        print("Colab download command:")
        print(f"from google.colab import files; files.download('{archive_path.as_posix()}')")
        if args.download:
            maybe_download_in_colab(archive_path)


if __name__ == "__main__":
    main()
