#!/usr/bin/env python3
"""
PR-III canonical release byte-exact regeneration audit.

Pass 016 promotes the previously separated schema/numeric reproducibility tier
into a deterministic canonical release-byte tier.

The audit regenerates every generator/data pair, applies only the locked release
presentation policy, and then requires the generated canonical release bytes to
match the locked canonical release bytes exactly.

Important claim boundary:

- This is not raw generator stdout byte identity.
- This is not raw checked-in file-order byte identity.
- It is byte identity of the canonical PR-III release artifacts after applying
  the documented release policy:

  1. root metadata wrapper normalization for dataset/input_policy/module;
  2. numeric display lock only when generated and locked finite Decimal leaves
     are equal under configured tolerance;
  3. exact nonnumeric text equality;
  4. canonical JSON serialization with sorted keys, two-space indent, UTF-8,
     and a terminal newline.

Any true schema drift, text drift, or numeric drift beyond policy remains fatal.
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
POLICY_MANIFEST = ROOT / "schemas" / "pr3_release_byte_exact_policy.json"

DEFAULT_ABS_TOL = Decimal("1e-40")
DEFAULT_REL_TOL = Decimal("1e-40")
ROOT_KEYS_COPIED_FROM_LOCKED = ("dataset", "input_policy")
ROOT_KEYS_REMOVED_FROM_GENERATED = ("module",)


class ReleaseByteExactError(Exception):
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
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def discover_builder(module: ModuleType, preferred: str | None = None):
    if preferred and preferred != "AUTO":
        if not hasattr(module, preferred):
            raise ReleaseByteExactError(f"preferred builder missing: {preferred}")
        fn = getattr(module, preferred)
        if not callable(fn):
            raise ReleaseByteExactError(f"preferred builder is not callable: {preferred}")
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
        raise ReleaseByteExactError(f"multiple build_* functions found; set builder_function explicitly: {names}")
    raise ReleaseByteExactError("no build_* function found")


def regenerate_payload(code_path: Path, builder_name: str | None) -> tuple[dict[str, Any], str]:
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


def normalize_root_wrapper(locked: Any, generated: Any) -> tuple[Any, dict[str, Any]]:
    info = {
        "applied": False,
        "added_from_locked": [],
        "removed_from_generated": [],
        "scope": "root_metadata_wrapper_only",
    }
    if not isinstance(locked, dict) or not isinstance(generated, dict):
        return generated, info

    normalized = dict(generated)
    for key in ROOT_KEYS_COPIED_FROM_LOCKED:
        if key in locked and key not in normalized:
            normalized[key] = locked[key]
            info["added_from_locked"].append(key)
    for key in ROOT_KEYS_REMOVED_FROM_GENERATED:
        if key not in locked and key in normalized:
            normalized.pop(key)
            info["removed_from_generated"].append(key)
    info["applied"] = bool(info["added_from_locked"] or info["removed_from_generated"])
    return normalized, info


def release_payload_from_locked_display(
    locked: Any,
    generated: Any,
    path: str,
    failures: list[str],
    events: Counter,
    tolerances: dict[str, Any],
) -> Any:
    """Return generated payload rendered with locked release display strings.

    The returned object uses generated structure and values, but it may reuse the
    locked string representation for finite Decimal leaves only after numeric
    equality under policy has been proven.
    """
    if isinstance(locked, dict) and isinstance(generated, dict):
        locked_keys = set(locked)
        generated_keys = set(generated)
        missing = sorted(locked_keys - generated_keys)
        extra = sorted(generated_keys - locked_keys)
        if missing:
            failures.append(f"{path}: missing keys in generated artifact: {missing}")
            events["schema_key_drift"] += 1
        if extra:
            failures.append(f"{path}: extra keys in generated artifact: {extra}")
            events["schema_key_drift"] += 1
        return {
            key: release_payload_from_locked_display(locked[key], generated[key], f"{path}.{key}", failures, events, tolerances)
            for key in sorted(locked_keys & generated_keys)
        }

    if isinstance(locked, list) and isinstance(generated, list):
        if len(locked) != len(generated):
            failures.append(f"{path}: list length mismatch locked={len(locked)} generated={len(generated)}")
            events["list_length_drift"] += 1
            return generated
        return [
            release_payload_from_locked_display(a, b, f"{path}[{idx}]", failures, events, tolerances)
            for idx, (a, b) in enumerate(zip(locked, generated))
        ]

    dec_locked = try_decimal(locked)
    dec_generated = try_decimal(generated)
    if dec_locked is not None and dec_generated is not None:
        abs_tol, rel_tol = tolerance_for(path, tolerances)
        if not decimal_close(dec_locked, dec_generated, abs_tol, rel_tol):
            failures.append(
                f"{path}: numeric drift locked={locked!r} generated={generated!r} diff={dec_generated - dec_locked} abs_tol={abs_tol} rel_tol={rel_tol}"
            )
            events["numeric_drift"] += 1
            return generated
        if str(locked) != str(generated):
            events["numeric_display_locked"] += 1
        return locked

    if dec_locked is not None or dec_generated is not None:
        failures.append(f"{path}: mixed numeric/text drift locked={locked!r} generated={generated!r}")
        events["mixed_numeric_text_drift"] += 1
        return generated

    if locked != generated:
        failures.append(f"{path}: text/metadata drift locked={locked!r} generated={generated!r}")
        events["text_or_metadata_drift"] += 1
        return generated

    return locked


def run_pair(pair: dict[str, Any], tolerances: dict[str, Any], out_dir: Path | None) -> dict[str, Any]:
    name = pair["name"]
    data_path = PAYLOAD_ROOT / pair["data_path"]
    code_path = PAYLOAD_ROOT / pair["code_path"]
    builder_name = pair.get("builder_function")

    if not data_path.exists():
        return {"name": name, "status": "FAIL", "failures": [f"missing data artifact: {pair['data_path']}"], "events": {"missing_file": 1}}
    if not code_path.exists():
        return {"name": name, "status": "FAIL", "failures": [f"missing generator: {pair['code_path']}"], "events": {"missing_file": 1}}

    locked = load_json(data_path)
    try:
        generated, resolved_builder = regenerate_payload(code_path, builder_name)
    except Exception as exc:
        return {"name": name, "status": "FAIL", "failures": [f"generator execution failed: {exc}"], "events": {"generator_execution_failed": 1}}

    normalized_generated, root_normalization = normalize_root_wrapper(locked, generated)
    failures: list[str] = []
    events: Counter = Counter()
    release_payload = release_payload_from_locked_display(
        locked,
        normalized_generated,
        pair["data_path"],
        failures,
        events,
        tolerances,
    )

    locked_release_text = canonical_text(locked)
    generated_release_text = canonical_text(release_payload)
    canonical_release_byte_equal = locked_release_text == generated_release_text
    raw_checked_in_byte_equal = data_path.read_text(encoding="utf-8") == generated_release_text

    if not canonical_release_byte_equal:
        failures.append(f"{name}: canonical release bytes differ after release policy normalization")
        events["canonical_release_byte_drift"] += 1

    if out_dir is not None and not failures:
        destination = out_dir / pair["data_path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(generated_release_text, encoding="utf-8")

    return {
        "name": name,
        "data_path": pair["data_path"],
        "code_path": pair["code_path"],
        "resolved_builder": resolved_builder,
        "status": "PASS" if not failures else "FAIL",
        "canonical_release_byte_equal": canonical_release_byte_equal,
        "raw_checked_in_byte_equal": raw_checked_in_byte_equal,
        "root_wrapper_normalization": root_normalization,
        "events": dict(sorted(events.items())),
        "failures": failures,
    }


def summarize_root_normalization(results: list[dict[str, Any]]) -> dict[str, Any]:
    added = Counter()
    removed = Counter()
    pairs: list[str] = []
    for result in results:
        info = result.get("root_wrapper_normalization", {})
        if not info.get("applied"):
            continue
        pairs.append(result.get("name", "UNKNOWN_PAIR"))
        for key in info.get("added_from_locked", []):
            added[key] += 1
        for key in info.get("removed_from_generated", []):
            removed[key] += 1
    return {
        "pairs_normalized": len(pairs),
        "added_from_locked_key_counts": dict(sorted(added.items())),
        "removed_from_generated_key_counts": dict(sorted(removed.items())),
        "pairs": pairs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PR-III canonical release byte-exact regeneration audit.")
    parser.add_argument("--pairs", default=str(PAIR_MANIFEST), help="Pair manifest path")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument(
        "--write-release-tree",
        default=None,
        help="Optional output directory for regenerated canonical release artifacts. Files are written only for passing pairs.",
    )
    args = parser.parse_args()

    pair_manifest = load_json(Path(args.pairs))
    policy = load_json(POLICY_MANIFEST) if POLICY_MANIFEST.exists() else {}
    tolerances = load_tolerances()
    out_dir = Path(args.write_release_tree) if args.write_release_tree else None

    results = [run_pair(pair, tolerances, out_dir) for pair in pair_manifest.get("pairs", [])]
    failures = [result for result in results if result["status"] != "PASS"]
    event_counts = Counter()
    for result in results:
        event_counts.update(result.get("events", {}))

    canonical_matches = sum(1 for result in results if result.get("canonical_release_byte_equal") is True)
    raw_matches = sum(1 for result in results if result.get("raw_checked_in_byte_equal") is True)

    summary = {
        "project": "Projection Relativity III",
        "audit": "canonical_release_byte_exact_regeneration_audit",
        "status": "PASS" if not failures else "FAIL",
        "pairs_checked": len(results),
        "pairs_passed": len(results) - len(failures),
        "pairs_failed": len(failures),
        "canonical_release_byte_exact_claimed": not failures,
        "raw_checked_in_file_order_byte_exact_claimed": False,
        "raw_generator_stdout_byte_exact_claimed": False,
        "numeric_tolerance_relaxed": False,
        "schema_numeric_reproducibility_required": True,
        "canonical_release_byte_matches": canonical_matches,
        "raw_checked_in_byte_matches": raw_matches,
        "event_counts": dict(sorted(event_counts.items())),
        "mechanical_root_wrapper_normalization": summarize_root_normalization(results),
        "release_tree_written": None if out_dir is None else str(out_dir),
        "policy": policy,
        "results": results,
    }

    if args.json:
        print(canonical_text(summary), end="")
        return

    print(f"PR-III canonical release byte-exact audit: {summary['status']}")
    print(f"pairs checked: {summary['pairs_checked']}; passed: {summary['pairs_passed']}; failed: {summary['pairs_failed']}")
    print(f"canonical release byte matches: {canonical_matches}/{summary['pairs_checked']}")
    print(f"raw checked-in file-order byte matches: {raw_matches}/{summary['pairs_checked']} (not the release claim)")
    print("event counts:")
    for key, value in sorted(event_counts.items()):
        print(f"- {key}: {value}")
    root = summary["mechanical_root_wrapper_normalization"]
    print("mechanical root wrapper normalization:")
    print(f"- pairs_normalized: {root['pairs_normalized']}")
    for key, value in root["added_from_locked_key_counts"].items():
        print(f"- added_from_locked.{key}: {value}")
    for key, value in root["removed_from_generated_key_counts"].items():
        print(f"- removed_from_generated.{key}: {value}")
    for result in results:
        mark = "PASS" if result["status"] == "PASS" else "FAIL"
        print(f"- {mark}: {result['name']}")
        for failure in result.get("failures", []):
            print(f"  failure: {failure}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
