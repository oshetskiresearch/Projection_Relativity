# PR-III Symbolic Harness Run Summary

Run date: 2026-07-14

## Inputs

- Public repository: `oshetskiresearch/Projection_Relativity`
- Public repository commit checked before harness import: `001dae8f46803bce16a40834cbb240c63d497faf`
- Public manuscript source: `manuscript/projection_relativity_III/Oshetski_Projection_Relativity_III_Main.tex`
- Public manuscript PDF: `manuscript/projection_relativity_III/Oshetski_Projection_Relativity_III_Main.pdf`
- Maple engine: Maple 2026 command-line `cmaple`

## Result

```text
OVERALL_STATUS: PASS
Python paper conformance: PASS, 68/68
Equation audit: PASS, 225/225 display blocks mapped
Numeric value audit: PASS, 295/295 manuscript numeric values matched
Maple symbolic checks: PASS, 38/38
Maple negative controls: PASS, 7/7
```

The public PDF text was also spot-checked for the corrected
`\epsilon_2^{\rm PR}` continuation:

```text
291973168297815611743348884979166980206478
```

## Notes

The wrapper expects the PR-III sandbox checkout as `-Repo` because the sandbox
contains the locked PR-III JSON/CSV/report ledger and regeneration scripts.
When this harness lives in the public repository at
`test_harness/projection_relativity_III`, it automatically audits the public
manuscript at `../../manuscript/projection_relativity_III`.

The pass criterion for the equation audit is full display-block accounting:
all display equations are mapped to direct Maple/locked-value checks,
repository-generation coverage, diagnostic/data comparison, or explicit
source/context coverage. It is not a claim that every display block is an
independent Maple theorem.
