import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help = "input filename")
parser.add_argument("-o", help = "output filename")
args = parser.parse_args()

input_file = args.i
output_file = args.o
# print(input_file, output_file)

file = open(input_file,'r')
dna = file.read()
# print(dna)

length = len(dna)
delete_till = 0;
for i in range(length):
	if dna[i] == '\n':
		delete_till = i
		break
dna = dna[i+1:]

dna = dna.replace('\n', '')
print("DNA sequence: ", dna)

rna = dna.replace("T", "U")
print("corresponding RNA sequence: ", rna)

rna_to_protein = {
	'UUU':'F', 'UUC':'F', 'UUA':'L','UUG':'L',
	'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
	'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
	'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
	'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
	'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
	'ACU':'U', 'ACC':'U', 'ACA':'U', 'ACG':'U',
	'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
	'UAU':'Y', 'UAC':'Y', 'UAA':'-', 'UAG':'-', 
	'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
	'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 
	'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'A',
	'UGU':'C', 'UGC':'C', 'UGA':'-', 'UGG':'W',
	'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
	'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
	'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
	}

protein = ''
flag = 0
for i in range(0,length,3):
	if(rna[i:i+3] == ''):
		break
	# print('codon: ', rna[i:i+3])
	if(rna[i:i+3] == 'AUG'):
		flag = 1;
		# print("start codon")
	if(rna[i:i+3] == 'UAA' or rna[i:i+3] == 'UAG' or rna[i:i+3] == 'UGA'):
		# print("stop codon")
		flag = 0
	if flag:
		protein += rna_to_protein[rna[i:i+3]]	
print("corresponding Protein sequence: ", protein)

file = open(output_file, 'w')
file.write(protein)
file.close();