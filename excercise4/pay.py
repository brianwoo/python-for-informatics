
################################
#
# Compute Pay by hours and rate
#
################################
def computePay(hours, rate):

	baseNumHour = 40.0
	otRatePercentage = 1.5


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


	return pay;




hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")

pay = computePay(hours, rate)

print "Pay is: " + str(pay);
