# Projection Relativity III Generators

This directory contains the 41 standard-library Python generators that produce
the declared PR-III JSON calculation ledgers in [`../data/`](../data/).

The authoritative generator/output pairing is
[`pr3_full_regeneration_pairs.json`](../../../test_harness/projection_relativity_III/numerical/schemas/pr3_full_regeneration_pairs.json).
The checked source hashes are recorded in
[`PR3_NUMERICAL_SOURCE_INVENTORY.csv`](../../../test_harness/projection_relativity_III/numerical/results/PR3_NUMERICAL_SOURCE_INVENTORY.csv).

## Requirements

- Python 3.10 or newer
- No third-party Python packages

## Run a Generator

Run generators from the repository root so their sibling data paths resolve
consistently. For example:

```bash
python data/projection_relativity_III/code/pr3_v08f_final_priii_consistency_statement.py
```

Each generator writes its JSON result to standard output. Use the pair manifest
to identify the corresponding checked-in JSON ledger.

## Validate the Complete Package

From the repository root:

```bash
python test_harness/projection_relativity_III/numerical/run_pr3_numerical_validation.py
```

That runner checks the manifest, schema/numerical agreement, source inventory,
and canonical release bytes. See the
[`PR-III numerical README`](../../../test_harness/projection_relativity_III/numerical/README.md)
for the complete contract.
