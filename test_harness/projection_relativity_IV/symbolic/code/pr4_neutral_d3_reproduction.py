#!/usr/bin/env python3
"""Reproduce the neutral D3 classification links and diagnostic table."""

from __future__ import annotations

import argparse
import csv
import json
from decimal import Decimal, getcontext
from pathlib import Path


getcontext().prec = 70
REQUIRED_EXACT_CHECKS = {
    "d3:u1_rank_reduction", "d3:adjoint_trace", "d3:unique_quadratic_response",
    "d3:canonical_k", "d3:unique_defect_zero", "d3:structural_family_negative_control",
    "d3:diagnostic_firewall", "d3:log_hessian", "d3:second_jet_counterfamily",
    "physical-z:second_jet_shift", "physical-z:eft_operator",
    "d3:mixing_normalization_nogo", "physical-z:normalized_generator",
}


def data() -> dict[str, Decimal]:
    epsilon = Decimal("0.010764280253915984059993061466845953623291973168297958463495179185823935069035706")
    return {
        "epsilon": epsilon, "rho": epsilon*epsilon/Decimal(3), "pi_z_c2": -epsilon/Decimal(3),
        "mz_c1": Decimal("91.348172148831652601189435910712007341759134665792081831637272352752169646942106"),
        "mz_ref": Decimal("91.1876"), "mz_sigma": Decimal("0.0021"),
        "cos2theta_w": Decimal("0.768644236701811"),
    }


def solve_k(mass: Decimal, d: dict[str, Decimal]) -> Decimal:
    return ((mass/d["mz_c1"])**2 - Decimal(1) - d["pi_z_c2"]) / d["rho"]


def mz(k: Decimal, d: dict[str, Decimal]) -> Decimal:
    return d["mz_c1"] * (Decimal(1) + d["pi_z_c2"] + k*d["rho"]).sqrt()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--exact-results", type=Path, required=True)
    args = parser.parse_args(); args.output_dir.mkdir(parents=True, exist_ok=True)
    exact = json.loads(args.exact_results.read_text(encoding="utf-8"))
    checks = {row["id"]: row["status"] for row in exact["checks"]}
    exact_ok = all(checks.get(name) == "PASS" for name in REQUIRED_EXACT_CHECKS)
    d = data()
    lower = solve_k(d["mz_ref"]-d["mz_sigma"], d)
    upper = solve_k(d["mz_ref"]+d["mz_sigma"], d)
    central = solve_k(d["mz_ref"], d)
    models = [
        ("half_trace", Decimal(1), False),
        ("photon_safe_W3_pullback", Decimal(2)*d["cos2theta_w"], False),
        ("canonical", Decimal(2), False),
        ("three_half_trace", Decimal(3), False),
        ("diagnostic_central_value", central, True),
        ("strict_interval_lower_endpoint", lower, True),
        ("strict_interval_upper_endpoint", upper, True),
    ]
    rows = []
    for model, k, diagnostic_selected in models:
        mass = mz(k, d)
        distance = abs(mass-d["mz_ref"])/d["mz_sigma"]
        rows.append({
            "model_id": model, "k": str(k), "MZ_GeV": str(mass),
            "MZ_sigma_distance": str(distance), "inside_strict_1sigma": distance < 1,
            "completed_class_admissible": k == Decimal(2),
            "canonical_defect_k_minus_2": str(k-Decimal(2)),
            "uses_diagnostic_to_define_k": diagnostic_selected,
        })
    with (args.output_dir / "pr4_neutral_d3_diagnostic_table.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    references = {
        "lower": Decimal("0.768434787688685769"),
        "upper": Decimal("3.145092343548119919"),
        "central": Decimal("1.956749882341106"),
    }
    generated = {"lower": lower, "upper": upper, "central": central}
    comparisons = {name: {
        "generated": str(generated[name]), "manuscript_prefix": str(reference),
        "absolute_difference": str(abs(generated[name]-reference)),
        "status": "PASS" if abs(generated[name]-reference) < Decimal("1e-15") else "FAIL",
    } for name, reference in references.items()}
    status = "PASS" if exact_ok and all(row["status"] == "PASS" for row in comparisons.values()) else "FAIL"
    report = {
        "status": status,
        "exact_check_links": sorted(REQUIRED_EXACT_CHECKS), "all_exact_links_pass": exact_ok,
        "classification_dimensions": [10, 4, 3, 1],
        "fixed_kernel_structural_family": "D3(k)=rho*k*P_Z for every real k",
        "canonical_normalization": {"k": 2, "tensor": "2*rho*P_Z", "defect": "rho^2*(k-2)^2"},
        "diagnostic_open_interval": [str(lower), str(upper)],
        "diagnostic_central_k": str(central), "manuscript_comparison": comparisons,
        "integer_members_of_open_interval": [1, 2, 3],
        "interpretation": "The exact target-independent response closure fixes k=2. The diagnostic interval is reported only as an outside-class control.",
    }
    (args.output_dir / "pr4_neutral_d3_results.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PR-IV neutral D3 reproduction: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
