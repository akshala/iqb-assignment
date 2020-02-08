import sys 
input_file = '/home/akshala/Documents/IIITD/fourthSem/IQB/assignment1/Group25/DNA.fa'    #sys.argv[0]
output_file = '/home/akshala/Documents/IIITD/fourthSem/IQB/assignment1/Group25/question1_ouput.fa'    #sys.argv[1]
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

dna_to_protein = {
	'TTT':'F', 'TTC':'F', 'TTA':'L','TTG':'L',
	'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
	'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',
	'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
	'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
	'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
	'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
	'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
	'TAT':'Y', 'TAC':'Y', 'TAA':'-', 'TAG':'-', 
	'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
	'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 
	'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'A',
	'TGT':'C', 'TGC':'C', 'TGA':'-', 'TGG':'W',
	'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
	'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
	'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
	}

protein = ''
for i in range(0,length,3):
	if(dna[i:i+3] == ''):
		break
	protein += dna_to_protein[dna[i:i+3]]
print("corresponding Protein sequence: ", protein)

file = open(output_file, 'w')
file.write(protein)
file.close();