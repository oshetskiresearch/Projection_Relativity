# PR-IV Numerical Scope

Projection Relativity IV introduces no new fitted numerical output.  Its new
claims concern exact uniqueness, equation equivalence, canonical closure, and
the boundary of the declared admissible class.  Those claims are tested in the
[`../symbolic`](../symbolic) harness.

Numerical values quoted in PR-IV are inherited diagnostics from PR-I through
PR-III.  Their reproducibility artifacts remain in:

- [`../../projection_relativity_I/numerical`](../../projection_relativity_I/numerical)
- [`../../projection_relativity_II/numerical`](../../projection_relativity_II/numerical)
- [`../../projection_relativity_III/numerical`](../../projection_relativity_III/numerical)

The PR-IV source audit labels those blocks as inherited or diagnostic and
fails if any display is left unaccounted for.  Diagnostic values are never
used to select `sigma8`, `N_gen`, or the neutral coefficient `k`.
