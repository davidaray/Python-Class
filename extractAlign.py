import argparse
import os
import sys
import re
import subprocess
import pandas as pd
from Bio import SearchIO
from Bio import SeqIO
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

#df = pd.data_frame(BLAST, sep='\t', names=['QUERYNAME', 'SCAFFOLD', 'C', 'D', 'E', 'F', 'QUERYSTART', 'QUERYSTOP', 'SCAFSTART', 'SCAFSTOP', 'E-VALUE', 'BITSCORE'])

#make TE output file function 
def CREATE_TE_OUTFILES(TES):
	for record in SeqIO.parse(TES, 'fasta'):
		NEWID = re.sub('#', '__', record.id)
		NEWID = re.sub('/', '___', NEWID)
		record.id = 'CONSENSUS-' + NEWID
		record.description = ''
		SeqIO.write(record, NEWID + '.fas', 'fasta')

#import blast data 
df = pd.data_frame('BLAST', sep='\t', names=['QUERYNAME', 'SCAFFOLD', 'C', 'D', 'E', 'F', 'QUERYSTART', 'QUERYSTOP', 'SCAFSTART', 'SCAFSTOP', 'E-VALUE', 'BITSCORE'])

#add buffer zones to start and stop 
df.loc[:, 'QUERYSTART'] = df.loc[: 'QUERYSTART'] - BUFFER #introduces buffer number to the blast file
df.loc[df['QUERYSTART']<0, 'QUERYSTART'] = 0  
df.loc[:, 'QUERYSTOP'] = df.loc[: 'QUERYSTOP'] + BUFFER

#rerank blast file by e value

df.sort_values(by=['E-VALUE', 'BITSCORE'], ascending=[True, False])

#determine blast hits 
blastscaffold=df["SCAFFOLD"]
blastscaffold=blastscaffold.unique()
for hit in blastscaffold:
	blasthits = blastscaffold.head(BUFFER)
	
	
for record in SeqIO.parse('HLphyDis2.fa', "fasta"):
	if blastscaffold in record.id:
		f.write(str(seq_record.id) + "\n")
			f.write(str(seq_record.seq['QUERYSTART':'QUERYSTOP']) + "\n")
				



	n=0
	while n <41:
		if  blastid in record.id: 
			#call function to pull out sequence from genome 
			SeqIO.write(record, 'pDis_rnd-5_family-2483__LTR___ERV1_cons.fas', 'fasta')
#			TEfile.write('>'+record.id + '\n' + str(record.seq) '\n', TEfile, 'fasta') #write record,not record.id;  
			n += 1
		else: 
			pass 
		
#align with muscle 

	subprocess.run(["/lustre/work/daray/software/muscle/muscle", '-i', TE, '-o', TE'.muscle.fas']) #need to make this optional 
















#rerank blast file by e value

df.sort_values(by=['E-VALUE', 'BITSCORE'], ascending=[True, False]) 

#create new file for each blasted TE 
blastid=df["QUERYNAME"]

#file = open(TE'.fas', "w+")
for record in SeqIO.parse(INPUT, "fasta"):
for record in SeqIO.parse('pDis_rnd12.fas', "fasta"):
	seq = str(record.seq)
	record-id = re.sub('#', '__', record.id)
	record-id = re.sub('/', '___', record-id)
	record = 'CONSENSUS' + record-id
	with open(record-id+'.fas', "w+") as output:
		output.write(">CONSENSUS_" + record + '\n' + '\n')
#	SeqIO.write(record.seq, record-id+'.fas', "fasta")
	
#add top 40 blast hits to the new file  
	n=0
	while n <41:
		if  blastid in record.id: 
			SeqIO.write(record, 'pDis_rnd-5_family-2483__LTR___ERV1_cons.fas', 'fasta')
#			TEfile.write('>'+record.id + '\n' + str(record.seq) '\n', TEfile, 'fasta') #write record,not record.id;  
			n += 1
		else: 
			pass 
		
#align with muscle 

	subprocess.run(["/lustre/work/daray/software/muscle/muscle", '-i', TE, '-o', TE'.muscle.fas']) #need to make this optional 

blastid=df["QUERYNAME"]              
blastscaffold=df["SCAFFOLD"]
file = open(TE'.fas', "w+")
for record in SeqIO.parse(INPUT, "fasta"):
    TEfile = open(TE'.fas', "a+")
    re.sub('__'(.*) '___', '#'\1'/', record.id)    
    record.id = 'CONSENSUS' + record.id
    TEfile.write(record.id + '\n', "w+")

#add top 40 blast hits to the new file
import Bio
from Bio import SeqIO
for RECORD in SeqIO.parse('allTEsCper.fasta', 'fasta'):
	if 'CONSENSUS' in RECORD.id:
		HITSFILE = open('CperConsensi.fasta', 'a+')
		SeqIO.write(RECORD, HITSFILE, 'fasta')
	else: 
		pass
		

		
		
SUBSLICE coordinates
define query: query = record[start:stop]
output query to new file 

with open(BLAST,"w") as f:
        for seq_record in SeqIO.parse(GENOME, "fasta"):
                f.write(str(seq_record.id) + "\n")
                f.write(str(seq_record.seq['QUERYSTART':'QUERYSTOP']) + "\n")  #first 10 base positions


df = pd.data_frame('testblast.out', sep='\t', names=['QUERYNAME', 'SCAFFOLD', 'C', 'D', 'E', 'F', 'QUERYSTART', 'QUERYSTOP', 'SCAFSTART', 'SCAFSTOP', 'E-VALUE', 'BITSCORE'])
blastscaffold=df["SCAFFOLD"]
with open('testoutput.txt',"w") as f:
		for record in SeqIO.parse('HLphyDis2.fa', "fasta"):
			if blastscaffold in seq_record.id:
				f.write(str(seq_record.id) + "\n")
				f.write(str(seq_record.seq['QUERYSTART':'QUERYSTOP']) + "\n")
				
				
				
				
	