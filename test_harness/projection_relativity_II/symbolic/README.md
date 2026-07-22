# Projection Relativity II Symbolic Test Harness

This directory contains the reproducible Maple tester and release evidence for the current Projection Relativity II manuscript.

## Release Result

The 2026-07-21 release audit passed all `617` Maple checks and all `8` negative-control self-tests. It inventoried all `442` top-level display blocks, with `0` unmapped blocks and `0` unresolved `MANUSCRIPT` rows. The independent Python reference runner also passed `155/155` numerical checks.

The exact audited manuscript has SHA256:

```text
C14579DEC15B29C315B48FEF80DC47031FA345BAAE9DE8F358F63F55E74DE214
```

See `RUN_SUMMARY.md` for the complete release ledger.

## User Map

```text
symbolic/
|-- README.md
|-- RUN_SUMMARY.md
|-- code/
|   `-- pr2_symbolic_tester_code_package.zip
`-- results/
    |-- coverage_quality_report.md
    |-- equation_audit.md
    |-- equation_derivations.md
    |-- equation_map.md
    |-- github_source_manifest.json
    |-- harness_validation.md
    |-- pr2_maple_results.csv
    |-- pr2_maple_summary.md
    |-- pr2_maple_traceability.csv
    |-- pr2_reference_results.csv
    |-- pr2_reference_scope.md
    |-- pr2_reference_summary.md
    |-- pr2_reference_traceability.csv
    |-- proof_report.md
    |-- qcd_threshold_recompute.md
    |-- source_equation_coverage.md
    |-- source_equation_inventory.csv
    `-- pr2_symbolic_tester.zip
```

### `code/`

`pr2_symbolic_tester_code_package.zip` contains only the runnable release code and user documentation:

- Maple harness entrypoints and test modules
- manuscript source fetcher
- source-equation inventory and Maple assertion generators
- independent Python reference runner
- portable Windows PowerShell runners

### `results/`

The unpacked files provide direct access to the principal evidence. `pr2_symbolic_tester.zip` contains the complete result set, including the exact audited TeX source and its SHA256 manifest.

The main reviewer-facing files are:

- `proof_report.md`: complete passing Maple assertion ledger
- `equation_map.md`: equation-to-test traceability map
- `source_equation_coverage.md`: classification of every display block
- `source_equation_inventory.csv`: machine-readable display inventory
- `pr2_maple_results.csv`: all Maple outcomes
- `pr2_maple_traceability.csv`: test-to-section traceability
- `harness_validation.md`: negative-control results
- `github_source_manifest.json`: exact source provenance

Temporary files, internal construction notes, obsolete issue lists, and empty failure-report placeholders are not included in the release package.

## Reproduce the Audit

Requirements:

- Windows PowerShell
- Maple with `cmaple` or `maple`
- Python 3

Extract `code/pr2_symbolic_tester_code_package.zip`, open PowerShell in the extracted directory, and run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_full_audit_windows.ps1
```

The runner fetches the current public PR-II manuscript, regenerates the full equation inventory and Maple source assertions, runs Maple, and regenerates the coverage report. It searches PATH and common Maple installation directories. For a nonstandard Maple installation, set `MAPLE_BIN` to its binary directory before running.

For an offline rerun after the source fixture has been fetched:

```powershell
$env:PR2_SKIP_GITHUB_FETCH="1"
.\run_full_audit_windows.ps1
```

## Coverage Labels

- `PASS`: directly recomputed or covered by an identified passing section chain
- `NOTE`: contextual, repeated, definitional, or explicitly deferred material
- `DATA`: external diagnostic/reference material not used as a generation input
- `MANUSCRIPT`: reserved for unresolved source-cleanup items; the released audit has none

`NOTE` and `DATA` classifications are coverage boundaries, not test failures.

## Package Integrity

```text
code/pr2_symbolic_tester_code_package.zip
SHA256: FC2BE7729C7F8525358036485D3A3BBA40686C4A80919EEB1228598320616AAA

results/pr2_symbolic_tester.zip
SHA256: 5816C6517A009970CBEB4072B46E2670D05FA818F4F44EE537E074D2E5AD7993
```

## Scope

The harness verifies the PR-II machine-checkable symbolic and numerical closure chain, full source-equation accounting, negative controls, and audit traceability. External precision inputs and explicit PR-III deferred layers remain identified as `DATA` or `NOTE`; they are not silently counted as derived PR-II theorems.
