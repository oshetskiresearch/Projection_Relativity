# PR-I Symbolic Tester Rerun Summary

Run date: 2026-06-24  
Execution engine: Maple 2026  
Source: latest GitHub raw manuscript fetch

## Source

The PR-I Maple harness expects repository-local manuscript files at:

```text
manuscript/Oshetski_Projection_Relativity_Main.tex
manuscript/Oshetski_Projection_Relativity_Supplement.tex
```

For this run, the latest GitHub PR-I manuscript files were fetched from the current public layout and staged into the expected harness paths:

```text
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Supplement.tex
```

Fetched at UTC: `2026-06-24T16:16:17.5826484Z`

Main manuscript:

```text
URL: https://raw.githubusercontent.com/oshetskiresearch/Projection_Relativity/main/manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex
SHA256: B9AB9D6E5CDB46AA7AA3572BC4D9C96E490ED5E724A7695B44D8590F12D41E8B
```

Supplement:

```text
URL: https://raw.githubusercontent.com/oshetskiresearch/Projection_Relativity/main/manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Supplement.tex
SHA256: 36FB0B59C0970E693AA5C78E8445CB1375E9C32B6F84DC8B43499C055131F916
```

Harness:

```text
URL: https://raw.githubusercontent.com/oshetskiresearch/Projection_Relativity/main/test_harness/projection_relativity_I/symbolic/ProjectionRelativityAppendixVerify.mpl
SHA256: 1505BE9590D7E57373520A60DB7A56B92B61728DC951E2C9AEE17629070AC71F
```

## Result

Status: PASS

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

- `MANUSCRIPT count: 0`, so the harness found no current paper/checker mismatch.
- Source-text coverage found the locked constants in the fetched main paper and supplement.
- All 18 self-validation negative controls passed.
- The independent radial spectrum recomputation produced 3 passing checks.

## Included Artifacts

- `equation_audit.md`
- `equation_derivations.md`
- `equation_map.md`
- `harness_validation.md`
- `proof_report.md`
- `spectrum_recompute.md`
- `source_manifest/source_manifest.json`

## Scope

This harness verifies the Projection Relativity I symbolic, dimensional, numerical, source-text, and negative-control checks that are machine-checkable from the paper and supplement.

Boundary labels such as `ASSUMPTION`, `DATA`, and `NOTE` are not failures. They mark claims that require physical assumptions, external datasets/backends, or structural interpretation beyond direct Maple proof.
