

###############################################################
#####                Python Assignment #3                 #####
##### Creating sliding windows and Calculating GC content #####
###############################################################


##### Steps to take #####
# 1. Only use scaffolds with a minimum length (Ex: 30,000 bp)
# 2. Create sliding windows of given length (Ex: 10,000 bp) using "def" function
# 3. Calculate GC content for each window using "def" function
# 4. Plot frequency histogram 

##### Arguments #####
# 1. Input file
# 2. Output plot file
# 3. Minimum length of scaffold
# 4. Length of window

# imports 
import sys
import os
import argparse
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
from pylab import savefig
from Bio import SeqIO
from Bio.SeqUtils import GC

#argparse 

def get_args():
	parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-i', '--input', type=str, help='Name of the data file with scaffolds. Must be fasta', required=True)
	parser.add_argument('-s', '--scaffold', type=int, help='Minimum scaffold size you want to work with ', default = 30000, required=True)
	parser.add_argument('-w', '--window', type=int, help='Range size of sliding window', default=10000, required=True)
	parser.add_argument('-v', '--overlap', type=int, help='Where you want to start next window', default=10000, required=True)
	parser.add_argument('-o', '--output', type=str, help='Output file, must add .png', required=True)
	args = parser.parse_args()
	INPUT = args.input 
	SCAFFOLD = args.scaffold 
	WINDOW = args.window  
	OVERLAP = args.overlap
	OUTPUT = args.output
	return INPUT, SCAFFOLD, WINDOW, OVERLAP, OUTPUT
INPUT, SCAFFOLD, WINDOW, OVERLAP, OUTPUT = get_args()		
			
#input arguments 

GCout = open('test.out', 'w') 
n = 1 

def sliding_window(INPUT, WINDOW, OVERLAP):
	for windowlength in range(0, WINDOW * OVERLAP, OVERLAP):
		yield INPUT[windowlength:windowlength+WINDOW]

#I really tried to write this script using islice but couldn't get it working - the reason I didn't finish this before my parents came in 
#for window in islice(combined-genomes.fa, 0, none, 10000): 
#		comp=GC(window)
#		GCout.write(comp)

for line in SeqIO.parse(INPUT, 'fasta'): 
	if len(line) > SCAFFOLD:
		for window in sliding_window(INPUT, WINDOW, OVERLAP): 
			comp=GC(window)
			GCout.write(str(n) + '\t' + str(comp) + '\n')
			n = n + 1
	else: 
			pass 
	
GCout.close()
#If I have to calculate GC content without a function 


#total = len(window)
#c = list.count("C")
#g = list.count("G")

#gc_total = g+c

#gc_content = gc_total/total			
			
#build histogram
df = pd.read_table('test.out')
print(df)
plt.hist(df)
plt.ylabel('GC Percentage')
plt.savefig('test.png')		
			
#example sequence 
#CCTCTTACCTTCCCCATATCAGCTATCTTCCCCAGAAATTATTCATGATACTCCAGTATGATAAAAGTATCCCTCTTTTGGAGGAAGTCAAATTTTAGCTAACAAATTAGAAGTTTATATTATGAAAGGACATTTTGACCTTATAGAAT
			
			
			
			
			
			
			
			
			
			
			
# 			
			
			
			
			
			
			

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			