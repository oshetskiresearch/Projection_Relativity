# Manuscript: Projection Relativity II

This directory contains the complete source files for the primary manuscript: **The Foundation of Projection Relativity II: Geometric Constraints on the Non-Abelian Phase Fiber**.

## Development Environment
This manuscript was developed and typeset using **LaTeX** via the **Overleaf** platform for professional scientific document management. This ensures standardized formatting, precise rendering of the geometric proofs, and rigorous structural organization of the equations.

## Directory Structure
* `Oshetski_Projection_Relativity_II_Main.tex`: The primary LaTeX source document containing the core text, derivations, and structure.
* `Oshetski_Projection_Relativity_Main_II_References.bib`: The BibTeX file containing all formal citations and astrophysical data references.
* `/plots`: Contains the high-resolution plots, projection diagrams, and observational charts used in the manuscript.

## How to Compile
If you wish to compile the PDF locally from the source files, you will need a standard TeX distribution (such as TeX Live, MiKTeX, or MacTeX). 

You can compile the document using standard `pdflatex` or `latexmk`. From your terminal in this directory, run:

```bash
pdflatex Oshetski_Projection_Relativity_II_Main.tex
bibtex Oshetski_Projection_Relativity_II_Main
pdflatex Oshetski_Projection_Relativity_II_Main.tex
pdflatex Oshetski_Projection_Relativity_II_Main.tex
