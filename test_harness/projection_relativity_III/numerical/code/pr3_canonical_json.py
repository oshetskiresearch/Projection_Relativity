#!/usr/bin/env python3
"""
PR-III canonical JSON utilities.

This module is the first step toward reducing artifact drift from metadata order,
indentation, and JSON formatting. It preserves decimal values as strings rather
than coercing them to floats.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CANONICAL_INDENT = 2


def canonical_json_text(payload: dict[str, Any]) -> str:
    """Return canonical PR-III JSON text with stable key order and newline."""
    return json.dumps(payload, indent=CANONICAL_INDENT, sort_keys=True, ensure_ascii=False) + "\n"


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_canonical_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json_text(payload), encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Canonicalize one or more PR-III JSON files in place.")
    parser.add_argument("paths", nargs="+", help="JSON file paths to canonicalize")
    args = parser.parse_args()

    for raw in args.paths:
        path = Path(raw)
        write_canonical_json(path, read_json(path))
        print(f"canonicalized {path}")
