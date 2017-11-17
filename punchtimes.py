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
    for x in week:
        pass
    print (week)
    
    print(convert_to_mil_time("7:42a"))
def convert_to_mil_time(time_to_convert):
    converted = time_to_convert.replace(":","")
    length_of_time=len(converted)
    #convert standard time to military time, add 1200 to any time from 1:00pm to 11:00pm
    if converted[length_of_time-1:] =="a":
        print("if a")
        converted=converted.zfill(length_of_time+1)
        converted=converted[:4]
    elif int(converted[:2]) > 12:
        converted=str(int(converted[:2])-2)+converted[2:]
    converted = converted.zfill(4)
    return converted
def round_to_15(num):
    pass
    
main()
