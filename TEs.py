import os 
import argparse
import subprocess 

def get_args)_:
	parser=argparse.ArgumentParser()
	parser.add_argument('-gen', '--genome', help='data input file - FASTA', required=True)
	parser.add_argument('-out', '--output', type=str, help='name of the blast output file', required=True)
	parser.add_argument('-lib', '--TElibrary', type=str, help='the list of TEs to blast the genome with' , required=True)
	parser.add_argument('-flank', '--flankingseq', type=int, help='amount of flanking sequence you want on either side of the TE blasted', required=True)
	parser.add_argument('-num', '--seqnum', type=int, help='number of TEs you want to form a consensus sequence with', required=True)
	args=vars(parser.parse_args())
	GEN=args.genome
	LIB=args.TElibrary
	BLAST=args.output
	BUFF=args.flankingseq
	NUM=args.seqnum
	retuern GEN, LIB, BLAST, BUFF, NUM = get_args()



blastn='/lustre/scratch/kevsulli/batTEs/blast/blastn.exe'
extractAlign='perl /lustre/work/daray/extractAlign_assignment/extractAlignTEs.pl'

subprocess.run([blastn, '-query', LIB'.fa', '-db', GEN'.fa', '-out', BLAST'.blast.out', '-outfmt', '6'])

subprocess.run([extractAlign, '-genome', GEN, '-blast', BLAST'.blast.out', '-consTEs', LIB'.fa', '-seqBuffer', BUFF, '-seqNum', NUM, '-align'])