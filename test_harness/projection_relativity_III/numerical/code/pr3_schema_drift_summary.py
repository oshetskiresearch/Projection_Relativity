#!/usr/bin/env python3
"""
Summarize PR-III artifact schema drift after the builder-exposure layer is gone.

Input is the JSON emitted by scripts/pr3_artifact_drift_audit.py --json.
This tool does not relax or pass any reproducibility gate. It classifies the
remaining schema-drift surface so the next hardening pass can distinguish:

- mechanical top-level wrapper drift,
- nested structural schema drift,
- numeric drift beyond policy,
- formatting-only numeric drift,
- list/value/mixed representation mismatches.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reports" / "pr3_artifact_drift_audit_pass_006.json"

MISSING_RE = re.compile(r"^(?P<path>.+?): missing keys in generated artifact: \[(?P<keys>.*)\]$")
EXTRA_RE = re.compile(r"^(?P<path>.+?): extra keys in generated artifact: \[(?P<keys>.*)\]$")
NUMERIC_RE = re.compile(r"^(?P<path>.+?): numeric drift ")
VALUE_RE = re.compile(r"^(?P<path>.+?): value mismatch ")
MIXED_RE = re.compile(r"^(?P<path>.+?): mixed numeric/text drift ")
LIST_RE = re.compile(r"^(?P<path>.+?): list length mismatch ")

COMMON_TOP_LEVEL_WRAPPER_KEYS = {"dataset", "input_policy"}
COMMON_TOP_LEVEL_EXTRA_KEYS = {"module"}


def read_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    # Windows PowerShell redirection can write UTF-16LE; normal repo JSON should
    # be UTF-8. Try the common encodings explicitly.
    for encoding in ("utf-8-sig", "utf-16", "utf-8"):
        try:
            return json.loads(raw.decode(encoding))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise RuntimeError(f"Could not decode JSON input: {path}")


def parse_key_list(raw: str) -> list[str]:
    if not raw.strip():
        return []
    try:
        parsed = ast.literal_eval("[" + raw + "]")
        return [str(item) for item in parsed]
    except Exception:
        return [item.strip().strip("'\"") for item in raw.split(",") if item.strip()]


def is_top_level_path(path: str) -> bool:
    return path.endswith(".json") and ".json." not in path


def add_pair(mapping: defaultdict[str, list[str]], key: str, name: str) -> None:
    if name not in mapping[key]:
        mapping[key].append(name)


def summarize(payload: dict[str, Any]) -> dict[str, Any]:
    results = payload.get("results", [])

    top_missing = Counter()
    top_extra = Counter()
    nested_missing = Counter()
    nested_extra = Counter()
    event_counts = Counter()
    key_to_pairs: defaultdict[str, list[str]] = defaultdict(list)

    numeric_drift_pairs: set[str] = set()
    value_mismatch_pairs: set[str] = set()
    mixed_numeric_text_pairs: set[str] = set()
    list_length_pairs: set[str] = set()
    top_level_wrapper_pairs: set[str] = set()
    nested_schema_pairs: set[str] = set()
    script_stdout_pairs: set[str] = set()
    pass_pairs: list[str] = []

    per_pair: list[dict[str, Any]] = []

    for result in results:
        name = result.get("name", "UNKNOWN_PAIR")
        if result.get("status") == "PASS":
            pass_pairs.append(name)
        if result.get("resolved_builder") == "__script_stdout__":
            script_stdout_pairs.add(name)

        pair_missing_top = Counter()
        pair_extra_top = Counter()
        pair_missing_nested = Counter()
        pair_extra_nested = Counter()
        pair_counts = Counter()

        for failure in result.get("failures", []):
            missing = MISSING_RE.match(failure)
            extra = EXTRA_RE.match(failure)
            numeric = NUMERIC_RE.match(failure)
            value = VALUE_RE.match(failure)
            mixed = MIXED_RE.match(failure)
            list_mismatch = LIST_RE.match(failure)

            if missing:
                keys = parse_key_list(missing.group("keys"))
                path = missing.group("path")
                if is_top_level_path(path):
                    event_counts["top_level_missing_key_events"] += 1
                    pair_counts["top_level_missing_key_events"] += 1
                    for key in keys:
                        top_missing[key] += 1
                        pair_missing_top[key] += 1
                        add_pair(key_to_pairs, f"top_missing:{key}", name)
                else:
                    event_counts["nested_missing_key_events"] += 1
                    pair_counts["nested_missing_key_events"] += 1
                    nested_schema_pairs.add(name)
                    for key in keys:
                        nested_missing[key] += 1
                        pair_missing_nested[key] += 1
                        add_pair(key_to_pairs, f"nested_missing:{key}", name)
                continue

            if extra:
                keys = parse_key_list(extra.group("keys"))
                path = extra.group("path")
                if is_top_level_path(path):
                    event_counts["top_level_extra_key_events"] += 1
                    pair_counts["top_level_extra_key_events"] += 1
                    for key in keys:
                        top_extra[key] += 1
                        pair_extra_top[key] += 1
                        add_pair(key_to_pairs, f"top_extra:{key}", name)
                else:
                    event_counts["nested_extra_key_events"] += 1
                    pair_counts["nested_extra_key_events"] += 1
                    nested_schema_pairs.add(name)
                    for key in keys:
                        nested_extra[key] += 1
                        pair_extra_nested[key] += 1
                        add_pair(key_to_pairs, f"nested_extra:{key}", name)
                continue

            if numeric:
                event_counts["numeric_drift_events"] += 1
                pair_counts["numeric_drift_events"] += 1
                numeric_drift_pairs.add(name)
                continue

            if value:
                event_counts["value_mismatch_events"] += 1
                pair_counts["value_mismatch_events"] += 1
                value_mismatch_pairs.add(name)
                continue

            if mixed:
                event_counts["mixed_numeric_text_events"] += 1
                pair_counts["mixed_numeric_text_events"] += 1
                mixed_numeric_text_pairs.add(name)
                continue

            if list_mismatch:
                event_counts["list_length_mismatch_events"] += 1
                pair_counts["list_length_mismatch_events"] += 1
                list_length_pairs.add(name)
                continue

            event_counts["unparsed_failure_events"] += 1
            pair_counts["unparsed_failure_events"] += 1

        common_missing = COMMON_TOP_LEVEL_WRAPPER_KEYS & set(pair_missing_top)
        common_extra = COMMON_TOP_LEVEL_EXTRA_KEYS & set(pair_extra_top)
        if common_missing or common_extra:
            top_level_wrapper_pairs.add(name)

        if result.get("failure_class") == "schema_drift" or result.get("status") == "PASS":
            per_pair.append(
                {
                    "name": name,
                    "status": result.get("status"),
                    "failure_class": result.get("failure_class"),
                    "resolved_builder": result.get("resolved_builder"),
                    "top_level_missing_keys": dict(sorted(pair_missing_top.items())),
                    "top_level_extra_keys": dict(sorted(pair_extra_top.items())),
                    "nested_missing_keys": dict(sorted(pair_missing_nested.items())),
                    "nested_extra_keys": dict(sorted(pair_extra_nested.items())),
                    "event_counts": dict(sorted(pair_counts.items())),
                }
            )

    priority = [
        {
            "rank": 1,
            "bucket": "mechanical_top_level_wrapper_drift",
            "criterion": "missing dataset/input_policy and/or extra module at artifact root",
            "pair_count": len(top_level_wrapper_pairs),
            "pairs": sorted(top_level_wrapper_pairs),
        },
        {
            "rank": 2,
            "bucket": "nested_structural_schema_drift",
            "criterion": "missing/extra keys below artifact root",
            "pair_count": len(nested_schema_pairs),
            "pairs": sorted(nested_schema_pairs),
        },
        {
            "rank": 3,
            "bucket": "numeric_drift_beyond_policy",
            "criterion": "numeric drift failures at current tolerance policy",
            "pair_count": len(numeric_drift_pairs),
            "pairs": sorted(numeric_drift_pairs),
        },
        {
            "rank": 4,
            "bucket": "representation_mismatch",
            "criterion": "value, mixed numeric/text, or list-length mismatch",
            "pair_count": len(value_mismatch_pairs | mixed_numeric_text_pairs | list_length_pairs),
            "pairs": sorted(value_mismatch_pairs | mixed_numeric_text_pairs | list_length_pairs),
        },
        {
            "rank": 5,
            "bucket": "canonical_numeric_formatting",
            "criterion": "warnings only; handle after schema/numeric failures",
            "pair_count": sum(1 for result in results if result.get("warnings")),
        },
    ]

    return {
        "project": payload.get("project", "Projection Relativity III"),
        "source_audit": payload.get("audit", "artifact_drift_audit"),
        "source_status": payload.get("status"),
        "source_counts": {
            "pairs_checked": payload.get("pairs_checked"),
            "pairs_passed": payload.get("pairs_passed"),
            "pairs_failed": payload.get("pairs_failed"),
            "failure_class_counts": payload.get("failure_class_counts", {}),
        },
        "summary_status": "SCHEMA_DRIFT_TRIAGE_GENERATED",
        "top_level_missing_key_counts": dict(top_missing.most_common()),
        "top_level_extra_key_counts": dict(top_extra.most_common()),
        "nested_missing_key_counts": dict(nested_missing.most_common()),
        "nested_extra_key_counts": dict(nested_extra.most_common()),
        "event_counts": dict(sorted(event_counts.items())),
        "pass_pairs": pass_pairs,
        "script_stdout_pairs": sorted(script_stdout_pairs),
        "priority_buckets": priority,
        "per_pair": per_pair,
        "key_to_pairs": dict(sorted((key, sorted(value)) for key, value in key_to_pairs.items())),
        "claims": {
            "changes_reproducibility_gate": False,
            "byte_exact_release_claimed": False,
            "full_schema_reproducibility_claimed": False,
        },
    }


def print_text(summary: dict[str, Any]) -> None:
    counts = summary["source_counts"]
    print("PR-III schema drift summary")
    print(f"source status: {summary['source_status']}")
    print(
        "pairs checked: {pairs_checked}; passed: {pairs_passed}; failed: {pairs_failed}".format(
            **counts
        )
    )
    print("failure classes:")
    for key, value in sorted(counts.get("failure_class_counts", {}).items()):
        print(f"- {key}: {value}")
    print("\nTop-level missing keys:")
    for key, value in list(summary["top_level_missing_key_counts"].items())[:20]:
        print(f"- {key}: {value}")
    print("\nTop-level extra keys:")
    for key, value in list(summary["top_level_extra_key_counts"].items())[:20]:
        print(f"- {key}: {value}")
    print("\nEvent counts:")
    for key, value in summary["event_counts"].items():
        print(f"- {key}: {value}")
    print("\nPriority buckets:")
    for bucket in summary["priority_buckets"]:
        print(f"{bucket['rank']}. {bucket['bucket']}: {bucket.get('pair_count', 0)} pairs")
    print("\nClaims: no reproducibility gate changed; byte-exact release still not claimed.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize PR-III schema drift from artifact drift audit JSON.")
    parser.add_argument("audit_json", nargs="?", default=str(DEFAULT_INPUT), help="artifact drift audit JSON path")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    payload = read_json(Path(args.audit_json))
    summary = summarize(payload)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        print_text(summary)


if __name__ == "__main__":
    main()
