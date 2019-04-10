import argparse
import os
import sys
import re
import subprocess
import pandas as pd
from Bio import SearchIO
for Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def get_args():

	parser = argparse.ArgumentParser(description="Using a TE library, will blast TEs to a genome, extract those hits, and align in fasta format.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-g', '--genome', type=str, help='Name of the fasta formatted genome to be blasted.', required=True)
	parser.add_argument('-b', '--blastfile', type=str, help='Blast output file', required = True)
	parser.add_argument('-l', '--TE', type=str, help='List of TE consensi.', required = True)
	parser.add_argument('-b', '--buffer', type=int, help='The number of bp of flanking sequence for each hit to be extracted.', default = 1000)
	parser.add_argument('-n', '--numHits', type=str, help='The number of blast hits to extract.', default = 50)
	parser.add_argument('-a', '--align', type=str, help='Aligns blast hits with consensus via muscle', default = 'y')
	parser.add_argument('-e', '--emboss', type=int, help='Generates an EMBOSS-customized consensus.', default = 'y')

	args = parser.parse_args()
	GENOME = args.genome
	BLAST = args.blastfile
	TES = args.TE
	BUFFER = args.buffer
	NUMHITS = args.hitnumber
	ALIGN = args.align
	EMBOSS = args.emboss



	return GENOME, BLAST, TES, BUFFER, NUMHITS, ALIGN, EMBOSS

seq = seq.reverse_complement()
	
file = open(TE, "a+")
for record in SeqIO.parse(INPUT, "fasta"):
	re.sub('__'(.*) '___', '#'\1'/', record.id)	
	record.id = 'CONSENSUS' + record.id
	file.write(record.id + '\n', "a+")














