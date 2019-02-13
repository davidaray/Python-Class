1) #Just use the methods described in chapter 3 to create a random sequence file consisting of 60,000 bp. 

alphabet=['ATGC']
n = 60000
dna = [random.choice(alphabet) for i in range(int(n))]
dna = ''.join(dna)
print(dna)

#Then, count up the number of CG dinucleotides and ACGTC pentanucleotides in that file. 

#That will make it easier on them by allowing them to use the methods
#described in the chapter without having to learn anything completely foreign.


#INTERNET EXAMPLE 
#for i,k in zip(data[0::2], data[1::2]):
 #   print(str(i), '+', str(k), '=', str(i+k))

#First attempt 	
def count(dna, two, five):
	n = 0
	x = 0 
	for ik in zip(dna[0::1], dna[1::1]):
		print(ik)
		print(two)
		if ik == two: 
			n +=1
	for abcde in zip(dna[0::1], dna[1::1], dna[2::1], dna[3::1], dna[4::1]):
		#print(abcde)
		if abcde == five:
			x +=1
	return n 
	return x 

#tryna split up the function 		
def count2(dna, two):
	n = 0
	for ik in zip(dna[0::1], dna[1::1]):
		print(ik)
#		print(two)
#		print(ik == two)
		if ik == two:
			print(n)
			n +=1
	return n 

def count5(dna, five):
	x = 0 
	for abcde in zip(dna[0::1], dna[1::1], dna[2::1], dna[3::1], dna[4::1]):
		print(abcde)
#		if abcde == five:
#			x +=1
	return x 		
		
#Best effort. Also LEAVE SPACE BETWEEN NUCLEOTIDES!!!!		
def count(dna, two, five):
	n = 0
	x = 0 
	two = #something that converts list to tuple
	five = 
	for ik in zip(dna[0::1], dna[1::1]):
#		print(ik)
#		print([two])
		if [[ik]] == two:
			print(n)
			n +=1
	for abcde in zip(dna[0::1], dna[1::1], dna[2::1], dna[3::1], dna[4::1]):
#		print(abcde)
#		print([five])
		if abcde == five:
			print(x)
			x +=1
	return n 
	return x 
		
		
