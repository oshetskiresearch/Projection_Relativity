# Projection Relativity III Symbolic and Manuscript Audit

This directory contains the public symbolic verification package for
Projection Relativity III. It combines Maple-based symbolic checks with a
source audit of the equations and numerical values printed in the manuscript.

This package is distinct from the separate [`../numerical/`](../numerical/)
validation harness. The numerical harness tests the broader computational
reproducibility pipeline and is documented independently.

## Scope

The symbolic and manuscript audit has three parts:

1. **Maple symbolic verification**
   - Checks the compact `SU(2)` ledger and electroweak null mode.
   - Checks local anomaly cancellation, Witten parity, and the residual
     electromagnetic branch.
   - Checks the neutrino ordering and the one-loop strong-sector sign.
   - Checks the locked headline values used by the manuscript.
   - Runs negative controls to confirm that known incorrect alternatives are
     rejected.

2. **Full equation audit**
   - Inventories every top-level display-math block in the public LaTeX source.
   - Maps each block to direct Maple or locked-value coverage, repository
     generation coverage, diagnostic/data coverage, or explicit source and
     context coverage.
   - Passes only when no display block is left unmapped.

3. **Manuscript value audit**
   - Extracts decimal and scientific-notation values from the public LaTeX.
   - Compares paper values with the locked PR-III JSON, CSV, and report ledger
     using rounding-aware decimal checks.
   - Classifies TeX dimensions and diagram coordinates separately so layout
     numbers are not treated as physical predictions.

The equation audit provides complete display-block accounting. It does not
claim that every displayed equation is an independent Maple theorem.

## Contents

```text
symbolic/
  README.md
  paper_claims_pr3.json
  code/
    pr3_harness.mpl
    pr3_tests.mpl
    run_pr3_paper_conformance.py
    pr3_equation_audit.py
    pr3_numeric_value_audit.py
  results/
    pr3_maple_summary.md
    pr3_maple_results.csv
    equation_audit.md
    equation_map.md
    source_equation_coverage.md
    numeric_value_audit.md
    numeric_value_inventory.csv
    numeric_value_unmatched.csv
```

The manuscript audited by this package is:

```text
manuscript/projection_relativity_III/Oshetski_Projection_Relativity_III_Main.tex
```

The locked comparison ledger is maintained in the
[`Projection-Relativity_III_Sandbox`](https://github.com/oshetskiresearch/Projection-Relativity_III_Sandbox)
repository.

## Requirements

- Maple with the command-line `cmaple` or `maple` executable.
- Python 3.10 or newer for the equation and paper-value audits.
- A local checkout of the PR-III sandbox ledger for locked-value comparison.

## Running the Checks

Run the Maple tester from
`test_harness/projection_relativity_III`:

```powershell
cmaple run_pr3_maple_test.mpl
```

Run the full equation audit from the same directory:

```powershell
python symbolic\code\pr3_equation_audit.py `
  --repo ..\.. `
  --tex-root ..\..\manuscript\projection_relativity_III `
  --output-dir results
```

Run the manuscript value audit:

```powershell
python symbolic\code\pr3_numeric_value_audit.py `
  --repo C:\path\to\Projection-Relativity_III_Sandbox `
  --tex-root ..\..\manuscript\projection_relativity_III `
  --output-dir results
```

The relative `results` output path is resolved to `symbolic/results` by the
Python audit scripts.

## Checked Result

The checked public run completed with:

```text
Maple symbolic checks: PASS, 67/67
Maple negative controls: PASS, 12/12
Equation audit: PASS, 253/253 display blocks mapped
Direct Maple or locked-value coverage: 148 display blocks
Manuscript value audit: PASS, 283/283 values matched
Layout-only values classified separately: 115
Unmatched manuscript values: 0
Symbolic/public paper conformance: PASS, 82/82
```

The 2026-07-20 symbolic refresh adds direct checks for the revised canonical
neutral `C3` section: the charged-adjoint trace, rank-one and photon-null
gates, normalized quadratic-response identities, the exact `k=2` defect,
the determinant Hessian, physical-`Z` reconstruction, matter charge traces,
second-jet and EFT comparison families, and normalized incidence/equivalence
conditions. The separate numerical validation harness was intentionally not
rerun because the manuscript's locked numerical outputs did not change.

Detailed machine-readable and human-readable outputs are committed in
[`results/`](results/). The run inputs and repository revisions are recorded
in [`../RUN_SUMMARY.md`](../RUN_SUMMARY.md).
