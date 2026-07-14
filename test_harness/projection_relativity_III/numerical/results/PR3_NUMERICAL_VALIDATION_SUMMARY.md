# PR-III Numerical Validation Summary

Status: **PASS**

- Checks: `17/17` passed
- PR-III generators: `41`
- PR-III JSON ledgers: `44`
- PR4-labelled source paths: `0`
- PR4 source references: `0`

## Reproducibility Tiers

- Tier A manifest/targeted audit: `PASS`
- Tier B schema/numeric pairs: `41/41 PASS`
- Tier C canonical release bytes: `41/41 PASS`
- Numeric tolerance relaxed: `no`
- Raw generator stdout byte identity: `NOT_CLAIMED`
- Raw checked-in file-order byte identity: `NOT_CLAIMED`

## Interpretation

Tier B permits documented decimal display-tail and mechanical root-wrapper accounting only when
the locked numerical tolerance and nonnumeric structure remain satisfied. Tier C then requires
the resulting canonical release JSON bytes to match for all declared pairs.
