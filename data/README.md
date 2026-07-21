# Projection Relativity Data User Map

This directory is the public guide to data and generated numerical ledgers for
the Projection Relativity manuscript series. It distinguishes usable release
artifacts from empty placeholders, external raw sources, and papers for which a
separate data package is not applicable.

## Status Key

| Status | Meaning |
|---|---|
| **Available** | The file contains a usable dataset, generated ledger, script, or result. |
| **External raw data** | The underlying public catalog or strain data is not redistributed here; the release contains derived products or retrieval instructions. |
| **Empty placeholder** | The named file exists but contains no usable archive content and must not be cited as a dataset. |
| **Not applicable** | That paper has no separate public data package, so no paper directory exists here. |

## At a Glance

| Paper | Data location | Public role |
|---|---|---|
| **PR-I** | [`projection_relativity_I/`](projection_relativity_I/) | Compact-phase precision audit, two usable Section 11.3 gravitational-wave support archives, and explicit placeholders for unavailable Section 11.1, 11.2, and 11.5 packages. |
| **PR-II** | [`projection_relativity_II/`](projection_relativity_II/) | Banded radial spectral compiler and its convergence table. |
| **PR-III** | [`projection_relativity_III/`](projection_relativity_III/) | Forty-four JSON calculation ledgers and inputs paired by stage with forty-one Python generators. These are generated scientific ledgers, not raw experimental datasets. |
| **PR-IV** | Not applicable | PR-IV adds no independent data package. Its exact and numerical outputs are under `test_harness/projection_relativity_IV/symbolic/results/`, so `data/projection_relativity_IV/` does not exist. |

## PR-I Data

The detailed PR-I policy and the interpretation of its observational channels
are documented in
[`projection_relativity_I/README.md`](projection_relativity_I/README.md).

### Available archives

| Archive | What it contains | Intended use |
|---|---|---|
| [`pr_public_section_10_compact_phase_fsc.tar`](projection_relativity_I/pr_public_section_10_compact_phase_fsc.tar) | A 20-digit compact-phase/fine-structure precision audit script, JSON report, and CSV summary. | Reproduce the high-precision compact-boundary arithmetic reported for the PR-I electromagnetic sector. |
| [`pr_public_section11_3_gw_kerr_consistency_support.tar.gz`](projection_relativity_I/pr_public_section11_3_gw_kerr_consistency_support.tar.gz) | Ringdown sample and summary CSV files, PNG/PDF plots, and the generating Python script. | Check the Section 11.3 claim that the PR exterior ringdown follows the Kerr hierarchy with only a formally suppressed projection-sector residual. This is a consistency test, not a detection claim. |
| [`pr_public_section11_3_gw_residual_screen_support.tar.gz`](projection_relativity_I/pr_public_section11_3_gw_residual_screen_support.tar.gz) | GW150914 screens, large-event and focused-follow-up tables, kernel and template interfaces, diagnostic plots, scripts, and theory notes. | Reproduce the conservative Section 11.3 public-data residual/null screens. The active interpretation is that no statistically robust PR-specific residual was identified. |

### Empty placeholders

The following files are each two bytes in the current public tree. They are not
valid TAR archives and contain no usable data:

| File | Intended channel | Current status |
|---|---|---|
| `pr_public_section11_1_quasar_support.tar` | Section 11.1 quasar luminosity-linked velocity-residual support. | **Empty placeholder** |
| `pr_public_section11_2_magnetic_area_law_support.tar.gz` | Section 11.2 compact-phase magnetic area-law and Faraday-residual support. | **Empty placeholder** |
| `pr_public_section11_5_hubble_desi_phase_response.tar` | Hubble/DESI phase-response pressure test. | **Empty placeholder** |

Do not extract, cite, or treat these placeholders as released datasets. The
PR-I README records the authoritative manuscript numbering and the precise
external-data boundary for those channels. Section 11.4 has no separate data
archive because its displayed magnetar relations are analytic.

There is no separate externally hosted PR-I support bundle in the public
release contract. Usable PR-I support archives are checked into
`data/projection_relativity_I/`; third-party raw catalogs and strain data remain
external under their original providers' terms.

### Raw-data boundary

Large quasar catalogs and public gravitational-wave strain are not generally
redistributed. When used, they remain subject to their original archive,
license, and citation requirements. The public repository should contain only
the derived tables, scripts, checksums, and source instructions needed to make
the analysis traceable.

## PR-II Data

PR-II contains one numerical convergence dataset and its generator:

| File | Purpose |
|---|---|
| [`pr2_banded_spectral_compiler.py`](projection_relativity_II/pr2_banded_spectral_compiler.py) | Builds the PR radial operator as a sparse banded harmonic-basis matrix, computes the converged spectral levels and gap, evaluates the compact-boundary leakage, and derives the boundary electromagnetic normalization. Requires NumPy and SciPy. |
| [`pr2_banded_spectral_compiler_results.md`](projection_relativity_II/pr2_banded_spectral_compiler_results.md) | Checked convergence table at basis sizes `N=300`, `N=10,000`, and `N=15,000`, including `lambda_0`, `lambda_1`, `lambda_3`, the spectral gap, `c_bc`, `p_1`, `q_bc`, and the derived inverse fine-structure value. |

There is no separate PR-II raw observational dataset in this directory. PR-II
validation outputs and diagnostic reference tables belong under
`test_harness/projection_relativity_II/`.

## PR-III Data

PR-III is organized as a reproducible calculation ledger:

```text
projection_relativity_III/
|-- code/    41 standard-library Python generators
|-- data/    44 JSON ledgers, inputs, audits, and decisions
`-- README.md
```

Run a generator from the repository root so its sibling paths remain stable.
For example:

```powershell
python data/projection_relativity_III/code/pr3_v08f_final_priii_consistency_statement.py
```

The full numerical and canonical-output audit is under
[`../test_harness/projection_relativity_III/numerical/`](../test_harness/projection_relativity_III/numerical/).

### Foundation and inherited inputs

| JSON file | Meaning |
|---|---|
| `locked_reference_sources.json` | Identifies the locked PR-I and PR-II source files used to synchronize inherited inputs. |
| `inheritance_ledger.json` | Canonical ledger of PR-I/PR-II objects frozen before PR-III generation. |
| `scalar_hessian_seed.json` | Scalar-amplitude Hessian seed, inherited couplings, and electroweak mass-block inputs. |
| `gauge_null_quotient_seed.json` | Gauge-null subspace removal and physical quotient construction. |
| `radiative_determinant_seed.json` | One-loop determinant/supertrace architecture and reference-normalization convention. |

### Electromagnetic and radiative ledgers

| JSON file | Meaning |
|---|---|
| `alpha_baseline_policy.json` | Declares the adopted PR-III tree-level inverse-alpha baseline and no-fit policy. |
| `alpha_convergence_N300_N10000_N15000.json` | Frozen radial convergence sequence across three basis sizes. |
| `alpha_radiative_extraction_protocol_seed.json` | Locks the radiative extraction, gauge, charge, and diagnostic conventions. |
| `charged_mode_supertrace_inventory.json` | Charged-mode inventory, supertrace signs, and charge-square audits. |
| `pr_spectral_kernel_seed.json` | Spectral regulator, kernel architecture, thresholds, and boundary anchors. |
| `alpha_radiative_candidate_minimal_boundary.json` | First generated minimal-boundary radiative candidate. |
| `alpha_no_fit_diagnostic_refinement.json` | Post-generation diagnostic comparison and allowed refinement decision. |
| `alpha_radiative_candidate_D1_D2.json` | Generated `D1+D2` refinement and acceptance-gate results. |
| `alpha_final_no_fit_precision_audit.json` | Final no-fit precision audit of the electromagnetic candidate. |
| `alpha_residual_closure_current_precision.json` | Current-precision residual bound and final comparison ledger. |

### Electroweak ledgers

| JSON file | Meaning |
|---|---|
| `electroweak_scale_transport_protocol_seed.json` | Locks the scale-transport protocol, weak-angle boundary, coupling reconstruction, and ledger equations. |
| `electroweak_running_inventory_kernel_seed.json` | Defines the electroweak running inventory, thresholds, and kernel class. |
| `electroweak_running_candidate_C1.json` | First transported-coupling and weak-mass candidate. |
| `electroweak_weak_mass_ledger_audit_C1.json` | Internal audit of the C1 weak-mass ledger. |
| `electroweak_diagnostic_comparison_C1.json` | Post-generation C1 comparison with locked diagnostic references. |
| `electroweak_weak_angle_oblique_refinement_decision.json` | Tests the weak-angle-only option and records the refinement decision. |
| `electroweak_vector_self_energy_candidate_C2.json` | Generated C2 vector self-energy correction and corrected weak ledger. |
| `electroweak_diagnostic_comparison_C2.json` | Post-generation C2 diagnostic comparison and improvement over C1. |
| `electroweak_final_precision_audit.json` | Final electroweak precision and no-fit provenance audit. |
| `electroweak_neutral_D3_candidate_C3.json` | Generated neutral D3/C3 candidate and corrected mass ledger. |
| `electroweak_neutral_D3_refinement_C3.json` | Companion D3 refinement ledger retained with the candidate output. |

### Neutrino ledgers

| JSON file | Meaning |
|---|---|
| `neutrino_branch_radiative_stability_seed.json` | Locks the inherited PR-II neutrino branch and radiative-stability form. |
| `neutrino_radiative_kernel_seed.json` | Defines the neutrino radiative kernel and stability envelope. |
| `neutrino_mbb_stability_envelope.json` | Effective Majorana-mass and mass-branch stability envelope. |
| `neutrino_ordering_pmns_stability_audit.json` | Normal-ordering, mass-squared, and PMNS stability checks. |
| `neutrino_diagnostic_comparison.json` | Post-generation comparison with neutrino diagnostic references. |
| `neutrino_final_closure_audit.json` | Final neutrino closure and no-fit provenance audit. |

### Strong-sector ledgers

| JSON file | Meaning |
|---|---|
| `strong_phase_fiber_closure_seed.json` | Locks the strong phase-fiber branch and SU(3) group ledger. |
| `strong_spectral_running_kernel_seed.json` | Defines the one-loop running kernel and threshold policy. |
| `strong_one_loop_color_audit.json` | Audits the color factor and one-loop beta-function sign table. |
| `strong_threshold_active_flavor_audit.json` | Audits quark thresholds and the active-flavor count across intervals. |
| `strong_diagnostic_comparison.json` | Post-generation comparison with the locked strong-sector reference. |
| `strong_final_closure_audit.json` | Final strong-sector closure and provenance decision. |

### Global ledgers

| JSON file | Meaning |
|---|---|
| `global_running_anomaly_ledger_seed.json` | Collects sector ledgers and defines the global audit queue. |
| `global_anomaly_registry_audit.json` | Audits local anomalies, SU(2) Witten parity, residual electromagnetism, and generation scaling. |
| `global_running_continuity_audit.json` | Checks continuity across the declared running and threshold transitions. |
| `global_no_fit_provenance_manifest.json` | Records allowed inputs and no-fit provenance sector by sector. |
| `global_cross_sector_diagnostic_table.json` | Consolidates post-generation cross-sector diagnostic comparisons. |
| `global_final_priii_consistency_statement.json` | Final PR-III sector status, safe manuscript statement, excluded overclaims, and remaining scope boundaries. |

## PR-IV Data

A separate PR-IV data package is not applicable. PR-IV is a theorem and
reproducibility paper whose public artifacts are exact checks, generated CSV
tables, JSON certificates, and manuscript-coverage inventories. They live in:

```text
test_harness/projection_relativity_IV/symbolic/results/
```

For that reason, `data/projection_relativity_IV/` intentionally does not exist.

## Extracting Available Archives

From the repository root, extract an available archive into a separate working
directory rather than treating its internal paths as live public-tree paths:

```bash
mkdir pr1_archive_work

# gzip-compressed TAR archive
tar -xzf data/projection_relativity_I/<archive>.tar.gz -C pr1_archive_work

# uncompressed TAR archive
tar -xf data/projection_relativity_I/<archive>.tar -C pr1_archive_work
```

Only files marked **Available** above should be extracted. Preserve each
archive's internal paths so scripts, data, results, plots, and documentation
remain linked.

## Citation and Interpretation

Generated ledgers are not raw observations. Diagnostic reference values enter
only where each paper labels them as post-generation comparisons. When an
artifact depends on an external survey, catalog, or public strain archive,
cite both the Projection Relativity manuscript and the original data provider.
