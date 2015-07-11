total = 0
count = 0

while True:

	try:
		input = raw_input("Enter a number:")
		if input == "done":
			print "Total: ", total
			print "Count: ", count

			# in case of div by 0
			if count > 0:
				print "Average: ", float(total) / float(count)
			else:
				print "Average: ", float(total)

			break

		number = float(input)

		total = total + number;
		count = count + 1;

	except:
		print "Invalid input"
