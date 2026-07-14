#!/usr/bin/env python3
"""
PR-III v00: Inheritance Ledger Loader and No-Fit Seed Audit

This module is the first PR-III compiler component. It loads the frozen
PR-I / PR-II inheritance ledger and verifies that the ledger is still in a
valid state before any PR-III Hessian, radiative, or SU(3) calculation runs.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER_PATH = REPO_ROOT / "data" / "inheritance_ledger.json"


@dataclass(frozen=True)
class LedgerObject:
    """Single inherited object in the PR-III inheritance ledger."""

    symbol: str
    display: str
    source: str
    status: str
    value: Any
    units: str | None
    allowed_as_input: bool
    notes: str


class LedgerError(RuntimeError):
    """Raised when the inheritance ledger fails an audit check."""


class InheritanceLedger:
    """Load and audit the PR-III inherited-object ledger."""

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload
        self.objects = [LedgerObject(**obj) for obj in payload.get("objects", [])]
        self.forbidden_generation_inputs = payload.get("forbidden_generation_inputs", [])

    @classmethod
    def from_file(cls, path: Path = DEFAULT_LEDGER_PATH) -> "InheritanceLedger":
        if not path.exists():
            raise LedgerError(f"Inheritance ledger not found: {path}")
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        return cls(payload)

    @property
    def status(self) -> str:
        return str(self.payload.get("status", "UNKNOWN"))

    def object_by_symbol(self, symbol: str) -> LedgerObject:
        for obj in self.objects:
            if obj.symbol == symbol:
                return obj
        raise LedgerError(f"Ledger object not found: {symbol}")

    def pending_objects(self) -> list[LedgerObject]:
        return [obj for obj in self.objects if obj.status.lower() != "frozen"]

    def audit_required_symbols(self, required: Iterable[str]) -> None:
        missing = [symbol for symbol in required if not any(obj.symbol == symbol for obj in self.objects)]
        if missing:
            raise LedgerError(f"Missing required inherited symbols: {missing}")

    def audit_no_forbidden_input_names(self, candidate_inputs: Iterable[str]) -> None:
        normalized_forbidden = [item.lower().replace(" ", "_") for item in self.forbidden_generation_inputs]
        offenders: list[str] = []
        for candidate in candidate_inputs:
            normalized_candidate = candidate.lower().replace(" ", "_")
            if any(token in normalized_candidate for token in normalized_forbidden):
                offenders.append(candidate)
        if offenders:
            raise LedgerError(f"Forbidden empirical generation inputs detected: {offenders}")

    def audit_step_01(self) -> None:
        required_symbols = [
            "Psi",
            "M_int_PR1",
            "O_X",
            "O_theta",
            "mu_min_squared",
            "P_disp",
            "P_A",
            "EW_parent_fiber",
            "sin2thetaW_tree",
            "GF_tree",
            "rho_EW_tree",
            "m_beta_beta_PR",
        ]
        self.audit_required_symbols(required_symbols)
        pending = self.pending_objects()
        if pending:
            raise LedgerError(f"Inheritance ledger still has pending objects: {[obj.symbol for obj in pending]}")
        if self.status.upper() != "FROZEN":
            raise LedgerError(f"Inheritance ledger is not frozen: {self.status}")
        if self.payload.get("project") != "Projection Relativity III":
            raise LedgerError("Inheritance ledger project label mismatch.")
        if self.payload.get("ledger") != "inheritance_ledger":
            raise LedgerError("Inheritance ledger identifier mismatch.")
        if not self.forbidden_generation_inputs:
            raise LedgerError("Forbidden generation input ledger must be nonempty.")


def build_inheritance_ledger() -> dict[str, Any]:
    """Return the locked Step 01 ledger after validating its frozen schema."""
    ledger = InheritanceLedger.from_file()
    ledger.audit_step_01()
    return ledger.payload


def main() -> None:
    print(json.dumps(build_inheritance_ledger(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
