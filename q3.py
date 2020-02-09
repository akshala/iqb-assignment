import sys, getopt

ifile = ""
ofile = ""

try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
	print('test.py -i <inputfile> -o <outputfile>')
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print('test.py -i <inputfile> -o <outputfile>')
		sys.exit()
	elif opt in ("-i", "--ifile"):
		ifile = arg
	elif opt in ("-o", "--ofile"):
		ofile = arg


f = open(ifile,'r')

lines = f.readlines()

seq1 = ""
seq2 = ""

for l in lines:
	if l[0] == 'M':
		if seq1 == "":
			seq1 = l[:-1]
		else:
			seq2 = l[:-1]

# seq1 = input()
# seq2 = input()

n = len(seq1)
m = len(seq2)

print(n,m)

mat = []

for i in range(n):
	mat.append([0]*m)

f.close()


#Similarity matrix generation

for i in range(n):
	for j in range(m):
		mat[i][j] = int(seq1[i] == seq2[j])

f = open("Similarity_Matrix.txt",'w')

s = [i for i in seq2]
f.write("  "+" ".join(s)+'\n')
c=0
for i in mat:
	s = seq1[c]+" "+' '.join([str(k) for k in i])
	f.write(s+'\n')
	c+=1

f.close()

#Sum Matrix Generation

for i in range(n-2,-1,-1):
	for j in range(m-2,-1,-1):
		row = [mat[i+1][k] for k in range(j+1,m)]
		col = [mat[k][j+1] for k in range(i+1,n)]
		mat[i][j] += max(max(row,col))

f = open("Sum_Matrix.txt",'w') # Open file in submlime text for clear view

s = [i for i in seq2]
f.write("  "+"  ".join(s)+'\n')
c=0
for i in mat:
	j = ["0"*(2-len(str(k)))+str(k) for k in i]
	s = seq1[c]+" "+' '.join(j)
	f.write(s+'\n')
	c+=1

f.close()

#Traceback

a = ""
b = ""

i=0
j=0

while i < n and j < m:
	x = i
	y = j
	currmax = mat[i][j]
	row = [mat[i][k] for k in range(j+1,m)]
	col = [mat[k][j] for k in range(i+1,n)]
	maxinrow = j+1
	if len(row) > 0:
		maxinrow += row.index(max(row)) 
		if max(row) > currmax:
			currmax = max(row)
			y = maxinrow
	maxincol = i+1
	if len(col) > 0:
		maxincol += col.index(max(col))
		if max(col) > currmax:
			x = maxincol
			y = j

	a += "_"*(y-j) + seq1[i:x] + seq1[x]
	b += "_"*(x-i) + seq2[j:y] + seq2[y]
	i = x+1
	j = y+1

a += seq1[i:n]
b += seq2[j:m]

print(a)
print(b)

f = open(ofile,'w')

f.write(a+'\n')
f.write(b+'\n')

f.close()

