# convert-blast-to-bed
Convert the output of BLAST to a BED file format that's suitable for uploading to JBrowse.

In many types of bioinformatic analyses, (primer design, devloping gene models, etc.) it can be helpful to view BLAST alignments in a genome browser like [JBrowse](https://jbrowse.org/). This script will convert the results of any BLAST search into a simple BED file that can be easily uploaded to JBrowse, allowing BLAST alignments to be displayed alongside genome sequence.

**NOTE: THE BLAST RESULTS MUST BE IN OUTPUT FORMAT 6!**

## USAGE

The syntax for this script is as follows:

`python3 blast_to_bed.py <INFILE IN BLAST FORMAT 6> <OUTFILE IN BED FORMAT>`

For example a command like this:

`blastn -query my_sequences.fasta -db my_database -out example_blast_results.txt -num_threads 4 -evalue 1e-10 -outfmt 6`

will generate blast results in output format 6 (-outfmt 6). The resulting example_blast_results.txt file can then be converted to BED format as follows:

'python3 blast_to_bed.py example_blast_results.txt example_blast_results.bed'

The example_blast_results.bed can then be uploaded to JBrowse, along with the fasta and indexed fasta files containing the reference sequences, to get a visual representation of the BLAST alignments to reference sequences. 

## DEPENDENCIES

You must be able to run Python3 and it's sys module in order to run this script.

I tested this script with JBrowse v1.16.9 and Python v3.8.2.
