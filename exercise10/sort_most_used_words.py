
fhandle = open("words.txt")
wordsString = fhandle.read()

words = wordsString.split()

dict = dict()
for word in words:
	dict[word] = dict.get(word, 0) + 1

# put the key,value to value,key as a tuple
# for sorting
valueKeyList = list()
for (key, value) in dict.items():
	valueKeyList.append((value, key))

valueKeyList.sort(reverse=True)
print valueKeyList[:10]
