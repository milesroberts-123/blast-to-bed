# MILES ROBERTS, NOLAN BORNOWSKI 2020-08-13
# INPUT: blast results file in outfmt 6 (tab delimited text file w/o comments)
# OUTPUT: BED format tab-delimited text file, suitable to upload to JBrowse

import sys
print("Usage: python3 blast_to_bed.py <INFILE IN BLAST FORMAT 6> <OUTFILE IN BED FORMAT>")

#Open blast results file
print("Extracting blast results from %s ..." % sys.argv[1])
file = open(sys.argv[1], "r")
blast = file.readlines()

#Extract relevant columns for minimal BED format
queries = [x.split("\t")[0] for x in blast]
subjects = [x.split("\t")[1] for x in blast]
starts = [x.split("\t")[8] for x in blast]
ends = [x.split("\t")[9] for x in blast]
evalues = [x.split("\t")[10] for x in blast]

#Determine strands on subject that each query aligned to
#If query aligned to negative strand, switch start and end coordinates so that start < end
#Adjust indicies as appropriate so that indexing begins at 0
strands = []
newstarts = []
newends = []

for start, end in zip(starts, ends):
	if start < end:
		strands.append("+")
		newstarts.append(str(int(start) - 1))
		newends.append(end)
	if start > end:
		strands.append("-")
		newstarts.append(str(int(end) - 1))
		newends.append(start)

#Write output BED file
print("Writing results in BED format to %s ..." % sys.argv[2])

outf = open(sys.argv[2], 'w')

for query, newstart, newend, subject, evalue, strand in zip(queries, newstarts, newends, subjects, evalues, strands):
	bed_record = [subject, newstart, newend, query, evalue, strand]
	outf.write("\t".join(bed_record) + "\n")

outf.close()
print("Conversion complete!")
