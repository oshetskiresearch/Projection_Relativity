# Projection Relativity III Numerical Reproducibility Tester

This directory contains the public Python numerical tester for Projection
Relativity III. It audits the PR-III generator/JSON ledger through the final
Step 09F consistency statement.

This package is separate from the [`../symbolic/`](../symbolic/) tester. The
symbolic package checks Maple identities and values printed in the paper; this
package checks the Python-generated numerical artifacts and their locked JSON
representations.

## Scope

The public repository separates construction artifacts from validation code:

- [`../../../data/projection_relativity_III/code/`](../../../data/projection_relativity_III/code/)
  contains 41 PR-III Python generators covering Steps 01 through 09F.
- [`../../../data/projection_relativity_III/data/`](../../../data/projection_relativity_III/data/)
  contains 44 PR-III JSON data and input-ledger files.
- [`schemas/`](schemas/) contains six PR-III schema and policy files.
- [`code/`](code/) contains six PR-III audit utilities.
- [`results/`](results/) contains the published reports and supporting tables.

The runner resolves both parts from a complete checkout of this repository; the
numerical test-harness directory is not intended to be detached from the data
package.

Files labelled for PR4 are outside the scope of this package. No `pr4_*.py`,
`pr4_*.json`, PR4 report, or file from the sandbox `PR4/` tree is executed. The
runner verifies this exclusion before it imports or executes any generator.

## Reproducibility Tiers

The default run verifies the three PR-III tiers that are currently claimed:

1. **Tier A: manifest and targeted regeneration**
   - Checks required files, locked status fields, and curated schema/gate
     regeneration targets.

2. **Tier B: full schema and numerical reproducibility**
   - Regenerates all 41 generator/data pairs.
   - Requires schema, status, gate, and numerical agreement under the locked
     PR-III tolerance policy.
   - Does not relax the `1e-40` default absolute or relative tolerance.

3. **Tier C: canonical release-byte reproducibility**
   - Requires all 41 regenerated canonical JSON artifacts to match the locked
     canonical release bytes.
   - Applies the documented display-lock and root-wrapper policy only after
     schema and numerical agreement have passed.

Tier D is intentionally not claimed. Raw generator stdout bytes and raw
checked-in JSON key-order bytes are not treated as release identities.

## Requirements

- A complete checkout of the public repository.
- Python 3.10 or newer.
- No third-party Python packages.

The generators and audits use only the Python standard library.

## Run

From `test_harness/projection_relativity_III/numerical`:

```powershell
python run_pr3_numerical_validation.py
```

To write reports to another directory:

```powershell
python run_pr3_numerical_validation.py --output-dir C:\path\to\results
```

## Expected Result

A clean run reports:

```text
PR-III numerical validation: PASS
PR4-labelled source paths: 0
PR4 source references: 0
Tier A manifest/targeted audit: PASS
Tier B schema/numeric pairs: 41/41 PASS
Tier C canonical release bytes: 41/41 PASS
Numeric tolerance relaxed: no
Raw generator stdout byte identity: not claimed
Raw checked-in file-order byte identity: not claimed
```

Numeric formatting warnings identify equivalent decimal representations with
different displayed tails. They are accounting information, not failed
physics checks. Any schema drift, nonnumeric text drift, or numerical drift
beyond policy remains a failure.

## Results

The runner writes:

```text
results/
  PR3_NUMERICAL_VALIDATION_SUMMARY.md
  PR3_NUMERICAL_VALIDATION_SUMMARY.json
  PR3_NUMERICAL_VALIDATION_RESULTS.csv
  PR3_NUMERICAL_SOURCE_INVENTORY.csv
  tier_a_manifest_audit.txt
  tier_b_artifact_drift_audit.json
  tier_b_schema_drift_summary.json
  tier_b_numeric_drift_summary.json
  tier_c_release_byte_exact_audit.json
```

The checked source boundary is recorded in
[`PR3_NUMERICAL_SCOPE.json`](PR3_NUMERICAL_SCOPE.json). The PR-III construction
payload is traceable to sandbox commit
`fbb61f3771db2674c2b551a2d767c923cd5f0a1f` and was verified unchanged through
`14979ec5d6ecdc4f0fb8f8ed5e6345bec1cbf0fa` for the included paths.

## Claim Boundary

This tester supports the following statement:

> The PR-III Python/JSON ledger is reproducible at the manifest, schema/numeric,
> and canonical release-byte tiers for all 41 declared generator/data pairs.

It does not turn post-generation diagnostic references into generation inputs,
does not claim raw stdout identity, and does not extend the test scope to PR4.
