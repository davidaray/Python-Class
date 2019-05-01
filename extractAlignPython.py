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
	



#from blast output file, add Seqbuffer to start and stop positions
#import pandas

df = pd.data_frame(BLAST, sep='\t', names=" qseqid	 sseqid	 pident	 length	 mismatch	 gapopen	 qstart	 qend	 sstart	 send	 evalue	 bitscore")

#add buffer zones to start and stop 

def Xbuffer:
	df['qend'] = df['qend'] + BUFFER
def Ybuffer:
 	df['qstart'] = df['qstart'] - BUFFER	 #npwhere (column, change, column to apply)
	if df['qstart'] <0:
		df['qstart'] = 0
	else: 
		pass 
df.apply(Xbuffer)
df.apply(Ybuffer)

#rerank blast file by e value

df.sort_values(by=['evalue'])

#create new file for each blasted TE 

file = open(TE'.fas', "w+")
for record in SeqIO.parse(INPUT, "fasta"):
	TEfile = open(TE'.fas', "a+")
	re.sub('__'(.*) '___', '#'\1'/', record.id)	
	record.id = 'CONSENSUS' + record.id
	TEfile.write(record.id + '\n', "w+")

#add top 40 blast hits to the new file  
	n=0
	while n <41:
		if seqIO.record == df['qseqid'] 
			TEfile.write(record.id, fasta, "a+") 
			n += 1
		else: 
			pass 
		
#align with muscle 

	subprocess.run(["/lustre/work/daray/software/muscle/muscle", '-i', TE, '-o', TE'.muscle.fas'])


























