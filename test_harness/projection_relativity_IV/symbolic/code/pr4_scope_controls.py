#!/usr/bin/env python3
"""Generate the finite outside-class controls reported by PR-IV.

These rows document why the completed admissible class matters.  A surviving
row in a broader reduct is a scope witness, not an admissible PR-IV solution.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
from fractions import Fraction
from pathlib import Path


TA, TX = Fraction(1, 4), Fraction(3, 4)
PUBLISHED = {"sigma8": -1, "projector": "Pi13"}


def cbc(sigma: int) -> Fraction:
    denominator = 1 - TA**3 - TA**4
    numerator = 1 + TA**3 + TA**4 + TX * (TA**5 + sigma * TA**8)
    return TX * (1 + TA**2 - TA**6 * numerator / denominator)


def compact_rows() -> list[dict[str, object]]:
    rows = []
    for sigma, high in itertools.product((-1, 0, 1), (3, 5, 7)):
        is_canonical = sigma == -1 and high == 3
        rows.append({
            "sigma8": sigma, "projector": f"Pi1{high}", "channels": f"1,{high}",
            "c_bc_fraction": str(cbc(sigma)), "c_bc_decimal": f"{float(cbc(sigma)):.18f}",
            "same_trace_alphabet": True, "same_primitive_denominator": True,
            "rank_two_odd_projector": True,
            "orientation_closure": sigma == -1,
            "minimal_required_channel_closure": high == 3,
            "completed_class_admissible": is_canonical,
            "role": "canonical" if is_canonical else "outside-class control",
        })
    return rows


def generation_rows() -> list[dict[str, object]]:
    dimension = 3
    rows = []
    for n in range(1, 13):
        rows.append({
            "N_gen": n, "broken_dimension": dimension, "max_rank": min(n, dimension),
            "completeness_possible": n >= dimension,
            "nonredundancy_possible": n <= dimension,
            "complete_and_nonredundant": n == dimension,
            "minimum_omitted_directions": max(dimension - n, 0),
            "minimum_redundant_combinations_if_complete": max(n - dimension, 0),
        })
    return rows


def monomial_rows() -> list[dict[str, object]]:
    rows = []
    for exponents in itertools.product(range(1, 3), range(1, 4), range(1, 3), range(0, 3)):
        if sum(exponents) > 6:
            continue
        role = {(1, 1, 1, 0): "D1", (1, 2, 1, 1): "D2"}.get(exponents, "outside-class control")
        rows.append({
            "p1_exponent": exponents[0], "Delta_exponent": exponents[1],
            "sin2theta_exponent": exponents[2], "Ngen_minus_half_exponent": exponents[3],
            "total_degree": sum(exponents), "role": role,
        })
    return rows


def hypercharge_certificate() -> dict[str, object]:
    def anomalies(q: Fraction, u: Fraction, d: Fraction, l: Fraction, e: Fraction) -> list[Fraction]:
        return [2*q+u+d, 3*q+l, 6*q+3*u+3*d+2*l+e,
                6*q**3+3*u**3+3*d**3+2*l**3+e**3]
    branches = []
    for name, u_multiple in (("canonical", -4), ("up_down_relabeling", 2)):
        t = Fraction(1, 3)
        q, u, l, e = t, u_multiple*t, -3*t, 6*t
        d = -2*t-u
        values = anomalies(q, u, d, l, e)
        assert values == [0, 0, 0, 0]
        branches.append({"branch": name, "q": str(q), "u": str(u), "d": str(d),
                         "l": str(l), "e": str(e), "all_anomalies_zero": True})
    return {
        "linear_reduction": {"l": "-3t", "e": "6t", "d": "-2t-u"},
        "cubic_factorization": "-18*t*(u-2*t)*(u+4*t)",
        "nonzero_ledger_branches": branches,
        "excluded_control": "t=0 vectorlike singlet family has zero charged-fermion ledger",
        "status": "PASS",
    }


def photon_certificate() -> dict[str, object]:
    g, gp = Fraction(7, 5), Fraction(11, 6)
    matrix = [[g*g, -g*gp], [-g*gp, gp*gp]]
    determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    return {
        "matrix": [[str(x) for x in row] for row in matrix],
        "determinant": str(determinant), "rank": 1,
        "null_vector": [str(gp), str(g)], "status": "PASS" if determinant == 0 else "FAIL",
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    compact, generations, monomials = compact_rows(), generation_rows(), monomial_rows()
    c2 = [{"charged_coefficient": a, "neutral_coefficient": b,
           "canonical": (a, b) == (2, -1), "role": "canonical" if (a, b) == (2, -1) else "outside-class control"}
          for a in range(1, 5) for b in range(-4, 0)]
    d3 = [{"coefficient_k": k, "canonical": k == 2,
           "role": "canonical" if k == 2 else "fixed-kernel diagnostic sample"} for k in range(1, 5)]
    write_csv(args.output_dir / "pr4_compact_scope_controls.csv", compact)
    write_csv(args.output_dir / "pr4_generation_rank_nullity.csv", generations)
    write_csv(args.output_dir / "pr4_radiative_monomial_inventory.csv", monomials)
    write_csv(args.output_dir / "pr4_c2_coefficient_controls.csv", c2)
    write_csv(args.output_dir / "pr4_d3_coefficient_samples.csv", d3)
    report = {
        "status": "PASS",
        "compact": {"rows": len(compact), "completed_class_survivors":
                    [r["projector"] for r in compact if r["completed_class_admissible"]]},
        "generation": {"sampled": "1..12", "unique_complete_nonredundant_count":
                       [r["N_gen"] for r in generations if r["complete_and_nonredundant"]]},
        "radiative": {"degree_limit": 6, "monomial_count": len(monomials)},
        "c2": {"bounded_control_count": len(c2), "canonical_pair": [2, -1]},
        "d3": {"bounded_sample_count": len(d3), "canonical_coefficient": 2,
               "complete_fixed_kernel_family": "D3(k)=rho*k*P_Z; canonical closure fixes k=2"},
        "hypercharge": hypercharge_certificate(), "photon": photon_certificate(),
        "interpretation": "Only the canonical row satisfies every completed-class closure. Other rows are retained as reproducible outside-class controls.",
    }
    (args.output_dir / "pr4_scope_control_results.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert len(compact) == 9 and sum(r["completed_class_admissible"] for r in compact) == 1
    assert len(monomials) == 23 and len(c2) == 16 and len(d3) == 4
    print("PR-IV finite scope controls: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
