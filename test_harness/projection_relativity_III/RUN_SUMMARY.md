# PR-III Public Harness Run Summary

Run date: 2026-07-21

Repository: `oshetskiresearch/Projection_Relativity`

Release branch: `main`

## Inputs

- Manuscript: `manuscript/projection_relativity_III/Oshetski_Projection_Relativity_III_Main.tex`
- Public generator and data ledger: `data/projection_relativity_III/`
- Numerical contract: `test_harness/projection_relativity_III/numerical/`
- Symbolic contract: `test_harness/projection_relativity_III/symbolic/`
- Maple engine: Maple 2026 command-line `cmaple`

No private sandbox checkout or personal-computer path is required.

## Result

```text
OVERALL_STATUS: PASS
Maple symbolic checks: 67/67 PASS
Maple negative controls: 12/12 PASS
Equation audit: 253/253 display blocks mapped
Direct Maple or locked-value coverage: 148 display blocks
Numeric value audit: 282/282 manuscript values matched
Layout-only values: 116 classified separately
Symbolic/public paper conformance: 69/69 PASS
Numerical Tier A manifest/targeted audit: PASS
Numerical Tier B schema/numeric pairs: 41/41 PASS
Numerical Tier C canonical release bytes: 41/41 PASS
```

## Interpretation

The equation-audit pass criterion is complete display-block accounting. Every display is mapped to a direct Maple/locked-value check or an explicit repository-generation, data, or contextual class; this does not recast definitions and contextual displays as independent Maple theorems.

The numerical release contract claims schema/numeric reproducibility and canonical release-byte equality for all 41 declared pairs. Raw generator-stdout byte identity and raw checked-in file-order byte identity remain explicitly unclaimed.

Detailed human-readable and machine-readable outputs are in `symbolic/results/` and `numerical/results/`.
