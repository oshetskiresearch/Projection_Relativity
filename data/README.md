# Projection Relativity Public Data and Reproducibility Package

This data package supports the public release of **Projection Relativity (PR)** and its companion manuscript/supplement. It contains derived tables, plots, reproducibility scripts, and audit outputs used to support the paper's numerical and observational claims.

The package is designed to be extracted into the root of the public repository:

```text
oshetskiresearch/Projection_Relativity
```

The data package is **not** intended to duplicate every raw public catalog or raw gravitational-wave strain file. Large public datasets remain external and are fetched by the supplied scripts when possible. The repository contains the derived outputs, manifests, plotting data, and reproduction instructions needed for reviewers to verify the claims without guessing which files were used.

---

## Recommended Repository Layout

After extraction, the public repository should use the following organization:

```text
Projection_Relativity/
  manuscript/
    Oshetski_Projection_Relativity_Main.tex
    Oshetski_Projection_Relativity_Supplement.tex

  test_harness/
    symbolic/
      ProjectionRelativityAppendixVerify.mpl
      run_appendix_verification.mpl
      README.md
      equation_audit.md
      equation_map.md
      equation_derivations.md
      proof_report.md
      harness_validation.md
      spectrum_recompute.md

  scripts/
    section11/
      11_1_quasar_residuals/
      11_2_gw_kerr_consistency/
      11_2_gw_residual_screen/
      11_3_magnetic_area_law/

  data/
    section11/
      11_1_quasar_residuals/
      11_2_gw_kerr_consistency/
      11_2_gw_residual_screen/
      11_3_magnetic_area_law/

  results/
    section11/
      11_1_quasar_residuals/
      11_2_gw_kerr_consistency/
      11_2_gw_residual_screen/
      11_3_magnetic_area_law/

  plots/
    section11/
      11_1_quasar_residuals/
      11_2_gw_kerr_consistency/
      11_2_gw_residual_screen/
      11_3_magnetic_area_law/

  docs/
    section11/
      README.md
      SECTION11_MANIFEST.csv
```

---

## Package Scope

This package supports three active Section 11 observational/reproducibility channels:

1. **Section 11.1 — Quasar luminosity-linked velocity residuals**
2. **Section 11.2 — Gravitational-wave Kerr consistency**
3. **Section 11.3 — Compact-phase magnetic area law / LoTSS Faraday residuals**
4. **Section 11.5 — Hubble/DESI phase-response pressure test**

The correct interpretation hierarchy is:

```text
Quasar channel:   primary positive observational diagnostic
GW channel:       Kerr recovery / consistency / no positive residual detection claimed
Magnetic channel: compact-phase area-law constraint, not a universal fixed-field claim
```

---

## Section 11.1: Quasar Luminosity-Linked Velocity Residuals

### Purpose

This is the strongest positive observational diagnostic in the current paper. The derived results package should allow a reviewer to inspect the matched-bin residual sign test, bootstrap intervals, permutation nulls, estimator breakdowns, and filtering counts.

### Expected files

```text
results/section11/11_1_quasar_residuals/
  quasar_highN_permutation_summary.csv
  quasar_highN_permutation_distribution.csv
  quasar_alt_estimator_bootstrap_summary.csv
  quasar_alt_estimator_bootstrap_distribution.csv
  quasar_alt_estimator_columnwise_warning_clean_summary.csv
  quasar_alt_estimator_columnwise_warning_clean_bins.csv
  quasar_alt_estimator_columnwise_summary.csv
  quasar_alt_estimator_columnwise_bins.csv
  quasar_alt_estimator_permutation_summary.csv
  quasar_alt_estimator_permutation_distribution.csv

plots/section11/11_1_quasar_residuals/
  quasar_estimator_negative_bin_counts.png
  quasar_permutation_null_summary.png
  quasar_bootstrap_ci_summary.png
  quasar_bin_residual_distribution.png

scripts/section11/11_1_quasar_residuals/
  quasar_residual_shared.py
  run_quasar_matched_bin_test.py
  run_quasar_permutation_test.py
  run_quasar_bootstrap_summary.py
```

### Core formula

The velocity residual used by the quasar tests is:

```text
Delta v_est = c * (z_est - z_sys) / (1 + z_sys)
```

The primary sign statistic is:

```text
Delta v_high-low = median(Delta v_est)_high_L - median(Delta v_est)_low_L
```

The PR sign prediction is:

```text
Delta v_high-low < 0
```

### Raw data policy

The public repo does not redistribute large raw quasar catalogs unless the license and size are appropriate. Prefer this structure:

```text
data/section11/11_1_quasar_residuals/raw_external_sources.md
```

That file should list catalog names, download locations, required columns, and checksums if available. Derived warning-clean and matched-bin tables belong in the release assets.

### Interpretation

The quasar channel is described as:

```text
primary positive observational diagnostic under low-ionization systemic anchoring and matched-bin controls
```

---

## Section 11.2: Gravitational-Wave Kerr Consistency

### Purpose

The gravitational-wave material supports the paper's current Kerr-consistency claim:

```text
Projection Relativity inherits the exterior Kerr ringdown hierarchy.
Projection-sector residuals are gap-suppressed.
No statistically robust public-data residual detection is claimed.
```

### Expected files

```text
results/section11/11_2_gw_kerr_consistency/
  pr_vs_kerr_ringdown_plot_data.csv
  pr_vs_kerr_ringdown_constants.csv

plots/section11/11_2_gw_kerr_consistency/
  pr_vs_kerr_ringdown_consistency.png
  pr_vs_kerr_ringdown_consistency.pdf

scripts/section11/11_2_gw_kerr_consistency/
  pr_vs_kerr_ringdown_consistency_colab.py
```

### What this supports

These files support the visual and numerical statement:

```text
A_obs = A_Kerr + A_X,
with A_X gap-suppressed relative to A_Kerr.
```

The plots should show PR and Kerr waveforms nearly overlapping, with only the formal suppressed residual displayed in a magnified panel.

### What this does not claim

This package does **not** claim a gravitational-wave detection of PR. It does not claim fixed sidebands or echo detections. Old sideband/echo exploratory files should not be used as active evidence unless clearly archived as superseded theory notes.

---

## Section 11.2 Support: Gravitational-Wave Residual / Null Screens

### Purpose

The residual-screen package documents the public-data tests that motivated the final paper's conservative GW position.

### Expected files

```text
results/section11/11_2_gw_residual_screen/
  pr_ringdown_restoration_gw150914_strong_null_results.csv
  pr_ringdown_restoration_gw150914_strong_null_summary.csv
  pr_ringdown_restoration_gw150914_nested_linear_pr_results.csv
  pr_ringdown_restoration_gw150914_nested_linear_pr_summary.csv
  pr_ringdown_restoration_large_screen_detector_windows.csv
  pr_ringdown_restoration_large_screen_detector_summary.csv
  pr_ringdown_restoration_large_screen_event_summary.csv
  pr_ringdown_restoration_focused_followup_windows.csv
  pr_ringdown_restoration_focused_followup_detector_summary.csv
  pr_ringdown_restoration_focused_followup_event_summary.csv

plots/section11/11_2_gw_residual_screen/
  *.png
  *.pdf

scripts/section11/11_2_gw_residual_screen/
  *.py
  *.ipynb
```

### Interpretation

These screens compare PR-inspired residual templates against generic drift/decay controls and off-source windows. They support the final manuscript statement:

```text
Public gravitational-wave screening did not identify a statistically robust PR-specific residual.
The GW channel is therefore treated as Kerr recovery and future high-SNR residual-stack work.
```

### Raw data policy

Raw GW strain should generally not be stored in the repo. Scripts should fetch public strain from GWOSC or other official public sources when needed.

---

## Section 11.3: Compact-Phase Magnetic Area Law / LoTSS

### Purpose

The magnetic package supports the compact-phase area-law interpretation:

```text
PR fixes a compact-phase flux normalization.
The realized projected compact-phase area determines the magnetic amplitude.
Faraday residuals constrain area and plasma-window factors.
```

### Core equations

The active magnetic relation is:

```text
B_geo^PR = Phi_theta^PR / A_proj^(theta)
```

In nanogauss units:

```text
B_geo^PR[nG] = 0.09009597185 / A_proj^(theta)[m^2]
```

The Faraday map is:

```text
RM_pred = 812 * n_e * L * B_geo^PR * W_EM
```

with:

```text
W_EM = W_orient * W_coh * W_fill * W_z
```

### Expected files

```text
results/section11/11_3_magnetic_area_law/
  magnetic_area_law_constants.csv
  magnetic_area_law_mapping.csv
  lotss_rrm2022_summary.csv
  lotss_projected_area_constraints.csv
  lotss_foreground_model_comparison.csv

plots/section11/11_3_magnetic_area_law/
  magnetic_area_law_curve.png
  lotss_projected_area_constraint.png
  lotss_foreground_model_comparison.png

scripts/section11/11_3_magnetic_area_law/
  pr_magnetic_area_law_support.py
  lotss_foreground_residual_audit.py
  lotss_area_constraint_triage.py
```
```text
scripts/section11/11_5_hubble_desi_phase_response/
  pr_hubble_phase_response_test_colab.py
  pr_hubble_desi_mixed_solution_test_colab_v2.py

results/section11/11_5_hubble_desi_phase_response/
  hubble_measurements_used.csv
  hubble_phase_response_pairwise_summary.csv
  hubble_phase_response_monte_carlo_summary.csv
  pr_hubble_desi_mixed_solution_summary.csv
  pr_hubble_desi_mixed_solution_top200.csv
  PR_HUBBLE_PHASE_RESPONSE_REPORT.md
  PR_HUBBLE_DESI_MIXED_RESPONSE_REPORT.md

plots/section11/11_5_hubble_desi_phase_response/
  h0_posterior_comparison.png
  delta_rho_theta_monte_carlo.png
  mixed_response_w0_wa_scan.png
  mixed_response_h0_rd_theta_surface.png
  desi_bao_vs_best_mixed_response.png

data/section11/11_5_hubble_desi_phase_response/
  desi_gaussian_bao_ALL_GCcomb_mean.txt
  desi_gaussian_bao_ALL_GCcomb_cov.txt
```
---

## Maple Audit and Numerical Harness

The public release includes a source-linked Maple verification harness under:

```text
test_harness/symbolic/
```

The Maple checker verifies the local repository manuscript files:

```text
manuscript/Oshetski_Projection_Relativity_Main.tex
manuscript/Oshetski_Projection_Relativity_Supplement.tex
```

It does not download files from GitHub during the run. Users should clone or download the full repository and run Maple from `test_harness/symbolic/`.

Recommended release language:

```text
symbolically audited and numerically validated where machine-checkable
```

Do not claim that Maple proves every physical interpretation. Claims requiring external catalogs, numerical backends, operator geometry, or physical assumptions are boundary-labeled in the audit reports.

---

## Data Status Labels

Use the following labels in `SECTION11_MANIFEST.csv`:

| Label | Meaning |
|---|---|
| `RAW_INCLUDED` | Raw data is included in the repo or release assets. |
| `RAW_EXTERNAL` | Raw data is public but must be downloaded from an external source. |
| `DERIVED_TABLE` | CSV/Parquet table derived from raw data or simulation output. |
| `PLOT_DATA` | Data table used directly to generate a figure. |
| `PLOT` | PNG/PDF/SVG generated figure. |
| `SCRIPT` | Reproduction or plotting script. |
| `AUDIT` | Maple/Python audit output. |
| `PLACEHOLDER` | Expected file not yet included; should not be cited as evidence. |

---

## Manifest Format

Every public data package should include a manifest row for each file:

```csv
section,channel,file_path,file_type,status,generated_by,raw_source,notes
```

Example:

```csv
11.3,magnetic_area_law,results/section11/11_3_magnetic_area_law/magnetic_area_law_mapping.csv,DERIVED_TABLE,active,scripts/section11/11_3_magnetic_area_law/pr_magnetic_area_law_support.py,internal constants,"Area-law mapping from Phi_theta_PR to projected area."
```

---

## Extracting the Tar Archives

If using the release tarballs, extract them from the repository root:

```bash
tar -xzvf pr_public_repo_section11_support_CURATED_BUNDLE.tar.gz -C /path/to/Projection_Relativity
```

Then inspect the manifest:

```bash
cat docs/section11/SECTION11_MANIFEST.csv
```

or:

```bash
python - <<'PY'
import pandas as pd
m = pd.read_csv('docs/section11/SECTION11_MANIFEST.csv')
print(m.groupby(['section','channel','status']).size())
PY
```

---

## Reproducibility Expectations

A reviewer should be able to:

1. Build the manuscript from `manuscript/`.
2. Run the Maple audit from `test_harness/symbolic/`.
3. Run or inspect the Python scripts under `scripts/section11/`.
4. Recreate the Section 11 plots from the provided derived tables.
5. Identify which raw datasets are included and which are external.
6. Confirm that obsolete claims are not used as active evidence.

---

## Citation and Use

If using this repository or derived data package, cite the main Projection Relativity manuscript and the public repository:

```text
Michael Stanislaus Oshetski, Projection Relativity: A Spectral-Projection Architecture for Emergent Relativity, 2026.
Repository: https://github.com/oshetskiresearch/Projection_Relativity
```

If a derived table uses an external public catalog, also cite the original catalog or survey according to that dataset's license and citation policy.

---

## Contact

For questions about the repository, derivation ledger, or reproducibility package, use the contact information listed in the main manuscript.
