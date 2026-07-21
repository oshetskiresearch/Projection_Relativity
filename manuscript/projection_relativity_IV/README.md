# Manuscript: Projection Relativity IV

This directory contains the complete source files for the primary manuscript:
*The Foundation of Projection Relativity IV: The Global Singleton Theorem—
Axiom-by-Axiom Uniqueness and Canonical Closure of the Complete Projection
Relativity Architecture*.

**Release DOI:** [10.5281/zenodo.21477033](https://doi.org/10.5281/zenodo.21477033)

## Development Environment

This manuscript was developed and typeset using LaTeX via the Overleaf
platform for professional scientific document management. This ensures
standardized formatting, precise rendering of the global uniqueness proofs and
canonical-closure arguments, and rigorous structural organization of the
equations.

## Directory Structure

- `Oshetski_Projection_Relativity_IV_Main.tex`: The primary LaTeX source
  document containing the preamble, front matter, bibliography configuration,
  and ordered section inputs.
- `Oshetski_Projection_Relativity_IV_References.bib`: The BibTeX file
  containing all formal citations and referenced scientific sources.
- `Oshetski_Projection_Relativity_IV_Main.pdf`: The compiled public manuscript.
- `CITATION.cff`: Citation File Format metadata for the manuscript and its
  Zenodo release.
- `sections/`: The lowercase, case-sensitive directory containing the complete
  ordered body sections and appendices loaded by the main source.

The public PR-IV exact, numerical, scope-control, and manuscript-coverage
harness is stored under `test_harness/projection_relativity_IV/`.

## How to Compile

To compile the PDF locally, install a standard TeX distribution such as TeX
Live, MiKTeX, or MacTeX. Keep the `sections/` directory beside the main source.
From a terminal in this directory, run:

```bash
pdflatex Oshetski_Projection_Relativity_IV_Main.tex
bibtex Oshetski_Projection_Relativity_IV_Main
pdflatex Oshetski_Projection_Relativity_IV_Main.tex
pdflatex Oshetski_Projection_Relativity_IV_Main.tex
```

Alternatively, if `latexmk` is installed:

```bash
latexmk -pdf Oshetski_Projection_Relativity_IV_Main.tex
```
