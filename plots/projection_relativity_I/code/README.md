# Projection Relativity I Plot Generators

This directory contains the public source used to generate or support the PR-I
plot topics catalogued in the parent [`plot user map`](../../README.md).

## Sources

| File | Plot or analysis |
|---|---|
| `ppr_branch_residual_scan.py` | Radial branch residual heatmap and unit-stiffness slice. Requires the branch-residual CSV described in the script header. |
| `pr_vs_kerr_ringdown_consistency.py` | Kerr/PR ringdown consistency plot and magnified suppressed residual. |
| `pr_regularized_kruskal_szekeres_spacetime.py` | Regularized Kruskal-Szekeres spacetime diagram. |
| `pr_mass_inflation_stability_tester.py` | Nonlinear counter-streaming mass-inflation stability figures and tables. |
| `pr_double_null_wall_stability.py` | Double-null crossing-wall finite-core stability figures and tables. A generated public archive for this source is **not available**. |

## Runtime Notes

The sources require combinations of NumPy, pandas, Matplotlib, and IPython.
Several files preserve Colab/Jupyter magics such as `%matplotlib` or `!pip` and
therefore are notebook-cell sources rather than directly executable standard
Python files. Run those files in Colab/Jupyter, or convert the magic and package
installation lines before using a normal Python interpreter.

The generated archives that are publicly available are stored one directory
above this README. Their contents and interpretation boundaries are documented
in [`plots/README.md`](../../README.md).

## Availability Boundary

Source availability does not imply that a generated plot archive is present.
In particular, the double-null wall generator is public, but its generated
archive is **not available** in this repository.
