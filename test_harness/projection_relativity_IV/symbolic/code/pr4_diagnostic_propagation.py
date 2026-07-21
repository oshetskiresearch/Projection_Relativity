#!/usr/bin/env python3
"""Regenerate the bounded diagnostic-control tables used by PR-IV."""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

from pr4_pr1_numerical_reproduction import build_ho_operators


getcontext().prec = 70
TA, TX = Fraction(1, 4), Fraction(3, 4)
DA = 1 - TA**3 - TA**4
PI_D = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
COMPACT_REFERENCE = {
    "published_sigma_minus1_Pi13": 137.035999207530239,
    "control_sigma0_Pi13": 137.035999207470098,
    "control_sigma_plus1_Pi13": 137.035999207409986,
    "control_sigma_minus1_Pi15": 254.208754866216196,
    "control_sigma_minus1_Pi17": 384.885897406270487,
}


def cbc_for_sigma(sigma8: int) -> Fraction:
    numerator = 1 + TA**3 + TA**4 + TX * (TA**5 + sigma8 * TA**8)
    return TX * (1 + TA**2 - TA**6 * numerator / DA)


def solve_compact(channels: tuple[int, int], cbc: float, n_basis: int = 100) -> dict[str, float]:
    ident, w2, p2 = build_ho_operators(n_basis)
    w4 = w2 @ w2
    radial = p2 + ident + w2 + 0.75 * w4
    lambdas, modes = eigh(radial, subset_by_index=[0, max(channels)])
    block = modes[:, channels].T @ (cbc * ident + w2 + 0.75 * w4) @ modes[:, channels]
    gaps = lambdas[list(channels)] - lambdas[0]
    k2 = np.diag((gaps / (lambdas[1] - lambdas[0])) ** 2)
    values, vectors = eigh(k2 @ block @ k2)
    weights = vectors[:, -1] ** 2
    q_bc = float(weights @ gaps)
    p1 = float(weights[0])
    alpha_tree = 4.0 * math.pi * q_bc
    delta = (1.0 - cbc) / q_bc
    sin2 = 0.25 - delta
    d1 = -p1 * delta * sin2
    d2 = d1 * delta / math.sqrt(3.0)
    return {
        "p_first": p1, "p_high": float(weights[1]), "q_bc": q_bc,
        "Delta_EW": delta, "sin2thetaW": sin2, "alpha_tree_inverse": alpha_tree,
        "alpha_D1D2_inverse": alpha_tree + 4.0 * math.pi * (d1 + d2),
        "boundary_eigenvalue_low": float(values[0]), "boundary_eigenvalue_high": float(values[1]),
    }


def compact_rows(table_tolerance: float) -> list[dict[str, object]]:
    alpha_ref, alpha_sigma = 137.035999206, 0.000000011
    specs = [
        ("published_sigma_minus1_Pi13", -1, (1, 3), True),
        ("control_sigma0_Pi13", 0, (1, 3), False),
        ("control_sigma_plus1_Pi13", 1, (1, 3), False),
        ("control_sigma_minus1_Pi15", -1, (1, 5), False),
        ("control_sigma_minus1_Pi17", -1, (1, 7), False),
    ]
    rows = []
    for model, sigma, channels, canonical in specs:
        generated = solve_compact(channels, float(cbc_for_sigma(sigma)))
        residual = generated["alpha_D1D2_inverse"] - alpha_ref
        table_difference = abs(generated["alpha_D1D2_inverse"] - COMPACT_REFERENCE[model])
        rows.append({
            "model_id": model, "completed_class_admissible": canonical, "sigma8": sigma,
            "channels": f"{channels[0]},{channels[1]}", "c_bc": f"{float(cbc_for_sigma(sigma)):.18f}",
            **{key: f"{value:.18g}" for key, value in generated.items()},
            "manuscript_alpha_value": f"{COMPACT_REFERENCE[model]:.15f}",
            "table_absolute_difference": f"{table_difference:.18g}",
            "table_reproduced": table_difference <= table_tolerance,
            "alpha_Rb_reference": f"{alpha_ref:.12f}", "alpha_residual": f"{residual:.18g}",
            "alpha_sigma_distance": f"{abs(residual)/alpha_sigma:.9f}",
            "inside_Rb_1sigma": abs(residual) <= alpha_sigma,
        })
    return rows


def radiative_rows() -> list[dict[str, object]]:
    p1 = Decimal("7.685346950896231e-04")
    delta = Decimal("0.018644280306692899718928776428403028768291215822597")
    sin2 = Decimal("0.231355763298189")
    ngen_factor = Decimal(3).sqrt() ** Decimal(-1)
    alpha_tree, alpha_ref, alpha_sigma = Decimal("137.036041314016444"), Decimal("137.035999206"), Decimal("0.000000011")
    published = {(1, 1, 1, 0): "D1", (1, 2, 1, 1): "D2"}
    rows = []
    for exps in itertools.product(range(1, 3), range(1, 4), range(1, 3), range(0, 3)):
        if sum(exps) > 6:
            continue
        p_exp, d_exp, s_exp, g_exp = exps
        magnitude = p1**p_exp * delta**d_exp * sin2**s_exp * ngen_factor**g_exp
        alpha = alpha_tree - Decimal(4) * PI_D * magnitude
        residual = alpha - alpha_ref
        rows.append({
            "exponents_p_Delta_sin2_G": ";".join(map(str, exps)),
            "published_role": published.get(exps, "outside-class control"),
            "monomial_magnitude": str(magnitude), "alpha_inverse": str(alpha),
            "Rb_sigma_distance": str(abs(residual)/alpha_sigma),
            "inside_Rb_1sigma": abs(residual) <= alpha_sigma,
        })
    d1 = p1*delta*sin2
    d2 = p1*delta**2*sin2*ngen_factor
    alpha = alpha_tree - Decimal(4)*PI_D*(d1+d2)
    rows.append({
        "exponents_p_Delta_sin2_G": "published_D1_plus_D2", "published_role": "published_sum",
        "monomial_magnitude": str(d1+d2), "alpha_inverse": str(alpha),
        "Rb_sigma_distance": str(abs(alpha-alpha_ref)/alpha_sigma),
        "inside_Rb_1sigma": abs(alpha-alpha_ref) <= alpha_sigma,
    })
    return rows


def electroweak_rows() -> list[dict[str, object]]:
    eps, ngen = Decimal("0.010764280253915984059993061466845953623291973168297958463495179185823935069035706"), Decimal(3)
    mw_c1 = Decimal("80.087096563511109803746814699902444354649798569999232287716279442425889446764759")
    mz_c1 = Decimal("91.348172148831652601189435910712007341759134665792081831637272352752169646942106")
    mw_ref, mw_sigma, mz_ref, mz_sigma = Decimal("80.3692"), Decimal("0.0133"), Decimal("91.1876"), Decimal("0.0021")
    rows = []
    for a, b, k in itertools.product(range(1, 5), range(-4, 0), range(1, 5)):
        mw = mw_c1 * (Decimal(1) + Decimal(a)/ngen*eps).sqrt()
        mz = mz_c1 * (Decimal(1) + Decimal(b)/ngen*eps + Decimal(k)/ngen*eps**2).sqrt()
        mw_z, mz_z = abs(mw-mw_ref)/mw_sigma, abs(mz-mz_ref)/mz_sigma
        rows.append({
            "C2_charged_coefficient": a, "C2_neutral_coefficient": b, "D3_neutral_coefficient": k,
            "completed_class_admissible": (a, b, k) == (2, -1, 2),
            "MW_GeV": str(mw), "MZ_GeV": str(mz),
            "MW_sigma_distance": str(mw_z), "MZ_sigma_distance": str(mz_z),
            "both_inside_1sigma": mw_z <= 1 and mz_z <= 1,
        })
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--tolerances", type=Path)
    args = parser.parse_args(); args.output_dir.mkdir(parents=True, exist_ok=True)
    tolerance_path = args.tolerances or Path(__file__).resolve().parents[2] / "numerical_tolerances.json"
    table_tolerance = json.loads(tolerance_path.read_text(encoding="utf-8"))["absolute_tolerances"]["published_table"]
    compact, radiative, ew = compact_rows(table_tolerance), radiative_rows(), electroweak_rows()
    write_csv(args.output_dir / "pr4_compact_branch_outputs.csv", compact)
    write_csv(args.output_dir / "pr4_radiative_monomial_outputs.csv", radiative)
    write_csv(args.output_dir / "pr4_electroweak_coefficient_outputs.csv", ew)
    compact_inside = [r["model_id"] for r in compact if not r["completed_class_admissible"] and r["inside_Rb_1sigma"]]
    rad_inside = sum(r["published_role"] == "outside-class control" and r["inside_Rb_1sigma"] for r in radiative)
    ew_inside = [[r["C2_charged_coefficient"], r["C2_neutral_coefficient"], r["D3_neutral_coefficient"]]
                 for r in ew if not r["completed_class_admissible"] and r["both_inside_1sigma"]]
    status = "PASS" if all(r["table_reproduced"] for r in compact) and len(radiative) == 24 and len(ew) == 64 else "FAIL"
    report = {
        "status": status, "candidate_generation_uses_diagnostics": False,
        "compact_rows": len(compact), "compact_outside_class_inside_Rb_1sigma": compact_inside,
        "radiative_rows": len(radiative), "radiative_outside_class_inside_Rb_1sigma": rad_inside,
        "electroweak_rows": len(ew), "electroweak_outside_class_inside_both_1sigma": ew_inside,
        "interpretation": "Diagnostics are post-generation checks. They neither define nor enlarge the completed admissible class.",
    }
    (args.output_dir / "pr4_diagnostic_propagation_results.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PR-IV diagnostic propagation: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
