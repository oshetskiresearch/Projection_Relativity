# Projection Relativity II Banded Spectral Data

This directory contains the PR-II banded radial spectral compiler and its
checked convergence table. These are generated numerical support artifacts,
not raw observational data.

## Files

| File | Purpose |
|---|---|
| [`pr2_banded_spectral_compiler.py`](pr2_banded_spectral_compiler.py) | Builds the radial operator in a harmonic-oscillator basis, solves the first four eigenpairs, evaluates the compact boundary map, and prints the derived spectral and electromagnetic quantities. |
| [`pr2_banded_spectral_compiler_results.md`](pr2_banded_spectral_compiler_results.md) | Checked convergence values for basis sizes `N=300`, `N=10,000`, and `N=15,000`. |

The compiler reports `lambda_0`, `lambda_1`, `lambda_3`, the radial spectral
gap, `c_bc`, the finite-rank leakage `p1`, the effective gap `q_bc`, and the
derived inverse electromagnetic normalization.

## Requirements

- Python 3.10 or newer
- NumPy
- SciPy

Install the numerical dependencies with:

```bash
python -m pip install numpy scipy
```

## Run

From the repository root:

```bash
python data/projection_relativity_II/pr2_banded_spectral_compiler.py
```

The checked script runs with `N=15000` and prints its result to the terminal.
That full convergence run is resource intensive and can take several minutes.
To inspect another basis size, import and call
`compile_projection_relativity_banded(N=...)` from the same module.

The broader PR-II numerical validation suite is documented in
[`test_harness/projection_relativity_II/numerical/`](../../test_harness/projection_relativity_II/numerical/).

## Interpretation Boundary

The table records convergence of the declared numerical construction. It is
not a raw measurement table, and empirical reference values are diagnostic
comparisons rather than generator inputs.
