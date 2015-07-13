
searchString = "X-DSPAM-Confidence"

fhandle = open("mbox-short.txt")
for line in fhandle:

	if searchString in line:
		#print line;
		colonAt = line.find(":")
		confidenceValueString = line[colonAt + 1:].strip()

		print confidenceValueString

		try:
			confidenceValue = float(confidenceValueString)
		except:
			print confidenceValueString + " is not a number!"

