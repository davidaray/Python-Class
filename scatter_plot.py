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
	parser = argparse.ArgumentParser(description="This script is meant to create a colored scatter plot with regression. Please be conscious of which columns you'd like on what axis and refer to --help to see command options!", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-i', '--input', type=str, help='Name of the data file required for plotting, must be .txt file', required=True)
	parser.add_argument('-c', '--color', type=str, help='Input nothing, or Set1-3', required=False)
	parser.add_argument('-l', '--location', type=str, help='Location of your legend. Options are: best, upper left/right, lower left/right, right, center left/right, lower/upper center, and center', default="False", required=False)
	parser.add_argument('-d', '--dpi', type=int, help='Size of output file', default=100, required=False)
	parser.add_argument('-x', '--xaxis', type=int, help='Choose column to be x-axis', default=2, required=False)	
	parser.add_argument('-y', '--yaxis', type=int, help='Choose column to be y-axis', default=1, required=False)
	parser.add_argument('-u', '--hue', type=int, help='Choose column to be hue i.e. legend outside of figure', default=0, required=False)	
	parser.add_argument('-g', '--legend', type=int, help='Choose column to be legend i.e. hue but when you wanna change the location', default=0, required=False)
	parser.add_argument('-o', '--output', type=str, help='Output file', required=True)
	args = parser.parse_args()
	INPUT = args.input 
	COLOR = args.color 
	LOC = args.location 
	DPI = args.dpi
	OUTPUT = args.output
	XAXIS = args.xaxis
	YAXIS = args.yaxis
	HUE = args.hue
	LEG = args.legend
	
	return INPUT, COLOR, LOC, DPI, XAXIS, YAXIS, HUE, LEG, OUTPUT
INPUT, COLOR, LOC, DPI, XAXIS, YAXIS, HUE, LEG, OUTPUT = get_args()

PICTURE=OUTPUT + ".png" #sets up output name with .png file output 
#import data to pandas

df = pd.read_table(INPUT)	

#make dataset in pandas
#INPUT = [['Agraulis vanillae', 'Dryas iulia', 'Eueides tales', 'Heliconius beskei', 'Heliconius burneyi', 'Heliconius cydno', 'Heliconius demeter', 'Heliconius elevatus', 'Heliconius hecale', 'Heliconius hecalesia', 'Heliconius himera', 'Heliconius melpomene', 'Heliconius numata', 'Heliconius padalinus', 'Heliconius sara', 'Heliconius telesiphe', 'Heliconius timareta', 'Heliconius (Laparus) doris'],[21.4, 21.9, 32.6, 64.8, 106.3, 51.5, 68, 30.1, 36.5, 68.9, 48.7, 194.3, 61.3, 33.4, 43.4, 42.7, 37, 46.8], [391, 567, 539, 300, 382, 321, 367, 444, 351, 381, 400, 274, 349, 400, 340, 464, 253, 405]]
#df = pd.DataFrame(data=INPUT)

#Convert input columns to variables to use in the arguments for linear regression plot 
hue=df.columns[HUE]

y=df.columns[YAXIS]

x=df.columns[XAXIS]

leg=df.columns[LEG]


####Seaborn scatter plot###

#If else statement!!! Basically, the above commands ALWAYS leave a legend outside the figure. So, in order to prevent 2 legends from being generated if you want the legend in a different location, I made this step so that anytime you want to specify the location ("LOC"), it defaults to the lower commands

if LOC == "False":

	sp = sb.lmplot(x=x, y=y, data=df, row_order=True, hue=hue, fit_reg=False, palette=COLOR, sharex=False, sharey=False) #sp stands for scatter plot. Aside from x, y, and data, the other commands are for...
#row_order keeps it in the order of rows. Can also go by order of hues or columns
#hues means you can create a different color for different data. Choose a column that distinguishes between different data types and it will form a legend outside the figure  
#fit_reg gets rid of linear regression lines, as since hue includes different colors, there'd be a regression line for each data point, which we don't want 
#palette means different color schemes. There's a default, then Set1-3

else: 
		sp = sb.lmplot(x=x, y=y, data=df, hue=leg, row_order=True, fit_reg=False, palette=COLOR, legend_out=True, legend=False, sharex=False, sharey=False) #legend_out and legend=false prevent the hue from appearing aside the figure 
		sp.despine(left=True)
		plt.legend(loc=LOC) 
		
sns.regplot(x=x, y=y, data=df, scatter=False, ax=sp.axes[0,0]) #uses regplot, brings back a regression line we left out in lmplot. Don't get the last bit so don't ask  
 
#ax[0].set_ylim(,500)) #controls range of y-axis, xlim will do the same for x-axis. Can't get to work, might not be available for lmplot 

sp.fig.suptitle('Construing the Associations of N50 and Genome Voluminosity') #adds a title

sp.savefig(PICTURE, dpi=DPI) #saves as an image and chooses size of the file 













