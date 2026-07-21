#!/usr/bin/env python3
"""Reproduce the PR-I radial/compact numerical ledger used by PR-IV."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import platform
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path

try:
    import numpy as np
    from scipy.linalg import eigh
except ImportError as exc:  # pragma: no cover - exercised by clean installations
    raise SystemExit("Install requirements.txt before running numerical reproduction.") from exc


TA, TX = Fraction(1, 4), Fraction(3, 4)
REFERENCE = {
    "lambda0": 2.322872581463488,
    "lambda1": 5.375889248196178,
    "lambda3": 13.233893408730470,
    "mu_min_squared": 3.053016666732689,
    "p1": 7.685346950896231e-4,
    "q_bc": 10.904981678435453,
    "alpha_tree_inverse": 137.036041314016444,
}


@dataclass(frozen=True)
class SpectralRow:
    n_basis: int
    lambda0: float
    lambda1: float
    lambda3: float
    mu_min_squared: float
    p1: float
    p3: float
    q_bc: float
    alpha_tree_inverse: float
    boundary_eigenvalue_low: float
    boundary_eigenvalue_high: float


def boundary_arithmetic() -> dict[str, object]:
    denominator = 1 - TA**3 - TA**4
    numerator = 1 + TA**3 + TA**4 + TX * (TA**5 - TA**8)
    response = numerator / denominator
    c_bc = TX * (1 + TA**2 - TA**6 * response)
    assert denominator == Fraction(251, 256)
    assert numerator == Fraction(267453, 262144)
    assert c_bc == Fraction(3354902985, 4211081216)
    return {
        "T_A": str(TA), "T_X": str(TX), "D_A": str(denominator),
        "N_bc": str(numerator), "R_bc": str(response), "c_bc": str(c_bc),
        "c_bc_decimal": float(c_bc),
    }


def build_ho_operators(n_basis: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    annihilation = np.zeros((n_basis, n_basis), dtype=float)
    for n in range(1, n_basis):
        annihilation[n - 1, n] = math.sqrt(n)
    creation = annihilation.T
    w = (annihilation + creation) / math.sqrt(2.0)
    w2 = w @ w
    harmonic = np.diag([2 * n + 1 for n in range(n_basis)])
    return np.eye(n_basis), w2, harmonic - w2


def solve_two_mode_boundary(n_basis: int, c_bc: float, channels: tuple[int, int] = (1, 3)) -> SpectralRow:
    ident, w2, p2 = build_ho_operators(n_basis)
    w4 = w2 @ w2
    radial = p2 + ident + w2 + 0.75 * w4
    lambdas, modes = eigh(radial, subset_by_index=[0, max(channels) + 1])
    multiplier = c_bc * ident + w2 + 0.75 * w4
    block = modes[:, channels].T @ multiplier @ modes[:, channels]
    gaps = lambdas[list(channels)] - lambdas[0]
    k2 = np.diag((gaps / (lambdas[1] - lambdas[0])) ** 2)
    boundary_eigenvalues, boundary_modes = eigh(k2 @ block @ k2)
    weights = boundary_modes[:, -1] ** 2
    q_bc = float(weights @ gaps)
    return SpectralRow(
        n_basis=n_basis,
        lambda0=float(lambdas[0]), lambda1=float(lambdas[1]),
        lambda3=float(lambdas[3]), mu_min_squared=float(lambdas[1] - lambdas[0]),
        p1=float(weights[0]), p3=float(weights[1]), q_bc=q_bc,
        alpha_tree_inverse=4.0 * math.pi * q_bc,
        boundary_eigenvalue_low=float(boundary_eigenvalues[0]),
        boundary_eigenvalue_high=float(boundary_eigenvalues[1]),
    )


def load_tolerances(path: Path) -> dict[str, float]:
    return json.loads(path.read_text(encoding="utf-8"))["absolute_tolerances"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--basis", default="24,32,40,50,60,70,80,100")
    parser.add_argument("--tolerances", type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    harness = Path(__file__).resolve().parents[2]
    tolerances = load_tolerances(args.tolerances or harness / "numerical_tolerances.json")
    boundary = boundary_arithmetic()
    rows = [solve_two_mode_boundary(int(n), boundary["c_bc_decimal"])
            for n in args.basis.split(",") if n.strip()]
    final = rows[-1]
    comparison: dict[str, dict[str, object]] = {}
    for key, reference in REFERENCE.items():
        generated = getattr(final, key)
        tolerance = tolerances["p1"] if key == "p1" else tolerances["spectral"]
        difference = abs(generated - reference)
        comparison[key] = {
            "generated": generated, "manuscript_reference": reference,
            "absolute_difference": difference, "absolute_tolerance": tolerance,
            "status": "PASS" if difference <= tolerance else "FAIL",
        }
    status = "PASS" if all(item["status"] == "PASS" for item in comparison.values()) else "FAIL"
    report = {
        "status": status,
        "certificate": "PR-I radial/compact numerical reproduction used by PR-IV",
        "generation_uses_empirical_alpha": False,
        "exact_boundary_arithmetic": boundary,
        "radial_coefficients": {"a2": 1, "a4": "3/4", "constraint_determinant": 4},
        "minimal_projector": {"channels": [1, 3], "rank": 2},
        "final_generated": asdict(final),
        "manuscript_comparison": comparison,
        "last_step_convergence": {
            "p1": abs(rows[-1].p1 - rows[-2].p1),
            "q_bc": abs(rows[-1].q_bc - rows[-2].q_bc),
            "alpha_tree_inverse": abs(rows[-1].alpha_tree_inverse - rows[-2].alpha_tree_inverse),
        },
        "runtime": {
            "python": platform.python_version(), "platform": platform.platform(),
            "numpy": np.__version__, "scipy": __import__("scipy").__version__,
            "thread_environment": {name: os.environ.get(name) for name in
                ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS")},
        },
        "interpretation": "PASS certifies agreement with the frozen manuscript ledger within the published numerical tolerance; exact identities are certified separately with zero tolerance.",
    }
    (args.output_dir / "pr4_pr1_numerical_results.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with (args.output_dir / "pr4_pr1_convergence.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0])))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    print(f"PR-IV PR-I numerical reproduction: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
