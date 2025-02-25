# Amino Acid Translation Project

This project takes a DNA sequence and translates it into a protein sequence based on the provided amino acid codon dictionary.

## How it works:
- The `protein_translation.py` script takes a DNA sequence.
- It splits the sequence into codons (sets of 3 nucleotides).
- It translates the codons into corresponding amino acids until a 'Stop' codon is encountered.
- The resulting protein sequence is printed.

## Example:
DNA sequence: `ATGGTGAGGAGGAGTAA`
Protein sequence: `MVGGG`
