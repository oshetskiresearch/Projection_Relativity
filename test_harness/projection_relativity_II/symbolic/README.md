# Projection Relativity II Symbolic Test Harness

This directory contains the Maple symbolic tester and validation evidence for the Projection Relativity II manuscript.

The harness is designed to fetch the current PR-II manuscript from GitHub, regenerate source-equation coverage, run the Maple symbolic checks, and produce reviewer-facing audit reports.

## Directory Contents

```text
symbolic/
|-- README.md
|-- RUN_SUMMARY.md
|-- code/
|   `-- pr2_symbolic_tester_code_package.zip
`-- results/
    |-- equation_audit.md
    |-- equation_derivations.md
    |-- harness_validation.md
    |-- pr2_symbolic_tester.zip
    |-- proof_report.md
    `-- qcd_threshold_recompute.md
```

## What Is Included

### `code/`

`code/pr2_symbolic_tester_code_package.zip` contains the runnable tester code:

- Maple harness entrypoints
- Maple symbolic test modules
- Python source-coverage generators
- Windows PowerShell runners
- GitHub source-fetch script
- GitHub-friendly `.gitignore` and upload manifest

The code package is intended for users who want to rerun the audit locally.

### `results/`

`results/` contains the public-facing evidence from the latest symbolic tester run.

Important files:

- `proof_report.md` - detailed proof/check ledger for the passing Maple assertions
- `equation_audit.md` - audit summary and coverage interpretation
- `harness_validation.md` - negative-control/self-validation summary
- `equation_derivations.md` - derivation routes for central equations
- `qcd_threshold_recompute.md` - focused QCD threshold/running recomputation ledger
- `pr2_symbolic_tester.zip` - complete result artifact package, including full CSV reports, coverage inventory, source manifest, and run summary

`RUN_SUMMARY.md` at this directory root gives the compact headline result.

## Latest Verified Result

The latest uploaded run was performed on 2026-06-23 using Maple 2026.

The tester fetched the current manuscript source from:

```text
https://raw.githubusercontent.com/oshetskiresearch/Projection_Relativity/main/manuscript/projection_relativity_II/Oshetski_Projection_Relativity_II_Main.tex
```

Fetched source:

```text
SHA256: F4417EDD54539B15FFE1FE176CCCB1DE0D5E8E7771F5801C11DAEB0D8BCB1BCD
Bytes: 227630
```

Symbolic tester result:

```text
Maple tests: 621
Passed: 621
Failed: 0
Self-validation negative controls: 8
Display blocks inventoried: 446
Unmapped display blocks: 0
```

## How To Rerun The Tester

1. Download and extract:

```text
code/pr2_symbolic_tester_code_package.zip
```

2. From the extracted folder, run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_full_audit_windows.ps1
```

The full runner performs this workflow:

1. Fetch the latest GitHub manuscript source.
2. Regenerate the LaTeX display-equation inventory.
3. Regenerate Maple source-coverage assertions.
4. Run the Maple symbolic tester.
5. Regenerate the coverage quality report.

## Requirements

- Windows PowerShell
- Maple with `cmaple`
- Python 3

The runner checks common Python locations and PATH. If Maple is installed in a nonstandard location, update `run_maple_windows.ps1` before rerunning.

## Generated Outputs

A rerun generates files such as:

```text
reports/pr2_maple_summary.md
reports/pr2_maple_results.csv
reports/pr2_maple_traceability.csv
reports/pr2_maple_failures.md
source/github_source_manifest.json
source_equation_coverage.md
source_equation_inventory.csv
coverage_quality_report.md
direct_proof_backlog.csv
proof_report.md
```

These generated files are intentionally separate from the code package and are represented publicly by the `results/` folder.

## Interpreting Coverage Labels

The coverage inventory uses several labels:

- `PASS` means the displayed expression is directly checked or covered by a passing section chain.
- `NOTE` marks contextual, repeated, structural, or PR-III-deferred displays that are accounted for but not treated as failed checks.
- `DATA` marks external reference or diagnostic values that are not used as generation inputs.
- `MANUSCRIPT` marks typographic or manuscript-cleanup issues that do not change the tested mathematical result.

`NOTE`, `DATA`, and `MANUSCRIPT` rows are accounting labels, not test failures.

## Package Hashes

Current uploaded package hashes:

```text
code/pr2_symbolic_tester_code_package.zip
SHA256: 0B2A32F1E86A716FB396DF98B0013C65A29C757527B08CBA775A06FFFE8AB29F

results/pr2_symbolic_tester.zip
SHA256: 1C401C3E28B17CAA03AAF742CE660216CF57C37E80B29179EAD3C5E276952898
```

## Scope

This symbolic harness verifies the PR-II machine-checkable symbolic and numerical closure chain, source-equation accounting, negative controls, and audit traceability.

It does not claim to complete deferred PR-III precision-layer obligations such as full radiative electroweak corrections, scalar mass closure, or full strong-sector precision matching.

