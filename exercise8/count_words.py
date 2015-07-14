
fhandle = open("words.txt")
fileContent = fhandle.read()

words = fileContent.split()


dict = dict()
for word in words:
	dict[word] = dict.get(word, 0) + 1;

print dict

largestKey = None
largestValue = None

for key,value in dict.items():
	if (largestKey == None) or (value > largestValue):
		largestKey = key
		largestValue = value

print "LargestKey=" + str(largestKey), ",LargestValue=" + str(largestValue) 
