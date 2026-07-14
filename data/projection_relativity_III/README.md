Projection Relativity III Public Numerical Data

This directory contains the public Python generators and JSON numerical ledgers
supporting **Projection Relativity III**. The files cover the complete PR-III
calculation sequence from Step 01 through the Step 09F consistency statement.

## Contents

```text
projection_relativity_III/
  code/                         41 PR-III Python generators
  data/                         44 PR-III JSON ledgers and inputs
  PR3_PUBLIC_DATA_MANIFEST.json generator/data pairs and SHA-256 hashes
  README.md
```

The 41 declared generator/data pairs are recorded in
[`PR3_PUBLIC_DATA_MANIFEST.json`](PR3_PUBLIC_DATA_MANIFEST.json). Three
additional JSON files provide convergence, refinement, or locked-reference
inputs used by the calculation ledger.

All files labelled for PR4 are outside this package and are not included.

## Requirements

- Python 3.10 or newer
- No third-party Python packages

## Running A Generator

Run generators from the repository root so their sibling `data/` paths remain
unchanged. For example:

```powershell
python data/projection_relativity_III/code/pr3_v08f_final_priii_consistency_statement.py
```

Each generator emits its JSON result to standard output. The corresponding
checked-in result is identified in the public data manifest.

## Full Reproducibility Test

The complete numerical audit is maintained in the
[`test_harness/projection_relativity_III/numerical`](../../test_harness/projection_relativity_III/numerical/)
directory. From the repository root, run:

```powershell
python test_harness/projection_relativity_III/numerical/run_pr3_numerical_validation.py
```

A passing run verifies:

- all 41 generator/data pairs at the schema and numerical tiers;
- all 41 canonical release JSON artifacts at the byte-exact tier;
- the locked numerical tolerance policy without tolerance relaxation; and
- exclusion of PR4-labelled source paths and dependencies.

## Provenance

The package was selected from
[`oshetskiresearch/Projection-Relativity_III_Sandbox`](https://github.com/oshetskiresearch/Projection-Relativity_III_Sandbox)
at PR-III payload snapshot
`fbb61f3771db2674c2b551a2d767c923cd5f0a1f`. The included paths were verified
unchanged through sandbox commit
`14979ec5d6ecdc4f0fb8f8ed5e6345bec1cbf0fa`.

## Claim Boundary

This package supports manifest, schema/numerical, and canonical release-byte
reproducibility for the 41 declared PR-III generator/data pairs when the public
numerical test harness passes. Raw generator stdout byte identity and raw
checked-in JSON key-order byte identity are not claimed.
