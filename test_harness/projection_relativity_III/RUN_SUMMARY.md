# PR-III Symbolic Harness Run Summary

Run date: 2026-07-20

## Inputs

- Public repository: `oshetskiresearch/Projection_Relativity`
- Public repository commit checked before harness update: `97db32395138b7fac38b646f045edf0d702bd00c`
- Locked sandbox ledger commit: `47a175c56676242fdfe1dfebdc15d680aa531109`
- Public manuscript source: `manuscript/projection_relativity_III/Oshetski_Projection_Relativity_III_Main.tex`
- Public manuscript PDF: `manuscript/projection_relativity_III/Oshetski_Projection_Relativity_III_Main.pdf`
- Maple engine: Maple 2026 command-line `cmaple`

## Result

```text
OVERALL_STATUS: PASS
Python symbolic/public paper conformance: PASS, 82/82
Equation audit: PASS, 253/253 display blocks mapped
Direct Maple or locked-value coverage: 148 display blocks
Numeric value audit: PASS, 283/283 manuscript numeric values matched
Maple symbolic checks: PASS, 67/67
Maple negative controls: PASS, 12/12
```

The public PDF text was checked for the revised canonical-closure,
closed-admissibility, positive-defect, and singleton-quotient statements, as
well as the locked headline values and diagnostic positions.

The separate numerical validation harness under `numerical/` was not rerun.
This refresh is limited to the symbolic, equation-accounting, manuscript-value,
and paper-conformance layers because the locked numerical predictions were
unchanged.

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

The public paper-conformance run used `--skip-repo-audits` so that the separate
numerical/regeneration pipeline was not executed. Its 82 checks cover required
artifacts, locked-value agreement, diagnostics, global and anomaly gates,
the revised exact `C3` identities, PDF text, and negative controls.
