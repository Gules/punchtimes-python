## time clock ##
# In/Out Low Value		In/Out High Value		Rounded Value		Hours						
# :0		:7		:00		0.00
# :8		:22		:15		0.25
# :23		:37		:30		0.50
# :38		:53		:45		0.75
# :54		:59		:60		1.00

def main():
        week= []
	workweek=["Monday","Tuesday","Wendsday","Thursday","Friday"]
	#get all the hours for the week and put them in a list called week
	for (day in workweek)
		i=raw_input(day+" in:")
		o=raw_input(day+" out:")
		week.append(i)
		week.append(o)
