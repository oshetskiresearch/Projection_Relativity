#!/usr/bin/env python3
"""
PR-III artifact drift audit.

This script is designed for Reproducibility Hardening Pass 004/005/006/008.
It separates artifact comparison into reproducibility tiers:

Tier 1: schema equality and status/gate equality.
Tier 2: numeric tolerance equality for decimal/string numeric values.
Tier 3: canonical JSON equality after sorted-key serialization.
Tier 4: byte-exact equality is intentionally not claimed here.

The script is deliberately stricter about required schema/gates than about
stored decimal tail formatting. It classifies drift instead of collapsing every
non-byte-identical artifact into a mathematical failure.

Pass 008 adds an explicit mechanical root-wrapper normalization tier for the
known dataset/input_policy/module mismatch. This normalization is recorded in
the audit output and does not claim byte-exact release regeneration.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
import sys
from collections import Counter
from decimal import Decimal, InvalidOperation, getcontext
from pathlib import Path
from types import ModuleType
from typing import Any

getcontext().prec = 120

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = ROOT.parents[2]
PAYLOAD_ROOT = REPOSITORY_ROOT / "data" / "projection_relativity_III"
PAIR_MANIFEST = ROOT / "schemas" / "pr3_full_regeneration_pairs.json"
TOLERANCE_MANIFEST = ROOT / "schemas" / "pr3_numeric_tolerances.json"

DEFAULT_ABS_TOL = Decimal("1e-40")
DEFAULT_REL_TOL = Decimal("1e-40")
ROOT_KEYS_COPIED_FROM_LOCKED = ("dataset", "input_policy")
ROOT_KEYS_REMOVED_FROM_GENERATED = ("module",)


class DriftAuditError(Exception):
    pass


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_text(payload: Any) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module spec for {path}")
    module = importlib.util.module_from_spec(spec)
    # Register before exec_module. dataclasses and some runtime decorators expect
    # sys.modules[__module__] to exist while the class body is being evaluated.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def discover_builder(module: ModuleType, preferred: str | None = None):
    if preferred and preferred != "AUTO":
        if not hasattr(module, preferred):
            raise DriftAuditError(f"preferred builder missing: {preferred}")
        fn = getattr(module, preferred)
        if not callable(fn):
            raise DriftAuditError(f"preferred builder is not callable: {preferred}")
        return fn, preferred

    candidates = []
    for name in dir(module):
        if not name.startswith("build_"):
            continue
        fn = getattr(module, name)
        if callable(fn):
            candidates.append((name, fn))

    if len(candidates) == 1:
        return candidates[0][1], candidates[0][0]

    preferred_order = [
        "build_payload",
        "build_audit",
        "build_manifest",
        "build_closure",
        "build_protocol",
        "build_kernel_seed",
        "build_running_continuity_audit",
    ]
    for name in preferred_order:
        if hasattr(module, name) and callable(getattr(module, name)):
            return getattr(module, name), name

    if candidates:
        names = [name for name, _ in candidates]
        raise DriftAuditError(f"multiple build_* functions found; set builder_function explicitly: {names}")
    raise DriftAuditError("no build_* function found")


def regenerate_payload(code_path: Path, builder_name: str | None) -> tuple[dict[str, Any], str]:
    """Regenerate an artifact through a build_* API or script stdout fallback.

    Early PR-III ledger modules were written as executable scripts before the
    build_* convention was introduced. The drift audit should classify their
    payload differences, not stop at API exposure. This mirrors the repo-native
    audit runner's fallback behavior.
    """
    try:
        module = load_module(code_path)
        builder, resolved_name = discover_builder(module, builder_name)
        payload = builder()
        if not isinstance(payload, dict):
            raise RuntimeError(f"builder {resolved_name} did not return a dict")
        return payload, resolved_name
    except Exception as import_error:
        proc = subprocess.run(
            [sys.executable, str(code_path)],
            cwd=str(PAYLOAD_ROOT),
            text=True,
            capture_output=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(
                f"builder import failed ({import_error}); script execution failed with {proc.returncode}: {proc.stderr.strip()}"
            ) from import_error
        try:
            payload = json.loads(proc.stdout)
        except json.JSONDecodeError as parse_error:
            raise RuntimeError(
                f"builder import failed ({import_error}); script stdout was not JSON: {parse_error}"
            ) from import_error
        if not isinstance(payload, dict):
            raise RuntimeError("script did not emit a JSON object")
        return payload, "__script_stdout__"


def normalize_mechanical_root_wrapper(locked: Any, generated: Any) -> tuple[Any, dict[str, Any]]:
    """Normalize the known root metadata wrapper mismatch for comparison only.

    Many generator outputs carry a top-level ``module`` key while the locked
    artifacts carry top-level ``dataset`` and/or ``input_policy`` keys. This is a
    mechanical wrapper mismatch, not a physics-payload change. The normalized
    payload is used for schema/numeric comparison, while raw canonical and byte
    equality are still reported separately and remain non-claimed.
    """
    normalization = {
        "applied": False,
        "added_from_locked": [],
        "removed_from_generated": [],
        "scope": "root_metadata_wrapper_only",
    }
    if not isinstance(locked, dict) or not isinstance(generated, dict):
        return generated, normalization

    normalized = dict(generated)

    for key in ROOT_KEYS_COPIED_FROM_LOCKED:
        if key in locked and key not in normalized:
            normalized[key] = locked[key]
            normalization["added_from_locked"].append(key)

    for key in ROOT_KEYS_REMOVED_FROM_GENERATED:
        if key not in locked and key in normalized:
            normalized.pop(key)
            normalization["removed_from_generated"].append(key)

    normalization["applied"] = bool(normalization["added_from_locked"] or normalization["removed_from_generated"])
    return normalized, normalization


def _finite_decimal(value: Decimal) -> Decimal | None:
    return value if value.is_finite() else None


def try_decimal(value: Any) -> Decimal | None:
    if isinstance(value, bool) or value is None:
        return None
    try:
        if isinstance(value, Decimal):
            return _finite_decimal(value)
        if isinstance(value, int):
            return Decimal(value)
        if isinstance(value, float):
            if not math.isfinite(value):
                return None
            return _finite_decimal(Decimal(repr(value)))
        if isinstance(value, str):
            raw = value.strip()
            if not raw:
                return None
            return _finite_decimal(Decimal(raw))
    except (InvalidOperation, ValueError, TypeError):
        return None
    return None


def parse_tolerance(value: Any, default: Decimal) -> Decimal:
    parsed = try_decimal(value)
    return parsed if parsed is not None else default


def decimal_close(a: Decimal, b: Decimal, abs_tol: Decimal, rel_tol: Decimal) -> bool:
    diff = abs(a - b)
    if diff <= abs_tol:
        return True
    scale = max(abs(a), abs(b), Decimal(1))
    return diff <= rel_tol * scale


def load_tolerances() -> dict[str, Any]:
    if not TOLERANCE_MANIFEST.exists():
        return {}
    return load_json(TOLERANCE_MANIFEST)


def tolerance_for(path: str, tolerances: dict[str, Any]) -> tuple[Decimal, Decimal]:
    default = tolerances.get("default", {})
    abs_tol = parse_tolerance(default.get("abs_tol", str(DEFAULT_ABS_TOL)), DEFAULT_ABS_TOL)
    rel_tol = parse_tolerance(default.get("rel_tol", str(DEFAULT_REL_TOL)), DEFAULT_REL_TOL)
    field = tolerances.get("fields", {}).get(path)
    if field:
        abs_tol = parse_tolerance(field.get("abs_tol", abs_tol), abs_tol)
        rel_tol = parse_tolerance(field.get("rel_tol", rel_tol), rel_tol)
    return abs_tol, rel_tol


def compare_values(locked: Any, generated: Any, path: str, failures: list[str], warnings: list[str], tolerances: dict[str, Any]) -> None:
    if isinstance(locked, dict) and isinstance(generated, dict):
        locked_keys = set(locked)
        generated_keys = set(generated)
        missing = sorted(locked_keys - generated_keys)
        extra = sorted(generated_keys - locked_keys)
        if missing:
            failures.append(f"{path}: missing keys in generated artifact: {missing}")
        if extra:
            failures.append(f"{path}: extra keys in generated artifact: {extra}")
        for key in sorted(locked_keys & generated_keys):
            compare_values(locked[key], generated[key], f"{path}.{key}", failures, warnings, tolerances)
        return

    if isinstance(locked, list) and isinstance(generated, list):
        if len(locked) != len(generated):
            failures.append(f"{path}: list length mismatch locked={len(locked)} generated={len(generated)}")
            return
        for idx, (a, b) in enumerate(zip(locked, generated)):
            compare_values(a, b, f"{path}[{idx}]", failures, warnings, tolerances)
        return

    dec_locked = try_decimal(locked)
    dec_generated = try_decimal(generated)
    if dec_locked is not None and dec_generated is not None:
        abs_tol, rel_tol = tolerance_for(path, tolerances)
        if not decimal_close(dec_locked, dec_generated, abs_tol, rel_tol):
            failures.append(
                f"{path}: numeric drift locked={locked!r} generated={generated!r} diff={dec_generated - dec_locked} abs_tol={abs_tol} rel_tol={rel_tol}"
            )
        elif str(locked) != str(generated):
            warnings.append(f"{path}: numeric formatting drift locked={locked!r} generated={generated!r}")
        return

    if dec_locked is not None or dec_generated is not None:
        failures.append(f"{path}: mixed numeric/text drift locked={locked!r} generated={generated!r}")
        return

    if locked != generated:
        failures.append(f"{path}: value mismatch locked={locked!r} generated={generated!r}")


def classify_failures(failures: list[str]) -> str:
    joined = "\n".join(failures)
    if "missing data artifact" in joined or "missing generator" in joined:
        return "missing_file"
    if "preferred builder" in joined or "build_*" in joined or "generator execution failed" in joined:
        return "builder_exposure_or_execution"
    if "missing keys" in joined or "extra keys" in joined or "list length mismatch" in joined:
        return "schema_drift"
    if "numeric drift" in joined:
        return "numeric_drift"
    if "mixed numeric/text drift" in joined:
        return "mixed_numeric_text_drift"
    if "value mismatch" in joined:
        return "text_or_metadata_drift"
    return "unclassified_failure"


def run_pair(pair: dict[str, Any], tolerances: dict[str, Any]) -> dict[str, Any]:
    name = pair["name"]
    data_path = PAYLOAD_ROOT / pair["data_path"]
    code_path = PAYLOAD_ROOT / pair["code_path"]
    builder_name = pair.get("builder_function")
    if not data_path.exists():
        failures = [f"missing data artifact: {pair['data_path']}"]
        return {"name": name, "status": "FAIL", "failure_class": classify_failures(failures), "failures": failures, "warnings": []}
    if not code_path.exists():
        failures = [f"missing generator: {pair['code_path']}"]
        return {"name": name, "status": "FAIL", "failure_class": classify_failures(failures), "failures": failures, "warnings": []}

    locked = load_json(data_path)
    try:
        generated, resolved_builder = regenerate_payload(code_path, builder_name)
    except Exception as exc:
        failures = [f"generator execution failed: {exc}"]
        return {"name": name, "status": "FAIL", "failure_class": classify_failures(failures), "failures": failures, "warnings": []}

    normalized_generated, root_normalization = normalize_mechanical_root_wrapper(locked, generated)

    failures: list[str] = []
    warnings: list[str] = []
    compare_values(locked, normalized_generated, pair["data_path"], failures, warnings, tolerances)

    locked_canon = canonical_text(locked)
    generated_canon = canonical_text(generated)
    normalized_generated_canon = canonical_text(normalized_generated)
    raw_canonical_equal = locked_canon == generated_canon
    normalized_canonical_equal = locked_canon == normalized_generated_canon
    byte_equal = data_path.read_text(encoding="utf-8") == generated_canon

    return {
        "name": name,
        "data_path": pair["data_path"],
        "code_path": pair["code_path"],
        "resolved_builder": resolved_builder,
        "status": "PASS" if not failures else "FAIL",
        "failure_class": None if not failures else classify_failures(failures),
        "schema_numeric_equal": not failures,
        "canonical_json_equal": raw_canonical_equal,
        "canonical_json_equal_after_root_normalization": normalized_canonical_equal,
        "byte_exact_release_equal": byte_equal,
        "root_wrapper_normalization": root_normalization,
        "failures": failures,
        "warnings": warnings,
    }


def summarize_root_normalization(results: list[dict[str, Any]]) -> dict[str, Any]:
    added = Counter()
    removed = Counter()
    pairs: list[str] = []
    for result in results:
        normalization = result.get("root_wrapper_normalization", {})
        if not normalization.get("applied"):
            continue
        pairs.append(result.get("name", "UNKNOWN_PAIR"))
        for key in normalization.get("added_from_locked", []):
            added[key] += 1
        for key in normalization.get("removed_from_generated", []):
            removed[key] += 1
    return {
        "pairs_normalized": len(pairs),
        "added_from_locked_key_counts": dict(sorted(added.items())),
        "removed_from_generated_key_counts": dict(sorted(removed.items())),
        "pairs": pairs,
        "claim": "root metadata wrapper comparison normalization only; byte-exact release regeneration not claimed",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PR-III artifact drift audit.")
    parser.add_argument("--pairs", default=str(PAIR_MANIFEST), help="Pair manifest path")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    pair_manifest = load_json(Path(args.pairs))
    tolerances = load_tolerances()
    results = [run_pair(pair, tolerances) for pair in pair_manifest.get("pairs", [])]
    failures = [r for r in results if r["status"] != "PASS"]
    failure_class_counts = Counter(r.get("failure_class") or "pass" for r in results)
    root_normalization_summary = summarize_root_normalization(results)
    summary = {
        "project": "Projection Relativity III",
        "audit": "artifact_drift_audit",
        "status": "PASS" if not failures else "FAIL",
        "pairs_checked": len(results),
        "pairs_passed": len(results) - len(failures),
        "pairs_failed": len(failures),
        "failure_class_counts": dict(sorted(failure_class_counts.items())),
        "mechanical_root_wrapper_normalization": root_normalization_summary,
        "byte_exact_release_claimed": False,
        "results": results,
    }

    if args.json:
        print(canonical_text(summary), end="")
        return

    print(f"PR-III artifact drift audit: {summary['status']}")
    print(f"pairs checked: {summary['pairs_checked']}; passed: {summary['pairs_passed']}; failed: {summary['pairs_failed']}")
    print("byte-exact release equality is not claimed by this audit")
    print("mechanical root wrapper normalization:")
    print(f"- pairs_normalized: {root_normalization_summary['pairs_normalized']}")
    for key, value in root_normalization_summary["added_from_locked_key_counts"].items():
        print(f"- added_from_locked.{key}: {value}")
    for key, value in root_normalization_summary["removed_from_generated_key_counts"].items():
        print(f"- removed_from_generated.{key}: {value}")
    print("failure classes:")
    for key, value in sorted(failure_class_counts.items()):
        print(f"- {key}: {value}")
    for result in results:
        mark = "PASS" if result["status"] == "PASS" else "FAIL"
        suffix = "" if result.get("failure_class") is None else f" [{result['failure_class']}]"
        builder_note = "" if "resolved_builder" not in result else f" builder={result['resolved_builder']}"
        norm = result.get("root_wrapper_normalization", {})
        norm_note = " normalized_root_wrapper" if norm.get("applied") else ""
        print(f"- {mark}: {result['name']}{suffix}{builder_note}{norm_note}")
        for failure in result["failures"]:
            print(f"  failure: {failure}")
        for warning in result["warnings"][:5]:
            print(f"  warning: {warning}")
        if len(result["warnings"]) > 5:
            print(f"  warning: ... {len(result['warnings']) - 5} more")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
