#!/usr/bin/env python3
"""Run the public PR-III Python/JSON reproducibility tester."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = ROOT.parents[2]
PAYLOAD_ROOT = REPOSITORY_ROOT / "data" / "projection_relativity_III"
DEFAULT_OUTPUT = ROOT / "results"
SCOPE_MANIFEST = ROOT / "PR3_NUMERICAL_SCOPE.json"
PAIR_MANIFEST = ROOT / "schemas" / "pr3_full_regeneration_pairs.json"
FORBIDDEN_SOURCE_TOKENS = ("pr4", "projection relativity iv")


@dataclass
class CheckResult:
    id: str
    category: str
    status: str
    actual: str
    expected: str
    detail: str


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def add_result(
    results: list[CheckResult],
    id_: str,
    category: str,
    passed: bool,
    actual: object,
    expected: object,
    detail: str,
) -> None:
    results.append(
        CheckResult(
            id=id_,
            category=category,
            status="PASS" if passed else "FAIL",
            actual=str(actual),
            expected=str(expected),
            detail=detail,
        )
    )


def relative_paths(paths: Iterable[Path], base: Path) -> list[str]:
    return sorted(path.relative_to(base).as_posix() for path in paths)


def repository_path(path: Path) -> str:
    try:
        return path.relative_to(REPOSITORY_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_scope(results: list[CheckResult]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    scope = read_json(SCOPE_MANIFEST)
    expected = scope["expected_counts"]

    groups = {
        "generator_python_files": sorted((PAYLOAD_ROOT / "code").glob("*.py")),
        "data_json_files": sorted((PAYLOAD_ROOT / "data").glob("*.json")),
        "schema_json_files": sorted((ROOT / "schemas").glob("*.json")),
        "audit_python_files": sorted((ROOT / "code").glob("*.py")),
    }
    for key, paths in groups.items():
        add_result(
            results,
            f"scope:{key}",
            "scope",
            len(paths) == int(expected[key]),
            len(paths),
            expected[key],
            f"Packaged {key.replace('_', ' ')}",
        )

    unexpected_code = [path for path in groups["generator_python_files"] if not path.name.startswith("pr3_")]
    add_result(
        results,
        "scope:generator_names",
        "scope",
        not unexpected_code,
        len(unexpected_code),
        0,
        "Every packaged generator must use the pr3_ filename prefix",
    )

    required_scripts = set(scope["required_audit_scripts"])
    actual_scripts = set(relative_paths(groups["audit_python_files"], ROOT))
    add_result(
        results,
        "scope:audit_scripts",
        "scope",
        actual_scripts == required_scripts,
        len(actual_scripts),
        len(required_scripts),
        "Audit utility set matches the locked public scope manifest",
    )

    pair_payload = read_json(PAIR_MANIFEST)
    pairs = pair_payload.get("pairs", [])
    pair_code_paths = {item["code_path"] for item in pairs}
    pair_data_paths = {item["data_path"] for item in pairs}
    actual_code_paths = set(relative_paths(groups["generator_python_files"], PAYLOAD_ROOT))
    actual_data_paths = set(relative_paths(groups["data_json_files"], PAYLOAD_ROOT))
    pair_ok = (
        len(pairs) == int(expected["regeneration_pairs"])
        and pair_code_paths == actual_code_paths
        and pair_data_paths.issubset(actual_data_paths)
    )
    add_result(
        results,
        "scope:regeneration_pairs",
        "scope",
        pair_ok,
        len(pairs),
        expected["regeneration_pairs"],
        "The 41-pair manifest covers every packaged generator and every locked pair exists",
    )

    support_paths = [ROOT / rel for rel in scope["required_support_files"]]
    missing_support = [path for path in support_paths if not path.is_file()]
    add_result(
        results,
        "scope:support_files",
        "scope",
        not missing_support,
        len(support_paths) - len(missing_support),
        len(support_paths),
        "Minimal Tier A support files are present",
    )

    payload_files = sorted(
        {path for paths in groups.values() for path in paths}.union(support_paths),
        key=lambda path: path.as_posix(),
    )
    forbidden_paths = [
        repository_path(path)
        for path in payload_files
        if "pr4" in repository_path(path).casefold()
    ]
    add_result(
        results,
        "scope:forbidden_paths",
        "scope",
        not forbidden_paths,
        len(forbidden_paths),
        0,
        "No PR4-labelled source path may enter the PR-III numerical package",
    )

    forbidden_references: list[str] = []
    for path in [item for paths in groups.values() for item in paths]:
        text = path.read_text(encoding="utf-8").casefold()
        if any(token in text for token in FORBIDDEN_SOURCE_TOKENS):
            forbidden_references.append(repository_path(path))
    add_result(
        results,
        "scope:forbidden_references",
        "scope",
        not forbidden_references,
        len(forbidden_references),
        0,
        "PR-III generators, JSON ledgers, schemas, and audit scripts contain no PR4 dependency",
    )

    inventory = [
        {
            "path": repository_path(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in payload_files
        if path.is_file()
    ]
    scope_summary = {
        "counts": {key: len(paths) for key, paths in groups.items()},
        "regeneration_pairs": len(pairs),
        "source_payload_files": len(inventory),
        "forbidden_paths": forbidden_paths,
        "forbidden_references": forbidden_references,
    }
    return scope_summary, inventory


def run_command(args: list[str], cwd: Path = ROOT) -> tuple[int, str]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONUTF8"] = "1"
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=str(cwd),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return proc.returncode, proc.stdout


def run_json_command(args: list[str], output_path: Path) -> tuple[int, dict[str, Any] | None, str]:
    returncode, output = run_command(args)
    try:
        payload = json.loads(output)
    except json.JSONDecodeError:
        return returncode, None, output
    write_json(output_path, payload)
    return returncode, payload, output


def write_inventory(path: Path, inventory: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "bytes", "sha256"])
        writer.writeheader()
        writer.writerows(inventory)


def output_reference(output_dir: Path) -> str:
    try:
        return output_dir.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return output_dir.name


def write_results(
    output_dir: Path,
    scope: dict[str, Any],
    inventory: list[dict[str, Any]],
    results: list[CheckResult],
    tier_data: dict[str, Any],
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    write_inventory(output_dir / "PR3_NUMERICAL_SOURCE_INVENTORY.csv", inventory)

    with (output_dir / "PR3_NUMERICAL_VALIDATION_RESULTS.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(results[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(item) for item in results)

    failed = [item for item in results if item.status != "PASS"]
    summary = {
        "project": "Projection Relativity III",
        "package": "public numerical reproducibility tester",
        "status": "PASS" if not failed else "FAIL",
        "checks_total": len(results),
        "checks_passed": len(results) - len(failed),
        "checks_failed": len(failed),
        "source_repository": "oshetskiresearch/Projection-Relativity_III_Sandbox",
        "source_snapshot_commit": read_json(SCOPE_MANIFEST)["source_snapshot_commit"],
        "output_directory": output_reference(output_dir),
        "source_scope": scope,
        "tiers": tier_data,
        "claim_boundary": read_json(SCOPE_MANIFEST)["claim_boundary"],
    }
    write_json(output_dir / "PR3_NUMERICAL_VALIDATION_SUMMARY.json", summary)

    artifact = tier_data.get("tier_b", {})
    release = tier_data.get("tier_c", {})
    lines = [
        "# PR-III Numerical Validation Summary",
        "",
        f"Status: **{summary['status']}**",
        "",
        f"- Checks: `{summary['checks_passed']}/{summary['checks_total']}` passed",
        f"- PR-III generators: `{scope.get('counts', {}).get('generator_python_files', 0)}`",
        f"- PR-III JSON ledgers: `{scope.get('counts', {}).get('data_json_files', 0)}`",
        f"- PR4-labelled source paths: `{len(scope.get('forbidden_paths', []))}`",
        f"- PR4 source references: `{len(scope.get('forbidden_references', []))}`",
        "",
        "## Reproducibility Tiers",
        "",
        f"- Tier A manifest/targeted audit: `{tier_data.get('tier_a', {}).get('status', 'NOT_RUN')}`",
        (
            "- Tier B schema/numeric pairs: "
            f"`{artifact.get('pairs_passed', 0)}/{artifact.get('pairs_checked', 0)} PASS`"
        ),
        (
            "- Tier C canonical release bytes: "
            f"`{release.get('canonical_release_byte_matches', 0)}/{release.get('pairs_checked', 0)} PASS`"
        ),
        f"- Numeric tolerance relaxed: `{'yes' if release.get('numeric_tolerance_relaxed') else 'no'}`",
        "- Raw generator stdout byte identity: `NOT_CLAIMED`",
        "- Raw checked-in file-order byte identity: `NOT_CLAIMED`",
        "",
        "## Interpretation",
        "",
        "Tier B permits documented decimal display-tail and mechanical root-wrapper accounting only when",
        "the locked numerical tolerance and nonnumeric structure remain satisfied. Tier C then requires",
        "the resulting canonical release JSON bytes to match for all declared pairs.",
        "",
    ]
    (output_dir / "PR3_NUMERICAL_VALIDATION_SUMMARY.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    return summary


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Report directory; relative paths are resolved from this tester directory",
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    results: list[CheckResult] = []
    scope, inventory = validate_scope(results)
    scope_ok = all(item.status == "PASS" for item in results)
    tier_data: dict[str, Any] = {}

    if scope_ok:
        tier_a_rc, tier_a_output = run_command(["code/run_all_pr3_audits.py"])
        (output_dir / "tier_a_manifest_audit.txt").write_text(tier_a_output, encoding="utf-8")
        tier_a_ok = tier_a_rc == 0 and "PR-III reproducibility audit: PASS" in tier_a_output
        add_result(
            results,
            "tier_a:manifest_targeted",
            "tier_a",
            tier_a_ok,
            tier_a_rc,
            0,
            "Manifest/status and targeted regeneration audit",
        )
        tier_data["tier_a"] = {"status": "PASS" if tier_a_ok else "FAIL", "returncode": tier_a_rc}

        artifact_rc, artifact, artifact_raw = run_json_command(
            ["code/pr3_artifact_drift_audit.py", "--json"],
            output_dir / "tier_b_artifact_drift_audit.json",
        )
        if artifact is None:
            (output_dir / "tier_b_artifact_drift_audit_error.txt").write_text(
                artifact_raw, encoding="utf-8"
            )
            artifact = {}
        artifact_ok = (
            artifact_rc == 0
            and artifact.get("status") == "PASS"
            and artifact.get("pairs_checked") == 41
            and artifact.get("pairs_passed") == 41
            and artifact.get("pairs_failed") == 0
            and artifact.get("byte_exact_release_claimed") is False
        )
        add_result(
            results,
            "tier_b:artifact_drift",
            "tier_b",
            artifact_ok,
            f"{artifact.get('pairs_passed', 0)}/{artifact.get('pairs_checked', 0)}",
            "41/41",
            "Full schema/numeric artifact reproducibility under locked tolerances",
        )

        artifact_path = output_dir / "tier_b_artifact_drift_audit.json"
        schema_rc, schema_summary, schema_raw = run_json_command(
            ["code/pr3_schema_drift_summary.py", str(artifact_path), "--json"],
            output_dir / "tier_b_schema_drift_summary.json",
        )
        if schema_summary is None:
            (output_dir / "tier_b_schema_drift_summary_error.txt").write_text(
                schema_raw, encoding="utf-8"
            )
            schema_summary = {}
        schema_counts = schema_summary.get("source_counts", {})
        schema_ok = (
            schema_rc == 0
            and schema_summary.get("source_status") == "PASS"
            and schema_counts.get("pairs_failed") == 0
        )
        add_result(
            results,
            "tier_b:schema_summary",
            "tier_b",
            schema_ok,
            schema_counts.get("pairs_failed", "missing"),
            0,
            "Schema drift accounting contains no failed generator/data pair",
        )

        numeric_rc, numeric_summary, numeric_raw = run_json_command(
            ["code/pr3_numeric_drift_summary.py", str(artifact_path), "--json"],
            output_dir / "tier_b_numeric_drift_summary.json",
        )
        if numeric_summary is None:
            (output_dir / "tier_b_numeric_drift_summary_error.txt").write_text(
                numeric_raw, encoding="utf-8"
            )
            numeric_summary = {}
        numeric_ok = (
            numeric_rc == 0
            and numeric_summary.get("source_status") == "PASS"
            and numeric_summary.get("numeric_failure_event_count") == 0
            and numeric_summary.get("claims", {}).get("relaxes_numeric_tolerance") is False
        )
        add_result(
            results,
            "tier_b:numeric_summary",
            "tier_b",
            numeric_ok,
            numeric_summary.get("numeric_failure_event_count", "missing"),
            0,
            "No numerical drift event exceeds the locked policy",
        )
        tier_data["tier_b"] = {
            "status": "PASS" if artifact_ok and schema_ok and numeric_ok else "FAIL",
            "pairs_checked": artifact.get("pairs_checked", 0),
            "pairs_passed": artifact.get("pairs_passed", 0),
            "pairs_failed": artifact.get("pairs_failed", 0),
            "numeric_failure_event_count": numeric_summary.get("numeric_failure_event_count"),
        }

        release_rc, release, release_raw = run_json_command(
            ["code/pr3_release_byte_exact_audit.py", "--json"],
            output_dir / "tier_c_release_byte_exact_audit.json",
        )
        if release is None:
            (output_dir / "tier_c_release_byte_exact_audit_error.txt").write_text(
                release_raw, encoding="utf-8"
            )
            release = {}
        release_ok = (
            release_rc == 0
            and release.get("status") == "PASS"
            and release.get("pairs_checked") == 41
            and release.get("pairs_passed") == 41
            and release.get("pairs_failed") == 0
            and release.get("canonical_release_byte_matches") == 41
            and release.get("numeric_tolerance_relaxed") is False
        )
        add_result(
            results,
            "tier_c:canonical_release_bytes",
            "tier_c",
            release_ok,
            f"{release.get('canonical_release_byte_matches', 0)}/{release.get('pairs_checked', 0)}",
            "41/41",
            "Canonical release JSON byte identity after locked policy normalization",
        )

        raw_stdout_ok = release.get("raw_generator_stdout_byte_exact_claimed") is False
        add_result(
            results,
            "claim:raw_generator_stdout",
            "claim_boundary",
            raw_stdout_ok,
            release.get("raw_generator_stdout_byte_exact_claimed"),
            False,
            "Raw generator stdout byte identity remains explicitly unclaimed",
        )
        raw_file_order_ok = release.get("raw_checked_in_file_order_byte_exact_claimed") is False
        add_result(
            results,
            "claim:raw_checked_file_order",
            "claim_boundary",
            raw_file_order_ok,
            release.get("raw_checked_in_file_order_byte_exact_claimed"),
            False,
            "Raw checked-in JSON file-order byte identity remains explicitly unclaimed",
        )
        tier_data["tier_c"] = {
            "status": "PASS" if release_ok else "FAIL",
            "pairs_checked": release.get("pairs_checked", 0),
            "pairs_passed": release.get("pairs_passed", 0),
            "pairs_failed": release.get("pairs_failed", 0),
            "canonical_release_byte_matches": release.get("canonical_release_byte_matches", 0),
            "numeric_display_locked": release.get("event_counts", {}).get("numeric_display_locked", 0),
            "numeric_tolerance_relaxed": release.get("numeric_tolerance_relaxed"),
            "raw_generator_stdout_byte_exact_claimed": release.get(
                "raw_generator_stdout_byte_exact_claimed"
            ),
            "raw_checked_in_file_order_byte_exact_claimed": release.get(
                "raw_checked_in_file_order_byte_exact_claimed"
            ),
        }

    summary = write_results(output_dir, scope, inventory, results, tier_data)
    print(f"PR-III numerical validation: {summary['status']}")
    print(f"checks={summary['checks_total']} passed={summary['checks_passed']} failed={summary['checks_failed']}")
    print(f"PR4-labelled source paths: {len(scope.get('forbidden_paths', []))}")
    print(f"PR4 source references: {len(scope.get('forbidden_references', []))}")
    if tier_data:
        print(f"Tier A manifest/targeted audit: {tier_data['tier_a']['status']}")
        print(
            "Tier B schema/numeric pairs: "
            f"{tier_data['tier_b']['pairs_passed']}/{tier_data['tier_b']['pairs_checked']} "
            f"{tier_data['tier_b']['status']}"
        )
        print(
            "Tier C canonical release bytes: "
            f"{tier_data['tier_c']['canonical_release_byte_matches']}/"
            f"{tier_data['tier_c']['pairs_checked']} {tier_data['tier_c']['status']}"
        )
        print(
            "Numeric tolerance relaxed: "
            f"{'yes' if tier_data['tier_c']['numeric_tolerance_relaxed'] else 'no'}"
        )
        print("Raw generator stdout byte identity: not claimed")
        print("Raw checked-in file-order byte identity: not claimed")
    print(f"summary={output_reference(output_dir)}/PR3_NUMERICAL_VALIDATION_SUMMARY.md")
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
