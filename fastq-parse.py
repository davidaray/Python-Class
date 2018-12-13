import Bio
from Bio import SeqIO 
import re 

#l = 1


#test to see if regex works 
for record in SeqIO.parse("cheat_example_fq.fastq", "fastq"):
	for c, value in enumerate(record.id, 1):
		replace = re.sub(r"(.+_([1-2]).*)", c + "\0", record.id)	
		print(replace)
	
	
#real script to change file directly 
#for record in SeqIO.parse("cheat_example_fq.fastq", "fastq"):
#	for c, value in enumerate(record.id, 1):
#		print(c, record.id)
#		re.sub(r"(.+_([1-2]).*)", c + "_" + r"\3", record.id)	
#		print(record.id)	
	
	
#Postulated line switching to get same number for different lines 
for record in SeqIO.parse("cheat_example_fq.fastq", "fastq"):
	if re.match("_2:", record.id) == True: 
		for c, value in enumerate(record.id, 1):
			print(c, record.id)
			re.sub(r"(.+_([1-2]).*)", c + "_" + 'OP:i:' + \1, record.id)
	else:
		for c, value in enumerate(record.id, 1):
			print(c, record.id)
			re.sub(r"(.+_([1-2]).*)", c + "_" + 'OP:i:' + \1, record.id)
	
		
	q.close()
	
#Tried to have each line written to a new file, but it didn't jibe with regex
	
#set regular expression 
#regex = r"((.*) [1-2](.*))"
#1 D00602:32:H3LN7BCXX:1:1101:1457:2096_2:N:0:1
#1 D00602:32:H3LN7BCXX:1:1101:1334:2126_1:N:0:1
#1 D00602:32:H3LN7BCXX:1:1101:1334:2126_2:N:0:1
#
#relax = re.sub(r"((.+)_[1-2](.+))", "record.id", "x")

