# Projection Relativity III Symbolic Audit Code

This directory contains the Maple and Python implementation used by the PR-III
symbolic, equation-coverage, manuscript-value, and paper-conformance audits.

## Files

| File | Role |
|---|---|
| `pr3_harness.mpl` | Maple assertion, reporting, and audit infrastructure. |
| `pr3_tests.mpl` | PR-III symbolic checks and negative controls. |
| `pr3_equation_audit.py` | Inventories and classifies displayed manuscript equations. |
| `pr3_numeric_value_audit.py` | Compares manuscript numerical values with the locked public ledger. |
| `run_pr3_paper_conformance.py` | Runs the PR-III claim and repository conformance checks. |

## Maple Audit

The parent runner loads both Maple files. From
`test_harness/projection_relativity_III/`, run:

```bash
cmaple run_pr3_maple_test.mpl
```

## Python Audits

The Python tools require Python 3.10 or newer. Their repository and output
arguments are documented by each command:

```bash
python test_harness/projection_relativity_III/symbolic/code/pr3_equation_audit.py --help
python test_harness/projection_relativity_III/symbolic/code/pr3_numeric_value_audit.py --help
python test_harness/projection_relativity_III/symbolic/code/run_pr3_paper_conformance.py --help
```

The checked commands, external-ledger boundary, and result totals are described
in the parent [`symbolic README`](../README.md). Generated reports belong in
[`../results/`](../results/), not in this code directory.
