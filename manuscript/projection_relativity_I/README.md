# Manuscript: Projection Relativity I

This directory contains the public manuscript package for **The Foundation of
Projection Relativity: A Spectral-Projection Architecture for Emergent
Relativity**.

## Directory Contents

| File | Purpose |
|---|---|
| `Oshetski_Projection_Relativity_Main.tex` | Primary LaTeX manuscript source. |
| `Oshetski_Projection_Relativity_Main.pdf` | Compiled primary manuscript. |
| `Oshetski_Projection_Relativity_Supplement.tex` | Supplementary derivations and supporting analysis. |
| `Oshetski_Projection_Relativity_Supplement.pdf` | Compiled supplement. |
| `Oshetski_Projection_Relativity_References.bib` | BibTeX references shared by the PR-I sources. |
| `figures/` | Publication-ready figure inputs referenced by the main TeX source. |
| `CITATION.cff` | Machine-readable citation metadata. |

The `figures/` directory makes the manuscript compile directly from a fresh
clone. Figure generators, generated bundles, and their availability boundaries
remain documented in
[`plots/projection_relativity_I/`](../../plots/projection_relativity_I/).

The public validation and data maps are located at:

- [`test_harness/projection_relativity_I/symbolic/`](../../test_harness/projection_relativity_I/symbolic/)
- [`test_harness/projection_relativity_I/numerical/`](../../test_harness/projection_relativity_I/numerical/)
- [`data/projection_relativity_I/`](../../data/projection_relativity_I/)

The data map records the manuscript's authoritative Section 11 numbering and
identifies which observational support archives are usable, unavailable, or
dependent on external raw data.

## Development Environment

The manuscript was developed and typeset with LaTeX using Overleaf. It can also
be compiled with a standard TeX distribution such as TeX Live, MiKTeX, or
MacTeX.

## Compile the Main Manuscript

From this directory, run:

```bash
pdflatex Oshetski_Projection_Relativity_Main.tex
bibtex Oshetski_Projection_Relativity_Main
pdflatex Oshetski_Projection_Relativity_Main.tex
pdflatex Oshetski_Projection_Relativity_Main.tex
```

## Compile the Supplement

From this directory, run:

```bash
pdflatex Oshetski_Projection_Relativity_Supplement.tex
bibtex Oshetski_Projection_Relativity_Supplement
pdflatex Oshetski_Projection_Relativity_Supplement.tex
pdflatex Oshetski_Projection_Relativity_Supplement.tex
```
