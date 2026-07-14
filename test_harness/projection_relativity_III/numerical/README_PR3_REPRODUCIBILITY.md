# Projection Relativity III - Reproducibility Package

## Purpose

This file defines the public reproducibility entry point for the PR-III ledger through Step 09.

Construction generators and JSON ledgers live under
`data/projection_relativity_III` at the repository root. Audit code, schemas,
and results live in this test-harness directory.

The sandbox status is:

```text
PRIII_GLOBAL_STATUS: CONSISTENCY_LOCKED
PRECISION_STATUS: ALPHA_MW_MZ_GF_ONE_SIGMA_DIAGNOSTIC_PASS
COMPATIBILITY_STATUS: NEUTRINO_AND_STRONG_BRANCHES_COMPATIBLE
STRUCTURAL_STATUS: ANOMALY_CONTINUITY_NO_FIT_PASS
FINAL_EXACT_ALL_ORDERS_THEOREM: NOT_CLAIMED
PRIII_SANDBOX_LEDGER: COMPLETE_THROUGH_STEP_09
```

## Reproducibility principle

Every reported value must be traceable to one of three categories:

1. frozen PR-I / PR-II / PR-III ledger input,
2. PR-generated output,
3. post-generation diagnostic reference.

Diagnostic references may evaluate PR outputs, but may not generate them.

## Reproducibility tiers

PR-III now separates reproducibility into four explicit tiers.

```text
Tier A: manifest/default repo audit
Tier B: full 41-pair schema/numeric artifact reproducibility
Tier C: canonical release byte-exact regeneration
Tier D: raw checked-in file-order or raw generator stdout byte identity
```

Current claim:

```text
Tier A: PASS
Tier B: PASS, 41/41 generator/data pairs
Tier C: PASS, 41/41 canonical release byte matches
Tier D: NOT CLAIMED
```

Tier D is intentionally not the release claim. Raw JSON key order, raw generator stdout formatting, and Python Decimal display tails are not treated as physics outputs. The release package is the canonical JSON byte stream defined by:

```text
schemas/pr3_release_byte_exact_policy.json
code/pr3_release_byte_exact_audit.py
```

## Required run order

Use:

```text
RUN_ORDER.md
```

## Tier A: default hardened audit

The default audit runner is:

```bash
python code/run_all_pr3_audits.py
```

By default, the audit runner performs:

```text
1. manifest/status checks
2. targeted regeneration schema/gate checks
```

To run only the older manifest/status layer:

```bash
python code/run_all_pr3_audits.py --manifest-only
```

The targeted regeneration schema list is:

```text
schemas/pr3_regeneration_targets.json
```

The locked-output manifest is:

```text
MANIFEST_PR3_LOCKED_OUTPUTS.json
```

## Tier B: full schema/numeric artifact reproducibility

Run:

```bash
python code/pr3_artifact_drift_audit.py
python code/pr3_artifact_drift_audit.py --json > results/tier_b_artifact_drift_audit.json
```

Current Tier B result:

```text
artifact_drift_audit.status: PASS
pairs_checked: 41
pairs_passed: 41
pairs_failed: 0
failure_classes:
  pass: 41
```

Supporting summaries:

```bash
python code/pr3_schema_drift_summary.py results/tier_b_artifact_drift_audit.json
python code/pr3_numeric_drift_summary.py results/tier_b_artifact_drift_audit.json
```

Both summaries are clean: no wrapper drift, no nested schema drift, no representation drift, and no numeric drift beyond policy.

## Tier C: canonical release byte-exact regeneration

Run:

```bash
python code/pr3_release_byte_exact_audit.py
python code/pr3_release_byte_exact_audit.py --json > results/tier_c_release_byte_exact_audit.json
```

Current Tier C result:

```text
PR-III canonical release byte-exact audit: PASS
pairs_checked: 41
pairs_passed: 41
pairs_failed: 0
canonical release byte matches: 41/41
numeric_display_locked: 151
raw checked-in file-order byte matches: 0/41
```

To regenerate the canonical release tree:

```bash
python code/pr3_release_byte_exact_audit.py --write-release-tree results/pr3_canonical_release
```

The release tree contains the regenerated canonical JSON artifacts. Files are generated under:

```text
results/pr3_canonical_release
```

## Tier D: raw byte identity not claimed

The following are not claimed:

```text
raw checked-in JSON file-order byte identity
raw generator stdout byte identity
that Python Decimal/string display tails are physical observables
```

The older full-target drift-report command remains useful as a raw-generator/canonical-diff diagnostic:

```bash
python code/run_all_pr3_audits.py --full-targets --drift-report
```

It is not the Tier C release-byte authority unless it is explicitly wired to the Pass 016 release policy.

The older strict byte-exact command remains a raw canonical-diff stress test:

```bash
python code/run_all_pr3_audits.py --full-targets --byte-exact
```

It is not the PR-III release-byte claim.

## Final audit summary

Use:

```text
results/PR3_FINAL_AUDIT_SUMMARY.md
```

## Core tables

```text
results/pr3_locked_outputs.csv
results/pr3_cross_sector_diagnostic_table.csv
```

## Hardening record

The hardening sequence through Pass 016 resolved:

```text
builder exposure failures
mechanical dataset/input_policy/module wrapper drift
nested structural schema drift
numeric drift beyond policy
Step 06C stale locked-artifact provenance drift
canonical release-byte regeneration
```

Final reproducibility status:

```text
manifest/default audit: PASS
41-pair schema/numeric artifact reproducibility: PASS
canonical release byte-exact regeneration: PASS
raw checked-in file-order identity: NOT CLAIMED
```

## Manuscript status

The next task is to convert the locked sandbox ledger into the PR-III manuscript. The manuscript must preserve the no-fit discipline, must not overclaim exact all-orders closure, and should state the reproducibility tier explicitly.
