#!/usr/bin/env python3
"""
Summarize and classify PR-III numeric drift after schema drift is cleared.

Input is the JSON emitted by scripts/pr3_artifact_drift_audit.py --json.
This tool does not change any reproducibility gate and does not relax numeric
policy. It separates:

- locked diagnostic/display rounding tails,
- true generated-value drift candidates,
- unclassified numeric drift,
- numeric-formatting-only warnings.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reports" / "pr3_artifact_drift_audit_pass_013.json"

NUMERIC_FAILURE_RE = re.compile(
    r"^(?P<path>.+?): numeric drift locked='(?P<locked>.*?)' generated='(?P<generated>.*?)' "
    r"diff=(?P<diff>\S+) abs_tol=(?P<abs_tol>\S+) rel_tol=(?P<rel_tol>\S+)$"
)
NUMERIC_FORMAT_WARNING_RE = re.compile(r"^(?P<path>.+?): numeric formatting drift locked='(?P<locked>.*?)' generated='(?P<generated>.*?)'$")

ROUNDING_ONLY_FIELDS = {
    "data/alpha_radiative_candidate_minimal_boundary.json.diagnostic_comparison.diagnostic_shift_capture_fraction": {
        "classification": "locked_diagnostic_rounding_tail",
        "locked_display_places": 12,
        "recommended_action": "emit diagnostic capture fraction at the locked display precision",
    },
    "data/alpha_radiative_candidate_minimal_boundary.json.diagnostic_comparison.diagnostic_shift_capture_percent": {
        "classification": "locked_diagnostic_rounding_tail",
        "locked_display_places": 10,
        "recommended_action": "emit diagnostic capture percent at the locked display precision",
    },
    "data/alpha_radiative_candidate_D1_D2.json.diagnostic_comparison.diagnostic_shift_capture_fraction": {
        "classification": "locked_diagnostic_rounding_tail",
        "locked_display_places": 15,
        "recommended_action": "emit diagnostic capture fraction at the locked display precision",
    },
    "data/alpha_radiative_candidate_D1_D2.json.diagnostic_comparison.diagnostic_shift_capture_percent": {
        "classification": "locked_diagnostic_rounding_tail",
        "locked_display_places": 13,
        "recommended_action": "emit diagnostic capture percent at the locked display precision",
    },
    "data/neutrino_ordering_pmns_stability_audit.json.pmns_branch.theta23_deg": {
        "classification": "locked_angle_display_rounding_tail",
        "locked_display_places": 14,
        "recommended_action": "emit theta23_deg at the locked display precision",
    },
}

TRUE_VALUE_DRIFT_FIELDS = {
    "data/electroweak_running_candidate_C1.json.derived_transport.alpha_PR_C1_muEW",
    "data/electroweak_running_candidate_C1.json.weak_mass_ledger_C1.MW_squared_GeV2",
    "data/electroweak_running_candidate_C1.json.weak_mass_ledger_C1.MZ_squared_GeV2",
}


def read_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-16", "utf-8"):
        try:
            return json.loads(raw.decode(encoding))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise RuntimeError(f"Could not decode JSON input: {path}")


def decimal_or_none(raw: str) -> Decimal | None:
    try:
        return Decimal(raw)
    except (InvalidOperation, ValueError):
        return None


def decimal_places(raw: str) -> int | None:
    if "e" in raw.lower():
        return None
    if "." not in raw:
        return 0
    return len(raw.split(".", 1)[1])


def rounded_string_matches(locked: str, generated: str, places: int | None) -> bool | None:
    if places is None:
        return None
    generated_decimal = decimal_or_none(generated)
    locked_decimal = decimal_or_none(locked)
    if generated_decimal is None or locked_decimal is None:
        return None
    return format(generated_decimal, f".{places}f") == locked


def classify_numeric_failure(pair_name: str, failure: str) -> dict[str, Any]:
    match = NUMERIC_FAILURE_RE.match(failure)
    if not match:
        return {
            "pair": pair_name,
            "classification": "unparsed_numeric_failure",
            "raw_failure": failure,
        }

    path = match.group("path")
    locked = match.group("locked")
    generated = match.group("generated")
    diff = match.group("diff")
    locked_places = decimal_places(locked)

    if path in ROUNDING_ONLY_FIELDS:
        policy = ROUNDING_ONLY_FIELDS[path]
        places = policy.get("locked_display_places")
        return {
            "pair": pair_name,
            "path": path,
            "locked": locked,
            "generated": generated,
            "diff": diff,
            "classification": policy["classification"],
            "locked_display_places": places,
            "generated_rounds_to_locked": rounded_string_matches(locked, generated, places),
            "recommended_action": policy["recommended_action"],
            "gate_action": "format generator output to locked display precision; do not relax tolerance",
        }

    if path in TRUE_VALUE_DRIFT_FIELDS:
        return {
            "pair": pair_name,
            "path": path,
            "locked": locked,
            "generated": generated,
            "diff": diff,
            "classification": "true_generated_value_drift_candidate",
            "locked_display_places": locked_places,
            "generated_rounds_to_locked": rounded_string_matches(locked, generated, locked_places),
            "recommended_action": "investigate generator/source provenance; do not accept by display rounding",
            "gate_action": "remain failing until generator and locked artifact provenance are reconciled",
        }

    return {
        "pair": pair_name,
        "path": path,
        "locked": locked,
        "generated": generated,
        "diff": diff,
        "classification": "unclassified_numeric_drift",
        "locked_display_places": locked_places,
        "generated_rounds_to_locked": rounded_string_matches(locked, generated, locked_places),
        "recommended_action": "manual review required",
        "gate_action": "remain failing",
    }


def summarize(payload: dict[str, Any]) -> dict[str, Any]:
    events: list[dict[str, Any]] = []
    warning_counts = Counter()
    warning_paths_by_pair: defaultdict[str, list[str]] = defaultdict(list)

    for result in payload.get("results", []):
        pair_name = result.get("name", "UNKNOWN_PAIR")
        for failure in result.get("failures", []):
            if "numeric drift" in failure:
                events.append(classify_numeric_failure(pair_name, failure))
        for warning in result.get("warnings", []):
            match = NUMERIC_FORMAT_WARNING_RE.match(warning)
            if not match:
                continue
            warning_counts[pair_name] += 1
            warning_paths_by_pair[pair_name].append(match.group("path"))

    class_counts = Counter(event.get("classification", "unknown") for event in events)
    pair_to_classes: defaultdict[str, set[str]] = defaultdict(set)
    for event in events:
        pair_to_classes[event["pair"]].add(event.get("classification", "unknown"))

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
        "summary_status": "NUMERIC_DRIFT_CLASSIFICATION_GENERATED",
        "numeric_failure_event_count": len(events),
        "classification_counts": dict(sorted(class_counts.items())),
        "pair_classification_counts": {pair: sorted(classes) for pair, classes in sorted(pair_to_classes.items())},
        "numeric_failure_events": events,
        "numeric_formatting_warning_counts_by_pair": dict(sorted(warning_counts.items())),
        "numeric_formatting_warning_paths_by_pair": {pair: paths for pair, paths in sorted(warning_paths_by_pair.items())},
        "claims": {
            "changes_reproducibility_gate": False,
            "relaxes_numeric_tolerance": False,
            "byte_exact_release_claimed": False,
            "full_numeric_reproducibility_claimed": False,
        },
    }


def print_text(summary: dict[str, Any]) -> None:
    counts = summary["source_counts"]
    print("PR-III numeric drift summary")
    print(f"source status: {summary['source_status']}")
    print(
        "pairs checked: {pairs_checked}; passed: {pairs_passed}; failed: {pairs_failed}".format(
            **counts
        )
    )
    print("numeric classification counts:")
    for key, value in summary["classification_counts"].items():
        print(f"- {key}: {value}")
    print("\nPair classifications:")
    for pair, classes in summary["pair_classification_counts"].items():
        print(f"- {pair}: {', '.join(classes)}")
    print("\nNumeric formatting warning counts by pair:")
    for pair, count in summary["numeric_formatting_warning_counts_by_pair"].items():
        print(f"- {pair}: {count}")
    print("\nClaims: no gate change, no tolerance relaxation, no byte-exact release claim.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize PR-III numeric drift from artifact drift audit JSON.")
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
