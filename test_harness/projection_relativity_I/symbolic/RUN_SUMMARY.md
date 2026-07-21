# PR-I Symbolic Tester Rerun Summary

Run date: 2026-07-21
Execution engine: Maple 2026  
Source: repository-local PR-I manuscript and supplement

## Fresh-Clone Command

The harness was run from the repository root with:

```bash
cmaple -q test_harness/projection_relativity_I/symbolic/code/run_appendix_verification.mpl
```

The runner loaded:

```text
test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl
```

The source-text audit read the public files directly from their tracked
paper-specific paths:

```text
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Supplement.tex
```

No manuscript file was downloaded, copied, renamed, or staged into a legacy
path for this run.

## Result

Status: **PASS**

```text
PASS count: 227
Boundary count: 18
  ASSUMPTION count: 8
  DATA count: 8
  MANUSCRIPT count: 0
  NOTE count: 2
SELFTEST PASS count: 18
SPECTRUM RECOMPUTE count: 3
PROOF REPORT entries: 216
```

## Release-Gate Notes

- `MANUSCRIPT count: 0`, so the harness found no paper/checker mismatch.
- Source-text coverage found every locked constant in the repository-local main
  paper and supplement.
- All 18 self-validation negative controls passed.
- The independent radial spectrum recomputation produced three passing checks.
- The command exited with status zero.

## Regenerated Artifacts

The run refreshed these tracked files under
`test_harness/projection_relativity_I/symbolic/results/`:

- `equation_audit.md`
- `equation_derivations.md`
- `equation_map.md`
- `harness_validation.md`
- `proof_report.md`
- `spectrum_recompute.md`

## Scope

This harness verifies the Projection Relativity I symbolic, dimensional,
numerical, source-text, and negative-control checks that are machine-checkable
from the paper and supplement.

Boundary labels such as `ASSUMPTION`, `DATA`, and `NOTE` are not failures. They
mark claims that require physical assumptions, external datasets/backends, or
structural interpretation beyond direct Maple proof.
