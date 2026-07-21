# Projection Relativity I Numerical Validation Harness

This README documents the Python numerical validation harness for the public
Projection Relativity repository.

The harness is intended to complement the Maple symbolic checker. Use the
release language:

```text
symbolically audited and numerically validated where machine-checkable
```

It checks the numerical and formula-level claims that are
machine-checkable from the manuscript, supplement, and embedded benchmark
constants.

## Main File

The current Colab-ready harness file is:

```text
test_harness/projection_relativity_I/numerical/code/projection_relativity_numerical_validation_harness.py
```
The script writes outputs to:

```text
projection_relativity_numerical_validation_outputs/
projection_relativity_numerical_validation_outputs.tar.gz
```

## What It Checks

The suite numerically checks:

- radial branch operator spectrum and locked reference constants
- radial convergence, branch stability, and non-tuning scans
- boundary cofactor and finite-rank alpha closure
- compact magnetic area law
- propagator subtraction, positivity, and cutoff stability
- finite-core, displacement, trace-free source, and dimensional checks
- weak-gravity GR recovery benchmarks
- Mercury perihelion precession
- solar-grazing light bending
- Shapiro delay scaling
- de Sitter geodetic precession
- Lense-Thirring frame-dragging scaling
- Hulse-Taylor binary-pulsar orbital decay
- strong-gravity Schwarzschild and Kerr exterior checks
- Kerr horizon, ergosurface, ISCO, photon-region, frame-dragging, and QNM scaling checks
- gap-suppressed residual diagnostics
- formula-level Hubble, quasar residual, and Friedmann GR-limit diagnostics
- optional stress-mode scans and failure-injection tests
- optional paper/supplement source-text checks when `.tex` files are present

## What It Does Not Check

The numerical harness does not replace:

- the Maple symbolic proof checker
- full differential-geometry verification of Teukolsky operator equivalence
- empirical catalog reanalysis unless those data files and scripts are supplied
- formal proof of physical assumptions such as positivity, boundary locking, or data-selection validity

Quasar and observational sections are checked at the displayed formula and
summary-arithmetic level unless the underlying catalogs are included.

## Requirements

Python packages:

```text
numpy
pandas
scipy
matplotlib
```

Optional:

```text
qnm
```

If `qnm` is not installed, the harness uses an analytic Kerr 220 fallback and
records that fallback in the output table. This is expected and still produces
a valid machine-checkable run.

## Run In Google Colab

1. Open a new Colab notebook.
2. Upload `projection_relativity_numerical_validation_harness.py` from the
   repository's `test_harness/projection_relativity_I/numerical/code/`
   directory.
3. Optional but recommended: upload the current paper and supplement `.tex`
   files into `/content` to activate document source checks.
4. Run:

```python
%run projection_relativity_numerical_validation_harness.py
```

For the deeper stress run:

```python
import os
os.environ["PR_STRESS_MODE"] = "1"
%run projection_relativity_numerical_validation_harness.py
```

The script creates:

```text
/content/projection_relativity_numerical_validation_outputs/
/content/projection_relativity_numerical_validation_outputs.tar.gz
```

Download the archive from Colab after the run.

## Run Locally

From the repository root:

```bash
python test_harness/projection_relativity_I/numerical/code/projection_relativity_numerical_validation_harness.py
```

For stress mode:

```bash
python test_harness/projection_relativity_I/numerical/code/projection_relativity_numerical_validation_harness.py --stress
```

If `python` is not on your path, use the full path to your Python executable.

## Source-Text Checks

The numerical harness can scan paper and supplement `.tex` files if they are
available in the runtime.

It searches common runtime locations such as:

```text
the repository root and its subdirectories
/content
```

To activate source-text checks in Colab, upload:

```text
Oshetski_Projection_Relativity_Main.tex
Oshetski_Projection_Relativity_Supplement.tex
```

If no `.tex` files are found, the harness may report a document-source
`WARNING`. This means the numerical checks ran, but paper-source wording checks
were not activated. For a release run, include the `.tex` files and require the
document-source scorecard row to pass.

## Standard Mode Vs Stress Mode

Standard mode runs the core validation suite.

Stress mode adds deeper tests, including:

- radial domain-size convergence stress scans
- wider radial branch parameter perturbations
- independent radial method cross-checks
- propagator cutoff stability sweeps
- finite-core mass scans across compact-object and supermassive scales
- near-extremal Kerr scans
- expected-failure injection checks

## Expected Current Stress Result

A healthy stress run with source `.tex` files present should have:

```text
OVERALL STATUS: PASS
RUN MODE: stress
FAIL: 0
WARNING: 0
```

The stress summary is:

```text
PASS: 113
WARNING: 0
FAIL: 0
QNM backend: analytic Kerr 220 fit fallback
```

The QNM fallback line is acceptable unless the release specifically requires
the optional `qnm` package.

## Output Files

The script writes a report and machine-readable CSV/JSON outputs.

Important files:

```text
projection_relativity_numerical_validation_outputs/
  numerical_validation_report.md
  projection_relativity_numerical_validation_results.csv
  validation_scorecard.csv
  summary.json
  radial_branch_spectrum.csv
  radial_convergence_scan.csv
  radial_operator_stability_scan.csv
  radial_vacuum_selection_scan.csv
  boundary_and_alpha_closure.csv
  magnetic_area_law_examples.csv
  propagator_low_energy_residual.csv
  propagator_spectral_stability_scan.csv
  weak_gravity_recovery.csv
  weak_gravity_precision_tests.csv
  weak_gravity_reference_values.csv
  binary_pulsar_orbital_decay.csv
  strong_gravity_kerr_core_checks.csv
  kerr_exterior_scan.csv
  kerr_qnm_gap_suppressed_residual.csv
  cosmology_gr_limit_checks.csv
  hubble_quasar_diagnostics.csv
```

Stress-mode runs also include files beginning with:

```text
stress_
```

Plots are written under:

```text
projection_relativity_numerical_validation_outputs/plots/
```

The entire output folder is bundled as:

```text
projection_relativity_numerical_validation_outputs.tar.gz
```

## Reading The Scorecard

The main scorecard categories are:

- `Core theory numerics`
- `Weak-gravity GR recovery`
- `Strong-gravity GR exterior`
- `Physical semantics`
- `Phenomenology diagnostics`
- `Paper/supplement source text`
- `Stress and failure injection` in stress mode

Status meanings:

- `PASS`: the check passed.
- `WARNING`: a nonfatal boundary or optional source-text condition needs review.
- `FAIL`: release blocker.
- `OPEN`: intentionally unresolved or not active in this run.

## Relationship To Maple

Use both harnesses:

```text
Maple checker  -> symbolic, algebraic, dimensional, trace, and source-text audit
Python checker -> numerical, convergence, stability, GR benchmark, and stress audit
```

The Maple and local Python checkers should be run from the repository root after
updating the checkout. The Python checker can also run in Colab.

Recommended release workflow:

1. Update the repository.
2. Run the Maple checker against the repo-local manuscript files.
3. Run this Python numerical harness in stress mode.
4. Confirm `MANUSCRIPT count: 0` in Maple.
5. Confirm `FAIL: 0` and `WARNING: 0` in the Python report.
6. Commit the refreshed reports and output archive if the repo is meant to store validation artifacts.

## Troubleshooting

### Missing Python Packages

Install the required packages:

```bash
python -m pip install numpy pandas scipy matplotlib
```

In Colab, the script attempts to install missing required packages
automatically.

### QNM Backend Not Installed

If the output says:

```text
analytic Kerr 220 fit fallback
```

that means the optional `qnm` package was not available. The fallback is
acceptable for the default validation harness, but install `qnm` if you want to
compare against that backend.

### Document Source Warning

Upload or place the paper and supplement `.tex` files next to the script or in
`/content`:

```text
Oshetski_Projection_Relativity_Main.tex
Oshetski_Projection_Relativity_Supplement.tex
```

Then rerun the harness.

### Colab Argument Errors

Do not call the script through an argument parser cell that inherits Jupyter
kernel arguments. Use:

```python
%run projection_relativity_numerical_validation_harness.py
```

or set stress mode with:

```python
import os
os.environ["PR_STRESS_MODE"] = "1"
%run projection_relativity_numerical_validation_harness.py
```

### Output Archive Missing

The archive is created at the end of a successful run:

```text
projection_relativity_numerical_validation_outputs.tar.gz
```

If it is missing, check whether the run stopped early because of a failed import
or filesystem permission issue.

## Release Boundary Statement
```text
The Projection Relativity manuscript is symbolically audited and numerically
validated where machine-checkable. The Maple harness verifies symbolic,
algebraic, dimensional, and source-text consistency; the Python harness checks
numerical spectra, convergence, stability, GR benchmark recovery, and stress
tests. Claims requiring external catalogs, physical assumptions, or full
differential-geometry backends are recorded as bounded validation scope rather
than asserted as fully proven by the harnesses.
```
