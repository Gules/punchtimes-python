## time clock ##
# In/Out Low Value		In/Out High Value		Rounded Value		Hours						
# :0		:7		:00		0.00
# :8		:22		:15		0.25
# :23		:37		:30		0.50
# :38		:53		:45		0.75
# :54		:59		:60		1.00

def main():
    week=[]
    workweek=["Monday","Tuesday","Wendsday","Thursday","Friday"]
    #get all the hours for the week and put them in a list called week
    print ("put time in military or with an a or p at end ex: 07:00 or 7:00a")
    for day in workweek:
        time_in=input(day+" in:")
        if day=="Friday":
            week.append(time_in)
            continue
        else:
            time_out=input(day+" out:")
        week.append(time_in)
        week.append(time_out)
    print (week)
def convert_to_mil_time(time_to_convert):
    pass
def round_to_15(num):
    pass
    
main()
