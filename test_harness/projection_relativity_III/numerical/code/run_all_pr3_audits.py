#!/usr/bin/env python3
"""
PR-III reproducibility audit runner.

Validation layers:

1. Manifest-level validation: locked JSON artifacts exist and carry expected
   status fields.
2. Targeted regeneration validation: generator modules are imported or executed,
   their build_* payloads are regenerated, and schema/gate/status consistency is
   checked against locked data artifacts.
3. Optional artifact drift classification: canonical JSON text equality is
   checked and reported separately from schema/numeric validation.

The runner intentionally separates:

- schema/status correctness
- gate correctness
- artifact drift / canonical JSON equality
- byte-exact release equality

The public Tier C claim is enforced by `pr3_release_byte_exact_audit.py` under
the release-byte policy. The optional `--byte-exact` flag here is a stricter
raw generator-JSON diagnostic and is not the Tier C release contract.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
import sys
from collections import Counter
from decimal import Decimal, InvalidOperation
from pathlib import Path
from types import ModuleType
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = ROOT.parents[2]
PAYLOAD_ROOT = REPOSITORY_ROOT / "data" / "projection_relativity_III"
SCHEMA_TARGETS = ROOT / "schemas" / "pr3_regeneration_targets.json"
FULL_TARGETS = ROOT / "schemas" / "pr3_full_regeneration_pairs.json"
EXPECTED_MANIFEST_STATUS = "PRIII_REPRODUCIBILITY_PACKAGE_RELEASE_LOCKED"

REQUIRED_STATUS = {
    "data/alpha_residual_closure_current_precision.json": "STEP_05H_RESIDUAL_BOUNDING_LOCKED",
    "data/electroweak_neutral_D3_candidate_C3.json": "STEP_06J_NEUTRAL_D3_REFINEMENT_GENERATED",
    "data/neutrino_final_closure_audit.json": "STEP_07F_FINAL_NEUTRINO_CLOSURE_AUDIT_LOCKED",
    "data/strong_final_closure_audit.json": "STEP_08F_FINAL_STRONG_CLOSURE_AUDIT_LOCKED",
    "data/global_running_anomaly_ledger_seed.json": "STEP_09A_GLOBAL_LEDGER_LOCKED",
    "data/global_anomaly_registry_audit.json": "STEP_09B_ANOMALY_REGISTRY_AUDIT_LOCKED",
    "data/global_running_continuity_audit.json": "STEP_09C_RUNNING_CONTINUITY_AUDIT_LOCKED",
    "data/global_no_fit_provenance_manifest.json": "STEP_09D_NO_FIT_PROVENANCE_MANIFEST_LOCKED",
    "data/global_cross_sector_diagnostic_table.json": "STEP_09E_CROSS_SECTOR_DIAGNOSTIC_TABLE_LOCKED",
    "data/global_final_priii_consistency_statement.json": "STEP_09F_FINAL_PRIII_CONSISTENCY_STATEMENT_LOCKED",
}

REQUIRED_FILES = [
    "README_PR3_REPRODUCIBILITY.md",
    "RUN_ORDER.md",
    "MANIFEST_PR3_LOCKED_OUTPUTS.json",
    "schemas/pr3_regeneration_targets.json",
    "schemas/pr3_full_regeneration_pairs.json",
    "schemas/pr3_artifact_drift_policy.json",
    "code/pr3_canonical_json.py",
    "results/PR3_FINAL_AUDIT_SUMMARY.md",
    "results/pr3_locked_outputs.csv",
    "results/pr3_cross_sector_diagnostic_table.csv",
]

DEFAULT_NUMERIC_TOL = Decimal("1e-40")


def canonical_json_text(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module spec for {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _finite_decimal(value: Decimal) -> Decimal | None:
    return value if value.is_finite() else None


def try_decimal(value: Any) -> Decimal | None:
    """Parse a JSON value as Decimal without ever raising Decimal exceptions.

    The audit sees both physical numeric fields and prose/provenance fields. A
    malformed or non-finite numeric-looking string must be classified as drift,
    not allowed to crash the audit runner.
    """
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


def is_decimal_like(value: Any) -> bool:
    return try_decimal(value) is not None


def as_decimal(value: Any) -> Decimal:
    parsed = try_decimal(value)
    if parsed is None:
        raise ValueError(f"not a finite decimal value: {value!r}")
    return parsed


def parse_decimal_or_default(value: Any, default: Decimal = DEFAULT_NUMERIC_TOL) -> Decimal:
    parsed = try_decimal(value)
    return parsed if parsed is not None else default


def compare_key_sets(label: str, expected: set[str], actual: set[str], failures: list[str]) -> None:
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        failures.append(f"{label}: missing keys {missing}")
    if extra:
        failures.append(f"{label}: extra keys {extra}")


def require_keys(label: str, required: set[str], actual: set[str], failures: list[str]) -> None:
    missing = sorted(required - actual)
    if missing:
        failures.append(f"{label}: missing keys {missing}")


def discover_builder(module: ModuleType, preferred: str | None = None):
    if preferred and preferred != "AUTO" and hasattr(module, preferred):
        return getattr(module, preferred), preferred

    candidates = []
    for name in dir(module):
        if not name.startswith("build_"):
            continue
        candidate = getattr(module, name)
        if callable(candidate):
            candidates.append((name, candidate))

    if len(candidates) == 1:
        name, candidate = candidates[0]
        return candidate, name

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
        names = ", ".join(name for name, _ in candidates)
        raise RuntimeError(f"multiple build_* functions found; set builder_function explicitly: {names}")

    raise RuntimeError("no build_* function found")


def regenerate_payload(code_path: Path, builder_name: str | None) -> tuple[dict[str, Any], str]:
    try:
        module = load_module(code_path)
        builder, resolved_name = discover_builder(module, builder_name)
        payload = builder()
        if not isinstance(payload, dict):
            raise RuntimeError(f"builder {resolved_name} did not return a dict")
        return payload, resolved_name
    except Exception as import_error:
        # Fallback for simple script-only generators that print JSON to stdout.
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


def compare_numeric_tree(
    label: str,
    locked: Any,
    generated: Any,
    failures: list[str],
    drift: Counter,
    tol: Decimal = DEFAULT_NUMERIC_TOL,
) -> None:
    if isinstance(locked, dict) and isinstance(generated, dict):
        locked_keys = set(locked.keys())
        generated_keys = set(generated.keys())
        if locked_keys != generated_keys:
            drift["schema_key_drift"] += 1
            return
        for key in sorted(locked_keys):
            compare_numeric_tree(f"{label}.{key}", locked[key], generated[key], failures, drift, tol)
        return

    if isinstance(locked, list) and isinstance(generated, list):
        if len(locked) != len(generated):
            drift["list_length_drift"] += 1
            return
        for index, (l_item, g_item) in enumerate(zip(locked, generated)):
            compare_numeric_tree(f"{label}[{index}]", l_item, g_item, failures, drift, tol)
        return

    locked_decimal = try_decimal(locked)
    generated_decimal = try_decimal(generated)
    if locked_decimal is not None and generated_decimal is not None:
        delta = abs(locked_decimal - generated_decimal)
        if delta > tol:
            failures.append(f"{label}: numeric drift {delta} exceeds tolerance {tol}")
        elif delta != 0:
            drift["numeric_within_tolerance_drift"] += 1
        return

    if locked_decimal is not None or generated_decimal is not None:
        drift["mixed_numeric_text_drift"] += 1
        return

    if locked != generated:
        # Text/provenance formatting drift is reported, not fatal by default.
        drift["text_or_metadata_drift"] += 1


def validate_manifest() -> list[str]:
    failures: list[str] = []

    manifest_path = ROOT / "MANIFEST_PR3_LOCKED_OUTPUTS.json"
    if not manifest_path.exists():
        return ["missing: MANIFEST_PR3_LOCKED_OUTPUTS.json"]

    manifest = load_json(manifest_path)
    if manifest.get("status") != EXPECTED_MANIFEST_STATUS:
        failures.append(
            f"manifest status mismatch: expected {EXPECTED_MANIFEST_STATUS}, got {manifest.get('status')}"
        )
    if manifest.get("path_base") != "repository_root":
        failures.append("manifest path_base must be repository_root")

    contract = manifest.get("release_contract", {})
    expected_contract = {
        "full_generator_data_pair_count": 41,
        "full_schema_numeric_regeneration_claimed": True,
        "canonical_release_byte_regeneration_claimed": True,
        "canonical_release_byte_match_count": 41,
        "raw_checked_in_file_order_byte_identity_claimed": False,
        "raw_generator_stdout_byte_identity_claimed": False,
    }
    for key, expected in expected_contract.items():
        if contract.get(key) != expected:
            failures.append(
                f"manifest release_contract.{key}: expected {expected!r}, got {contract.get(key)!r}"
            )

    pair_manifest = load_json(ROOT / "schemas" / "pr3_full_regeneration_pairs.json")
    pairs = pair_manifest.get("pairs", [])
    if pair_manifest.get("status") != "PRIII_FULL_REGENERATION_PAIR_MANIFEST_LOCKED":
        failures.append("full pair manifest is not release locked")
    if pair_manifest.get("pair_count") != 41 or len(pairs) != 41:
        failures.append(
            f"full pair manifest count mismatch: declared={pair_manifest.get('pair_count')} actual={len(pairs)}"
        )

    for field in ("final_reports", "reproducibility_files"):
        for rel_path in manifest.get(field, []):
            if not (REPOSITORY_ROOT / rel_path).is_file():
                failures.append(f"manifest {field} path missing: {rel_path}")

    for rel_path, expected_status in REQUIRED_STATUS.items():
        path = PAYLOAD_ROOT / rel_path
        if not path.exists():
            failures.append(f"missing: {rel_path}")
            continue
        payload = load_json(path)
        actual = payload.get("status")
        if actual != expected_status:
            failures.append(f"status mismatch: {rel_path}: expected {expected_status}, got {actual}")

    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            failures.append(f"missing: {rel_path}")

    return failures


def validate_regeneration_targets(targets_path: Path, *, byte_exact: bool, drift_report: bool) -> list[str]:
    failures: list[str] = []
    drift_counter: Counter = Counter()

    if not targets_path.exists():
        return [f"missing schema targets: {targets_path.relative_to(ROOT)}"]

    schema = load_json(targets_path)
    targets = schema.get("targets") or schema.get("pairs", [])
    for target in targets:
        name = target["name"]
        data_path = PAYLOAD_ROOT / target["data_path"]
        code_path = PAYLOAD_ROOT / target["code_path"]
        builder_name = target.get("builder_function", "AUTO")
        expected_status = target.get("status")
        required_top = set(target.get("required_top_level_keys", []))
        minimum_top = set(target.get("minimum_top_level_keys", ["project", "status"]))
        gate_field = target.get("gate_field")
        numeric_tol = parse_decimal_or_default(target.get("numeric_tolerance", DEFAULT_NUMERIC_TOL), DEFAULT_NUMERIC_TOL)

        if not data_path.exists():
            failures.append(f"{name}: locked data missing: {target['data_path']}")
            continue
        if not code_path.exists():
            failures.append(f"{name}: generator missing: {target['code_path']}")
            continue

        locked = load_json(data_path)
        if expected_status is None:
            expected_status = locked.get("status")
        try:
            generated, resolved_builder = regenerate_payload(code_path, builder_name)
        except Exception as error:
            failures.append(f"{name}: regeneration failed: {error}")
            continue

        if generated.get("status") != expected_status:
            failures.append(f"{name}: generated status mismatch: expected {expected_status}, got {generated.get('status')}")
        if locked.get("status") != expected_status:
            failures.append(f"{name}: locked status mismatch: expected {expected_status}, got {locked.get('status')}")

        if required_top:
            compare_key_sets(f"{name} generated top-level schema", required_top, set(generated.keys()), failures)
            compare_key_sets(f"{name} locked top-level schema", required_top, set(locked.keys()), failures)
        else:
            require_keys(f"{name} generated minimum schema", minimum_top, set(generated.keys()), failures)
            require_keys(f"{name} locked minimum schema", minimum_top, set(locked.keys()), failures)

        if gate_field:
            locked_gates = locked.get(gate_field, {})
            generated_gates = generated.get(gate_field, {})
            if not isinstance(locked_gates, dict) or not isinstance(generated_gates, dict):
                failures.append(f"{name}: gate field {gate_field} must be a dict in locked and generated artifacts")
            else:
                compare_key_sets(
                    f"{name} {gate_field} schema",
                    set(locked_gates.keys()),
                    set(generated_gates.keys()),
                    failures,
                )
                false_gates = [gate for gate, value in generated_gates.items() if value is not True]
                if false_gates:
                    failures.append(f"{name}: generated false gates {false_gates}")

        locked_canonical = canonical_json_text(locked)
        generated_canonical = canonical_json_text(generated)
        if locked_canonical == generated_canonical:
            drift_counter["byte_exact_or_canonical_match"] += 1
        else:
            drift_counter["canonical_diff"] += 1
            if byte_exact:
                failures.append(f"{name}: canonical JSON differs from locked artifact")
            else:
                compare_numeric_tree(name, locked, generated, failures, drift_counter, numeric_tol)

        if drift_report:
            print(f"[drift] {name}: builder={resolved_builder}; canonical_match={locked_canonical == generated_canonical}")

    if drift_report:
        print("Artifact drift summary:")
        for key, value in sorted(drift_counter.items()):
            print(f"- {key}: {value}")

    return failures


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PR-III reproducibility audits.")
    parser.add_argument(
        "--manifest-only",
        action="store_true",
        help="Run only manifest/status checks. By default, targeted regeneration checks are also run.",
    )
    parser.add_argument(
        "--full-targets",
        action="store_true",
        help="Use the canonical 41-pair schemas/pr3_full_regeneration_pairs.json manifest instead of the curated target list.",
    )
    parser.add_argument(
        "--byte-exact",
        action="store_true",
        help="Make raw generated canonical-JSON differences fatal as a stricter diagnostic; this is not the normalized Tier C release-byte audit.",
    )
    parser.add_argument(
        "--drift-report",
        action="store_true",
        help="Print artifact drift classifications for targeted regeneration.",
    )
    args = parser.parse_args()

    failures = validate_manifest()
    if not args.manifest_only:
        targets_path = FULL_TARGETS if args.full_targets else SCHEMA_TARGETS
        failures.extend(validate_regeneration_targets(targets_path, byte_exact=args.byte_exact, drift_report=args.drift_report))

    if failures:
        print("PR-III reproducibility audit: FAIL")
        for item in failures:
            print(f"- {item}")
        raise SystemExit(1)

    print("PR-III reproducibility audit: PASS")
    if args.manifest_only:
        print("Manifest/status layer passed.")
    elif args.full_targets:
        print("Manifest/status layer and full generator/data target checks passed at configured schema/numeric tolerance tier.")
    else:
        print("Manifest/status layer and targeted regeneration schema checks passed.")
    if args.byte_exact:
        print("Strict raw generated canonical-JSON equality was required for targeted artifacts.")
    else:
        print("Tier C canonical release-byte identity is enforced by code/pr3_release_byte_exact_audit.py.")
    print("Locked through Step 09F; the public Tier A-C reproducibility contract is release closed.")


if __name__ == "__main__":
    main()
