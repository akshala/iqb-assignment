import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help = "input filename")
parser.add_argument("-o1", help = "output rna filename")
parser.add_argument("-o2", help = "output protein filename")
args = parser.parse_args()

input_file = args.i
output_rna_file = args.o1
output_protein_file = args.o2

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
description = dna[:i]
dna = dna[i+1:]

dna = dna.replace('\n', '')
print("DNA sequence: ", dna)

rna = dna.replace("T", "U")
rna_list = []
n = len(rna)
for i in range(0, n, 60):
	rna_list.append(rna[i:i+60])
rna_print = '\n'.join(rna_list)
print("corresponding RNA sequence: ", rna_print)

file = open(output_rna_file, 'w')
file.write(description+'\n')
file.write(rna_print)
file.close();

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

file = open(output_protein_file, 'w')
file.write(description+'\n')
file.write(protein)
file.close();