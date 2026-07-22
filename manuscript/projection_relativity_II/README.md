# Manuscript: Projection Relativity II

This directory contains the complete public source package for **The
Foundation of Projection Relativity II: Geometric Constraints on the
Non-Abelian Phase Fiber**.

## Directory Contents

| Path | Purpose |
|---|---|
| `Oshetski_Projection_Relativity_II_Main.tex` | Primary LaTeX manuscript source. |
| `Oshetski_Projection_Relativity_II_Main.pdf` | Compiled manuscript. |
| `Oshetski_Projection_Relativity_II_References.bib` | BibTeX references used by the manuscript. |
| `figures/` | Publication-ready figure inputs referenced by the TeX source. |
| `CITATION.cff` | Machine-readable citation metadata. |

The complete PR-II figure bundle and plot documentation are also available in
[`plots/projection_relativity_II/`](../../plots/projection_relativity_II/).
The copy under `figures/` is the compile-time input required by the manuscript.

## Development Environment

The manuscript was developed with LaTeX using Overleaf. It can also be built
with TeX Live, MiKTeX, or MacTeX.

## Compile

From this directory, run:

```bash
pdflatex Oshetski_Projection_Relativity_II_Main.tex
bibtex Oshetski_Projection_Relativity_II_Main
pdflatex Oshetski_Projection_Relativity_II_Main.tex
pdflatex Oshetski_Projection_Relativity_II_Main.tex
```
