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


file = open(ifile)
file_out = open(ofile,"w+")
for row in file:
	indT = row.find("TITLE")
	indH = row.find("HEADER")
	indRs = row.find("RESOLUTION")
	if(indT > -1 ):
		file_out.write(row)
		print(row)
	if(indH > -1):
		file_out.write(row)
		print(row)
	if(indRs > -1 and row.find("RANGE") == -1 and row.find("SHELL") == -1):
		file_out.write(row[11:])
		print(row[11:])