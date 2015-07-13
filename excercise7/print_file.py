
filename = raw_input("Enter a file name:")

try:
	fhandle = open(filename)
	for line in fhandle:
		print line.strip()
except:
	print "file " + filename + " is not found"


