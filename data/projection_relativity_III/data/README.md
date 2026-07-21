# Projection Relativity III JSON Ledgers

This directory contains 44 checked PR-III JSON inputs, generated ledgers,
audits, refinements, and final decisions. They are scientific calculation
records, not raw experimental datasets.

The files cover the inherited PR-I/PR-II boundary state and the PR-III scalar,
electromagnetic, electroweak, neutrino, strong-sector, anomaly, continuity,
provenance, and cross-sector closure stages.

## Relationship to the Generators

The generator sources are in [`../code/`](../code/). The authoritative 41
generator/output pairs are listed in
[`pr3_full_regeneration_pairs.json`](../../../test_harness/projection_relativity_III/numerical/schemas/pr3_full_regeneration_pairs.json).
Three additional JSON files provide convergence, refinement, or locked-source
inputs used by the public calculation ledger.

Do not infer the role of a JSON file from its filename alone. Use the pair
manifest and the parent [`PR-III data README`](../README.md) to distinguish
generation inputs, generated outputs, and post-generation diagnostics.

## Reproducibility

Run the complete validation from the repository root:

```bash
python test_harness/projection_relativity_III/numerical/run_pr3_numerical_validation.py
```

The checked
[`PR3_NUMERICAL_SOURCE_INVENTORY.csv`](../../../test_harness/projection_relativity_III/numerical/results/PR3_NUMERICAL_SOURCE_INVENTORY.csv)
records the public package paths, byte counts, and SHA-256 hashes. The numerical
harness separately verifies schema/numerical agreement and canonical release
bytes for every declared pair.

## Interpretation Boundary

Diagnostic reference values are post-generation comparisons unless a ledger
explicitly identifies a value as inherited PR boundary data. These JSON files
must not be represented as raw observations or independently fitted inputs.
