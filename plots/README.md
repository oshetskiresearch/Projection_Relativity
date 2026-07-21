# Projection Relativity Plot User Map

This directory maps the public plot collections to the manuscript claims they
illustrate. It distinguishes generated plot archives, source-only generators,
inherited reference figures, and papers for which a separate plot package is
not applicable.

## Status Key

| Status | Meaning |
|---|---|
| **Available** | The archive or image contains a usable public plot. |
| **Source only** | Plot-generating code exists, but no usable generated plot archive is present. |
| **Inherited reference** | The file illustrates material inherited from an earlier paper rather than a new plot result for the directory in which it is stored. |
| **Not available** | No generated public plot archive is present for the documented source. |
| **Not applicable** | That paper has no separate plot release, so no paper directory exists here. |

## At a Glance

| Paper | Plot location | Public role |
|---|---|---|
| **PR-I** | [`projection_relativity_I/`](projection_relativity_I/) | Radial branch, Kerr recovery, regularized spacetime, and finite-core stability visualizations, with source scripts in `code/`. |
| **PR-II** | [`projection_relativity_II/`](projection_relativity_II/) | Seven electroweak, generation, flavor, CKM, and PMNS figure sets in one TAR archive. |
| **PR-III** | [`projection_relativity_III/`](projection_relativity_III/) | Four loose inherited PR-II diagrams/comparison figures retained as reference assets. |
| **PR-IV** | Not applicable | PR-IV has no standalone plot release. Its evidence is tabular and symbolic, so `plots/projection_relativity_IV/` does not exist. |

## PR-I Plots

### Available plot archives

| Archive | Plot meaning | Included formats/data |
|---|---|---|
| [`radial_branch_selection.tar.gz`](projection_relativity_I/radial_branch_selection.tar.gz) | Maps the residual over the radial coefficient plane and shows the `a2=1` unit-stiffness slice used to isolate the canonical quartic branch. | Smooth heatmap and black-and-white slice in PNG/PDF, plus the unit-slice and top-15 competing-point CSV tables. |
| [`pr_vs_kerr_ringdown_consistency.tar.gz`](projection_relativity_I/pr_vs_kerr_ringdown_consistency.tar.gz) | Compares the inherited Kerr ringdown waveform with the PR exterior prediction and magnifies the formally gap-suppressed residual. It supports Kerr consistency, not a new residual detection. | PNG and PDF. |
| [`pr_regularized_kruskal_szekeres_spacetime.tar.gz`](projection_relativity_I/pr_regularized_kruskal_szekeres_spacetime.tar.gz) | Conformal/spacetime diagram of the PR regularized Kruskal-Szekeres extension and finite-core replacement of the classical singular region. | PNG, PDF, and SVG. |
| [`pr_mass_inflation_stability.tar.gz`](projection_relativity_I/pr_mass_inflation_stability.tar.gz) | Tests bounded finite-core response under a nonlinear counter-streaming mass-inflation model, including a representative trajectory and parameter scans. | Three PNG/PDF figure pairs, single-case and scan CSV tables, and a JSON report. |

### Source-only plot

| Source | Plot meaning | Current status |
|---|---|---|
| [`code/pr_double_null_wall_stability.py`](projection_relativity_I/code/pr_double_null_wall_stability.py) | Simulates crossing ingoing/outgoing null-flux walls near the PR saturation boundary and compares the classical and finite-core response. | **Source only.** A generated public plot archive is **not available**. |

### Plot generators

The scripts under [`projection_relativity_I/code/`](projection_relativity_I/code/)
generate or support the five PR-I topics:

- `ppr_branch_residual_scan.py`: radial coefficient residual heatmap and
  `a2=1` slice;
- `pr_vs_kerr_ringdown_consistency.py`: PR/Kerr ringdown comparison;
- `pr_regularized_kruskal_szekeres_spacetime.py`: regularized spacetime diagram;
- `pr_mass_inflation_stability_tester.py`: mass-inflation single-case and scan
  figures;
- `pr_double_null_wall_stability.py`: double-null collision stability figures.

Several scripts are Colab-oriented and may include notebook magics or package
installation cells. Review those cells before running them as ordinary Python
programs.

## PR-II Plots

[`pr2_figures.tar`](projection_relativity_II/pr2_figures.tar) contains PNG and
PDF versions of seven figure sets:

| Figure | Meaning |
|---|---|
| `fig1_compact_fiber_lift` | Shows the lift from the PR-I internal geometry to the PR-II electroweak fiber, separating the inherited radial stiffness from the hypercharge and non-Abelian fibers. |
| `fig2_projection_locking_mass_spectrum` | Maps parent electroweak modes into the massive `W+`, `W-`, and `Z` modes and the massless residual photon under projection locking. |
| `fig3_weak_scale_closure_chain` | Displays the compact-boundary hierarchy from inherited PR-I inputs through weak mixing, order scale, hierarchy action, weak scale, electroweak vacuum, and the Fermi constant. |
| `fig4_generation_sheet_overlap_hierarchy` | Illustrates the generation-sheet overlap hierarchy used in the PR-II flavor construction. |
| `fig5_flavor_mass_output_comparison` | Compares generated charged-lepton, quark-threshold, and neutrino candidates with post-generation diagnostic references on a logarithmic scale. Quark entries are running/threshold diagnostics, not pole-mass claims. |
| `fig6a_ckm_matrix` | Visualizes the generated CKM quark-mixing matrix structure. |
| `fig6b_pmns_matrix` | Visualizes the generated PMNS lepton-mixing matrix structure. |

The archive preserves each figure in both raster form for convenient viewing
and vector PDF form for manuscript-quality rendering.

## PR-III Plots

The four loose files in `projection_relativity_III/` are inherited PR-II
reference assets rather than a separate PR-III-native plot suite:

| File | Meaning | Status |
|---|---|---|
| [`Figure 1.png`](<projection_relativity_III/Figure 1.png>) | PR-I internal geometry to PR-II compact electroweak lift, including the inherited radial stiffness, hypercharge phase, non-Abelian fiber, and residual boundary. | **Inherited reference** |
| [`Figure 2.png`](<projection_relativity_III/Figure 2.png>) | Projection locking from `(W1,W2,W3,B)` into physical `W+`, `W-`, `Z`, and the massless photon. | **Inherited reference** |
| [`Figure 3.png`](<projection_relativity_III/Figure 3.png>) | Weak-scale closure chain from the PR-I boundary inputs to the generated weak angle, order scale, electroweak scale, vacuum scale, and Fermi constant. | **Inherited reference** |
| [`fig5_flavor_mass_output_comparison (1).pdf`](<projection_relativity_III/fig5_flavor_mass_output_comparison (1).pdf>) | Log-scale comparison of PR-II flavor mass/threshold candidates with diagnostic reference values for charged leptons, quarks, and the two displayed neutrino states. | **Inherited reference** |

These files should not be interpreted as four new PR-III empirical tests. They
document inherited geometry and diagnostic context used by the PR-III ledger.

## PR-IV Plots

A separate PR-IV plot package is not applicable. The paper's public evidence
is supplied as exact certificates, numerical CSV/JSON tables, branch-control
matrices, and manuscript-coverage inventories under:

```text
test_harness/projection_relativity_IV/symbolic/results/
```

For that reason, `plots/projection_relativity_IV/` intentionally does not
exist.

## Extracting Plot Archives

From the repository root:

```bash
# gzip-compressed PR-I archive
tar -xzf plots/projection_relativity_I/<archive>.tar.gz

# uncompressed PR-II archive
tar -xf plots/projection_relativity_II/pr2_figures.tar
```

When publishing a figure derived from an external dataset, cite both the
applicable Projection Relativity manuscript and the original data source.
