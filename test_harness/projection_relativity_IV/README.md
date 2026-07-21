# PR-IV Symbolic and Manuscript Audit

The PR-IV harness follows the PR-I--PR-III public pattern: executable symbolic
checks are paired with a complete source inventory and checked result
artifacts.  It is dependency-free and can be run with Python 3.10 or newer.

## What is certified

The exact runner covers the seven adjustable equation-selection coordinates:

1. `(a2,a4)=(1,3/4)` in the minimal even-quartic radial class;
2. the minimal required-channel projector `span{phi1,phi3}`;
3. the terminal pre-projection orientation `sigma8=-1`;
4. the nonzero-ledger hypercharge orbit;
5. the photon null line of the fixed outer-product neutral mass matrix;
6. `(N_gen,[Phi3])=(3,[I3])` in the normalized complete/nonredundant incidence
   class; and
7. `D3=2 rho P_Z` in the fixed-kernel normalized minimal-response class.

It also checks the residual-`U(1)` dimension reduction `10 -> 4 -> 3 -> 1`,
the charged-adjoint trace, the quadratic-response functional, determinant
Hessian, physical-`Z` normalization, second-jet and EFT scope exclusions,
finite-tier monomial enumeration, the diagnostic firewall, and global
dependency-ordered composition.

## Coverage semantics

“Full coverage” has two explicit layers:

- **claim coverage** requires each theorem/proposition/lemma to name one or
  more passing executable exact checks;
- **display coverage** inventories every top-level display block and classifies
  it as direct exact coverage, a formal closure contract, an inherited earlier
  paper result, a diagnostic negative control, or an outside-class scope
  witness.

Display accounting does not claim that a definition, inherited formula, or
countermodel is a new independent theorem.  Unmapped displays or theorem
claims fail the run.

## Files

```text
symbolic/
  code/
    pr4_exact_harness.py
    pr4_equation_audit.py
    run_all_pr4_audits.py
  results/
    pr4_exact_results.json
    pr4_exact_results.csv
    pr4_exact_summary.md
    pr4_equation_inventory.csv
    pr4_theorem_inventory.csv
    pr4_coverage_summary.json
    pr4_coverage_summary.md
    PR4_RUN_SUMMARY.json
    PR4_RUN_SUMMARY.md
```

Run from the repository root:

```powershell
python test_harness\projection_relativity_IV\symbolic\code\run_all_pr4_audits.py
```

The runner exits nonzero for any failed exact check, unmapped display,
uncovered theorem claim, unresolved source reference/citation, or section-path
case regression.

