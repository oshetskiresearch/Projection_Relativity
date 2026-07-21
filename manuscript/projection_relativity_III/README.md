# Manuscript: Projection Relativity III

This directory contains the complete source files for the primary manuscript:
*The Foundation of Projection Relativity III: Zero-Parameter Radiative and
Cross-Sector Closure of the Projection Ledger*.

**Release DOI:** [10.5281/zenodo.21361507](https://doi.org/10.5281/zenodo.21361507)

## Development Environment

This manuscript was developed and typeset using LaTeX via the Overleaf
platform for professional scientific document management. This ensures
standardized formatting, precise rendering of the radiative and cross-sector
derivations, and rigorous structural organization of the equations.

## Directory Structure

- `Oshetski_Projection_Relativity_III_Main.tex`: The primary LaTeX source
  document containing the core text, derivations, figures, and manuscript
  structure.
- `Oshetski_Projection_Relativity_III_References.bib`: The BibTeX file
  containing all formal citations and referenced scientific sources.
- `Oshetski_Projection_Relativity_III_Main.pdf`: The compiled public manuscript.

The broader repository stores the PR-III validation harness under
`test_harness/projection_relativity_III/` and its public construction data under
`data/projection_relativity_III/`.

## How to Compile

To compile the PDF locally, install a standard TeX distribution such as TeX
Live, MiKTeX, or MacTeX. From a terminal in this directory, run:

```bash
pdflatex Oshetski_Projection_Relativity_III_Main.tex
bibtex Oshetski_Projection_Relativity_III_Main
pdflatex Oshetski_Projection_Relativity_III_Main.tex
pdflatex Oshetski_Projection_Relativity_III_Main.tex
```

Alternatively, if `latexmk` is installed:

```bash
latexmk -pdf Oshetski_Projection_Relativity_III_Main.tex
```
