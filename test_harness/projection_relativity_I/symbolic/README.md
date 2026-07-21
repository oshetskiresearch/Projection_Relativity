# Projection Relativity I Maple Checker

This folder contains the Maple symbolic verification harness for the public
Projection Relativity manuscript.

The checker is linked to the LaTeX source files in:

```text
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Supplement.tex
```

The main Maple file is:

```text
test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl
```

The convenience runner is:

```text
test_harness/projection_relativity_I/symbolic/code/run_appendix_verification.mpl
```

## What The Checker Does

The Maple checker verifies the algebraic, symbolic, dimensional, and numeric
claims that are machine-checkable from the paper and supplement.

It checks:

- section-level equations from the main paper
- supplemental derivation chains
- exact boundary-cofactor arithmetic
- radial spectrum reference values and gap arithmetic
- finite-rank alpha closure arithmetic
- compact magnetic area-law algebra
- propagator subtraction and low-energy residual algebra
- finite-core radius, density, and curvature expressions
- displacement-sector stationarity and mass formulas
- electromagnetic gauge-invariance identities
- trace-free tensor consistency
- dimensional homogeneity
- sign and domain preconditions
- source-text coverage against the LaTeX files
- negative controls proving the harness rejects known-bad equations

The checker does not certify claims outside its machine-checkable scope.
Statements needing external catalogs, numerical backends, operator geometry, or
physical assumptions are recorded as boundary labels.

Use this release language:

```text
symbolically audited and numerically validated where machine-checkable
```

## Repository Layout

The expected public repository layout is:

```text
Projection_Relativity/
  manuscript/
    projection_relativity_I/
      Oshetski_Projection_Relativity_Main.tex
      Oshetski_Projection_Relativity_Supplement.tex
  test_harness/
    projection_relativity_I/
      symbolic/
        README.md
        code/
          ProjectionRelativityAppendixVerify.mpl
          run_appendix_verification.mpl
        results/
```

The Maple harness has these source constants near the top of
`ProjectionRelativityAppendixVerify.mpl`:

```maple
PR_source_repo := "oshetskiresearch/Projection_Relativity":
PR_source_branch := "main":
PR_source_path := "manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex":
PR_supplement_path := "manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Supplement.tex":
PR_results_path := "test_harness/projection_relativity_I/symbolic/results":
PR_require_source_text := true:
```

Run the checker from the repository root. This makes the source and result paths
above valid on Windows, macOS, and Linux without staging or copying files.

The checker does not download files from GitHub. It intentionally verifies the
repo-local LaTeX files in the current checkout. To check the latest public
version, update the repository first, then run Maple:

```bash
git pull
```

## Prerequisites

You need:

- Maple installed locally
- a local clone or downloaded copy of `oshetskiresearch/Projection_Relativity`
- the complete `manuscript/projection_relativity_I/` and
  `test_harness/projection_relativity_I/symbolic/` directories

No Python dependencies are required for the Maple checker.

## Quick Start In Maple Worksheet

1. Open Maple.
2. Open a new worksheet.
3. Make sure you are using a Maple input prompt, not a 2-D math text region.
4. Paste and run the following commands, changing the path to your local repo:

```maple
restart:
currentdir("C:/path/to/Projection_Relativity"):
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

On Windows, an example path may look like:

```maple
restart:
currentdir("C:/Users/your-name/Documents/GitHub/Projection_Relativity"):
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

On macOS or Linux, an example path may look like:

```maple
restart:
currentdir("/Users/your-name/Projection_Relativity"):
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

## Quick Start From Maple Command Line

From the repository root, run the convenience runner with command-line Maple:

```bash
cmaple -q test_harness/projection_relativity_I/symbolic/code/run_appendix_verification.mpl
```

From an interactive Maple prompt at the repository root, read the same runner:

```maple
restart:
read "test_harness/projection_relativity_I/symbolic/code/run_appendix_verification.mpl";
```

Or read the main harness directly:

```maple
restart:
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

The runner simply loads the main harness and calls `PR_RunAll()`.

## Important Maple Input Rule

Do not paste the full `.mpl` file into a Maple worksheet.

Only paste the short commands above. The full harness should be loaded with
`read`.

If the source is pasted into a 2-D math worksheet region, Maple can reinterpret
line continuations and may report misleading errors such as:

```text
Error, unterminated procedure
```

Use a 1-D Maple input prompt or command-line Maple.

## Expected Console Output

The run prints section headers and many PASS lines, for example:

```text
=== Section 2: Foundational Postulates ===
PASS: Postulate 3 internal metric inverse
...

=== Summary ===
PASS count: ...
Boundary count: ...
  ASSUMPTION count: ...
  DATA count: ...
  MANUSCRIPT count: 0
  NOTE count: ...
Paper and appendix Maple verification completed.
```

A healthy release run should have:

```text
MANUSCRIPT count: 0
```

Boundary counts are allowed when the statement is outside Maple's honest
machine-checkable scope.

## Generated Files

Every full run refreshes these files in
`test_harness/projection_relativity_I/symbolic/results/`:

```text
equation_map.md
equation_audit.md
harness_validation.md
equation_derivations.md
proof_report.md
spectrum_recompute.md
```

Their roles are:

- `equation_map.md`: row-by-row mapping from paper location to Maple assertion.
- `equation_audit.md`: source coverage and equation audit summary.
- `harness_validation.md`: negative controls showing the harness catches bad equations.
- `equation_derivations.md`: symbolic derivation steps for central equations.
- `proof_report.md`: detailed proof ledger for each passing assertion.
- `spectrum_recompute.md`: independent radial eigenvalue/gap recomputation.

Commit these files when you want the repository to include the latest Maple
audit results.

## Running One Section At A Time

After loading the harness:

```maple
restart:
currentdir("C:/path/to/Projection_Relativity"):
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
```

you can run individual sections:

```maple
PR_Section02_FoundationalPostulates();
PR_Section03_FoundationalMathematicalStructures();
PR_Section04_GravitationalSector();
PR_Section05_DisplacementSector();
PR_Section06_ElectromagneticSector();
PR_Section07_ProjectionPropagator();
PR_Section08_GravitationalWaves();
PR_Section09_UnifiedEnergy();
PR_Section10_DerivedScaleClosure();
PR_Section11_ObservationalTests();
```

You can also run audit and supplement chains directly:

```maple
PR_PhysicalTraceAndDimensionalAudit();
PR_TensorTraceSymmetryAudit();
PR_SignDomainPreconditionsAudit();
PR_SourceTextCoverageAudit();
PR_MasterEquationReferenceSheet();
PR_GravitationalProjectionChain();
PR_DisplacementProjectionChain();
PR_ElectromagneticProjectionChain();
PR_PropagatorStabilityChain();
PR_GravitationalWaveProjectionChain();
PR_UnifiedProjectionEnergyChain();
PR_InformationPreservationChain();
```

For release checks, prefer:

```maple
PR_RunAll();
```

because it resets counters, runs every section, and regenerates reports.

## Boundary Labels

The checker separates hard failures from honest verification boundaries:

- `PASS`: the expression, identity, or numeric check passed.
- `ASSUMPTION`: the algebra follows if the stated physical assumptions hold.
- `DATA`: the claim needs an external data file, catalog, scan output, or backend.
- `MANUSCRIPT`: Maple found a paper consistency issue that should be fixed.
- `NOTE`: structural definition, method boundary, or explanatory record.

These are not equivalent:

- `MANUSCRIPT` means the paper and checker disagree.
- `ASSUMPTION`, `DATA`, and `NOTE` mean Maple is recording the limit of what it
  can honestly prove from the printed equations alone.

## Source-Text Coverage

The source-text coverage audit searches the main paper and supplement for locked
numerical constants. This is what ties the checker to the LaTeX source.

It expects:

```text
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex
manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Supplement.tex
```

when running from the repository root.

By default, source-text coverage is required:

```maple
PR_require_source_text := true:
```

If either LaTeX file is missing, Maple stops with a clear error. This prevents a
release run from silently checking only the algebra while skipping the paper
source.

For a standalone algebra-only smoke check, you may explicitly relax this after
loading the harness:

```maple
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_require_source_text := false:
PR_RunAll();
```

Do not use relaxed mode for a release check.

For release:

1. Run from the repository root.
2. Confirm the source scan is not skipped.
3. Confirm `MANUSCRIPT count: 0`.
4. Commit the refreshed Markdown reports.

## After Editing The Paper

Whenever either LaTeX file changes:

1. Save the paper and supplement.
2. Run:

```maple
restart:
currentdir("C:/path/to/Projection_Relativity"):
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

3. Review the console summary.
4. Open `test_harness/projection_relativity_I/symbolic/results/equation_audit.md`.
5. Open `test_harness/projection_relativity_I/symbolic/results/harness_validation.md`.
6. If `MANUSCRIPT count` is nonzero, fix either the paper or the harness.
7. Commit the updated `test_harness/*.md` reports with the paper change.

## Troubleshooting

### `Error, unterminated procedure`

Cause: the `.mpl` file was pasted into a worksheet, often in 2-D math mode.

Fix: restart Maple and run only:

```maple
restart:
currentdir("C:/path/to/Projection_Relativity"):
read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

### `Warning, the restart command only works at the top level`

Cause: `restart` was executed from inside a procedure or from a file being read.

Fix: type `restart:` manually at the top-level Maple prompt, then `read` the
harness file.

### Source-text scan skipped

Cause: `PR_require_source_text` was explicitly set to `false` and Maple could
not find `manuscript/projection_relativity_I/...` from the current working
directory.

In normal release mode, this condition is an error rather than a skipped note.

Fix: run from:

```text
Projection_Relativity/
```

and make sure the paper files exist at:

```text
Projection_Relativity/manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex
Projection_Relativity/manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Supplement.tex
```

If you want the newest GitHub version, update the repository first:

```bash
git pull
```

### A numeric check fails by a tiny amount

Check whether the failing item is an exact symbolic assertion or a numerical
recompute. Numerical spectrum recomputations can have discretization tolerance.
Do not loosen a tolerance until you understand whether the paper value, Maple
expression, or numerical discretization changed.

### `MANUSCRIPT count` is nonzero

This means the checker found a paper consistency issue. Treat it as a release
blocker unless you intentionally changed the theory and still need to update the
harness.

## Release Checklist

Before tagging or publishing:

1. Run `PR_RunAll()` from the repository root.
2. Confirm the source-text scan finds both LaTeX files.
3. Confirm `MANUSCRIPT count: 0`.
4. Confirm `test_harness/projection_relativity_I/symbolic/results/harness_validation.md`
   shows negative controls passed.
5. Review `test_harness/projection_relativity_I/symbolic/results/equation_audit.md`.
6. Commit refreshed generated reports.
7. Use boundary language in the paper and README:

```text
symbolically audited and numerically validated where machine-checkable
```

## MapleSim Bridge

This harness is Maple-native symbolic and numeric verification. A future
MapleSim bridge can export verified parameters such as:

```text
T_A, T_X, D_A, N_bc, c_bc, mu_min^2, K_core = 96 R_max^2
```

into a MapleSim parameter component.
