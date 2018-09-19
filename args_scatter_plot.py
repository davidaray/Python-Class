#from Bio import SeqIO
import os 
import sys
import pandas as pd
import matplotlib.pyplot as plt 
from pylab import savefig 
plt.switch_backend('Agg')
import seaborn as sb
import seaborn as sns 
import argparse
#
def get_args():
	parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-i', '--input', type=str, help='Name of the data file required for plotting', required=True)
	parser.add_argument('-c', '--color', type=str, help='Input nothing, or Set1-3', required=False)
	parser.add_argument('-d', '--dpi', type=int, help='Size of output file', default=100, required=False)
	parser.add_argument('-o', '--output', type=str, help='Output file, must add .png', required=True)
	args = parser.parse_args()
	INPUT = args.input 
	COLOR = args.color 
	DPI = args.dpi  
	OUTPUT = args.output
	return INPUT, COLOR, DPI, OUTPUT
INPUT, COLOR, DPI, OUTPUT = get_args()

#PICTURE= OUTPUT + ".png"
#import data to pandas

df = pd.read_table(INPUT)	

#make dataset in pandas
#INPUT = [['Agraulis vanillae', 'Dryas iulia', 'Eueides tales', 'Heliconius beskei', 'Heliconius burneyi', 'Heliconius cydno', 'Heliconius demeter', 'Heliconius elevatus', 'Heliconius hecale', 'Heliconius hecalesia', 'Heliconius himera', 'Heliconius melpomene', 'Heliconius numata', 'Heliconius padalinus', 'Heliconius sara', 'Heliconius telesiphe', 'Heliconius timareta', 'Heliconius (Laparus) doris'],[21.4, 21.9, 32.6, 64.8, 106.3, 51.5, 68, 30.1, 36.5, 68.9, 48.7, 194.3, 61.3, 33.4, 43.4, 42.7, 37, 46.8], [391, 567, 539, 300, 382, 321, 367, 444, 351, 381, 400, 274, 349, 400, 340, 464, 253, 405]]
#df = pd.DataFrame(data=INPUT)

col1=df.columns[0]
#col1 = str(col1)
#type(col1) is str
#print(col1)
col2=df.columns[1]
#col2 = str(col2)
col3=df.columns[2]
#col3= str(col3)



#Seaborn scatter plot 

sp = sb.lmplot(x=col3, y=col2, data=df, row_order=True, hue=col1, fit_reg=False, palette=COLOR)
sns.regplot(x=col3, y=col2, data=df, scatter=False, ax=sp.axes[0,0])
sp.fig.suptitle('Construing the Associations of N50 and Genome Voluminosity')
sp.savefig(OUTPUT, dpi=DPI)

















