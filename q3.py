import matplotlib.pyplot as plt
import matplotlib.pylab as pl
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

print(ifile,ofile)


f = open(ifile,'r')

lines = f.readlines()

seq1 = ""
seq2 = ""

for l in lines:
	if l[0] == 'M':
		if seq1 == "":
			seq1 = l
		else:
			seq2 = l

# seq1 = input()
# seq2 = input()

n = len(seq1)
m = len(seq2)

mat = []

for i in range(n):
	mat.append([0]*m)

print(n,m)

for i in range(n):
	for j in range(m):
		mat[i][j] = int(seq1[i] == seq2[j])

# print("SIMILARITY MATRIX")
# for i in mat:
# 	print(i)
# print('\n\n')

#####################	Dotplot		##########################

Dotplot_seq1 = seq1[:-1]
Dotplot_seq2 = seq2[:-1]

mat2 = []
first_seq = [' ']
for c in Dotplot_seq2:
	first_seq.append(c)
mat2.append(first_seq)

n1 = len(Dotplot_seq1)
m1 = len(Dotplot_seq2)

for i in range(0,n1):
	row = []
	row.append(Dotplot_seq1[i])
	for j in range(0, m1):
		if(Dotplot_seq1[i] == Dotplot_seq2[j]):
			row.append('O')
		else:
			row.append(' ')
	mat2.append(row)
	# print(len(row))


pl.figure(figsize = (8,8))
tb = pl.table(cellText=mat2, loc=(0,0), cellLoc='center')

tc = tb.properties()['child_artists']
for cell in tc: 
    cell.set_height(1/m1)
    cell.set_width(1/n1)
print("Saving Dotplot.....")
pl.savefig("Dotplot_accurate.jpg")


X = []
Y = []
for i in range(len(mat)):
	for j in range(len(mat[i])):
		if(mat[i][j] == 1):
			X.append(j)
			Y.append((-1)*i)

fig = plt.figure(figsize=(8, 6))
subplot = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
subplot.set_xlabel(seq2)
subplot.set_ylabel(seq1[::-1])
subplot.plot(X,Y,'ro')
# plt.show()
plt.savefig("Dotplot_clear.jpg", orientation = "landscape")






for i in range(n-2,-1,-1):
	for j in range(m-2,-1,-1):
		row = [mat[i+1][k] for k in range(j+1,m)]
		col = [mat[k][j+1] for k in range(i+1,n)]
		mat[i][j] += max(max(row,col))



# print("SUM MATRIX")
# for i in mat:
# 	print(i)


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
	# print(x+1,y+1,mat[x][y])
	# print(a,b)
	i = x+1
	j = y+1

a += seq1[i:n]
b += seq2[j:m]
fig2 = pl.figure(figsize = (10,10))
tb1 = pl.table(cellText=mat, loc=(0,0), cellLoc='center')

tc1 = tb1.properties()['child_artists']
for cell in tc1: 
    cell.set_height(1/m)
    cell.set_width(1/n)

print(a)
print(b)

f.close()

f = open(ofile,'w')

f.write(a+'\n')
f.write(b+'\n')

# fig1.show()
print("Saving sum matrix.....")
pl.savefig("Sum_matrix.jpg")