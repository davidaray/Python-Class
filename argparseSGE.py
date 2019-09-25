import Bio
from Bio import SeqIO
import os 
import sys
import pandas as pd
import matplotlib.pyplot as plt 
from pylab import savefig 
plt.switch_backend('Agg')
import seaborn as sb
import seaborn as sns 
import argparse

#set up program commands 

def get_args():
	parser = argparse.ArgumentParser(description="This script allows repeatmasker to mask a genome in parallel by converting to .2bit and breaking it up (called batch counts). This script requires a genome, TE library, batch count, and output.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-g', '--genome', type=str, help='genome file that will be masked', required=True)
	parser.add_argument('-l', '--library', type=str, help='TE library that will be masked over the genome to identify repeat elements', required=True)
	parser.add_argument('-p', '--species', type=str, help='Stock TE library provided on repeatmasker database', required=False) 
	#need to figure out optional argument for either species or library
	parser.add_argument('-b', '--batchcount', type=int, help='Number of pieces genome will be divided into to run in parallel', default=50, required=False)
	parser.add_argument('-o', '--output', type=str, help='Output file', required=True)
	parser.add_argument('-s', '--sensitive', type=str, help='Slows run while increasing accuracy of masking ~10%', required=False)
	parser.add_argument('-f', '--fast', type=str, help='Quickens run while decreasing accuracy of masking ~10%', required=False)
	parser.add_argument('-n', '--nolow', type=str, help='Does not bother to return simple repeats in output', required=False)
	parser.add_argument('-e', '--engine', type=str, help='Determines what search engine conducts this analysis. Options are crossmatch, abblast, rmblast,  and hmmer', choices=['crossmatch', 'abblast', 'rmblast', 'hmmer'] default='crossmatch', required=False)
	args = parser.parse_args()
	GENOME = args.genome 
	LIB = args.library
	BATCH = args.batchcount 
	SENS = args.sensitive
	FAST = args.fast
	NOLOW = args.nolow
	ENG = args.engine
	OUTPUT = args.output

	return GENOME, LIB, BATCH, SENS, FAST, NOLOW, ENG, OUTPUT = get_args()

# Where RepeatMasker is stored
REPEATMASKER="/lustre/work/daray/software/RepeatMasker"; 
# Where this script can find liftUp, twoBitInfo and twoBitToFa 
UCSCBINDIR="/lustre/work/daray/software";


----
if __name__ =="__main__":main()












