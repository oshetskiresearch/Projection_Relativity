# Projection Relativity III

**Working title:** *The Foundation of Projection Relativity III: Radiative Closure, Scalar Hessian, and the Strong Phase Fiber*

This directory contains the working documentation, equation ledger, and compiler audit plan for Projection Relativity III (PR-III).

PR-III is not a new theory branch. It is the forced continuation of the PR-I/PR-II projection ledger:

```text
PR-I  -> bosonic spectral-projection foundation
PR-II -> electroweak / flavor boundary closure
PR-III -> radiative precision, scalar Hessian, and SU(3) strong phase-fiber closure
```

## Central mission

PR-III tests whether the PR-II electroweak/flavor boundary ledger survives the precision layer:

\[
\boxed{\text{radiative closure} + \text{scalar Hessian stability} + SU(3)_c\ \text{phase-fiber topology}}
\]

The manuscript should remain a staged closure program, not a broad theory-of-everything expansion.

## Core rule

No new empirical knobs.

Every PR-III correction must be derived from inherited projection geometry, not fitted to measured particle data. CODATA, PDG, oscillation, CKM, PMNS, or QCD target values may be used only as diagnostic references after PR-III has generated its own values.

## Main working documents

- [`PR3_Scope_Ledger.md`](PR3_Scope_Ledger.md) — inherited objects, new objects, forbidden inputs, required outputs, and hard failure conditions.
- [`PR3_Equation_Dependency_Graph.md`](PR3_Equation_Dependency_Graph.md) — dependency chain from the master projection field to the radiative and strong-sector outputs.
- [`PR3_Compiler_Audit_Plan.md`](PR3_Compiler_Audit_Plan.md) — planned validation modules and no-fit audit structure.
- [`notes/External_Alignment_Ledger.md`](notes/External_Alignment_Ledger.md) — outside papers and observations classified as direct tests, benchmark analogs, adjacent prior art, or conceptual alignment.

## First closure gates

PR-III should not be released as a manuscript until the following gates are internally documented:

1. Scalar Hessian stability after gauge-null removal.
2. PR-native radiative determinant / effective action.
3. Fine-structure radiative gap closure without CODATA input.
4. Electroweak precision stability.
5. Neutrino branch radiative stability.
6. SU(3) generator, trace, and boundary closure.
7. Running-coupling and anomaly audits.
8. Full no-fit audit.

## Immediate first calculation

Do **not** start with SU(3). Start with the scalar Hessian and radiative layer:

\[
\mathcal H_{\rm PR}
\rightarrow
\Delta\Gamma_{\rm PR}^{(1)}
\rightarrow
\Delta\alpha_{\rm PR,rad}^{-1}.
\]

Only after this is stable should PR-III open the strong phase-fiber closure.
