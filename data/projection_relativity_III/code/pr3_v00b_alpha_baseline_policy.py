#!/usr/bin/env python3
"""
PR-III v00b: Alpha Baseline Policy Loader

This module locks the high-resolution N=15000 alpha solve as the PR-III
TREE-level baseline while preserving the PR-I / PR-II finite-resolution value
as the published reproducibility baseline.

The empirical alpha reference is diagnostic-only and must not be used as a
generation input.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 50

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POLICY_PATH = REPO_ROOT / "data" / "alpha_baseline_policy.json"


class AlphaPolicyError(RuntimeError):
    """Raised when the alpha baseline policy fails validation."""


class AlphaBaselinePolicy:
    """Load and audit the PR-III alpha baseline policy."""

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload
        self.branches = payload["branches"]

    @classmethod
    def from_file(cls, path: Path = DEFAULT_POLICY_PATH) -> "AlphaBaselinePolicy":
        if not path.exists():
            raise AlphaPolicyError(f"Alpha policy not found: {path}")
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        return cls(payload)

    def decimal(self, branch: str, key: str = "alpha_inv") -> Decimal:
        return Decimal(str(self.branches[branch][key]))

    def audit(self) -> None:
        published = self.decimal("published_ledger")
        hr = self.decimal("high_resolution_tree_N15000")
        reference = self.decimal("diagnostic_reference_supplied")

        if self.branches["diagnostic_reference_supplied"].get("allowed_as_generation_input") is not False:
            raise AlphaPolicyError("Diagnostic alpha reference must be forbidden as a generation input.")
        if self.payload.get("status") != "ADOPTED_AS_PR3_TREE_BASELINE":
            raise AlphaPolicyError(f"Unexpected alpha policy status: {self.payload.get('status')}")
        if self.payload.get("project") != "Projection Relativity III":
            raise AlphaPolicyError("Alpha policy project label mismatch.")
        if self.payload.get("policy") != "alpha_baseline_policy":
            raise AlphaPolicyError("Alpha policy identifier mismatch.")
        if hr >= published:
            raise AlphaPolicyError("High-resolution PR-III baseline should lower the published finite-resolution inverse alpha.")
        if hr <= reference:
            raise AlphaPolicyError("High-resolution tree baseline should remain above the diagnostic reference before radiative correction.")
        if self.payload.get("codata_usage") != "diagnostic_only":
            raise AlphaPolicyError("CODATA/reference usage must remain diagnostic-only.")
        if "diagnostic_reference_alpha_inv" not in self.payload.get("no_fit_rule", {}).get("forbidden_generation_inputs", []):
            raise AlphaPolicyError("Diagnostic alpha reference must be listed as a forbidden generation input.")


def build_alpha_baseline_policy() -> dict[str, Any]:
    """Return the locked alpha baseline policy after validating no-fit gates."""
    policy = AlphaBaselinePolicy.from_file()
    policy.audit()
    return policy.payload


def main() -> None:
    print(json.dumps(build_alpha_baseline_policy(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
