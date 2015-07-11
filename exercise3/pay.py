baseNumHour = 40.0
otRatePercentage = 1.5

hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")

try:
	hoursFloat = float(hours)
except:
	print("hours entered is not a number");
	exit();


try:
	rateFloat = float(rate)
except:
	print("rate entered is not a number");
	exit();

if (hoursFloat > baseNumHour):
	otHours = hoursFloat - baseNumHour;
	pay = (baseNumHour * rateFloat) + (otHours * rateFloat * otRatePercentage)
else:
	pay = hoursFloat  * rateFloat

print "Pay is: " + str(pay);
