import time
curr_time=time.ctime()
print("Current Time in pattern(day,mon,date,time,year): ",curr_time)

full_time=time.strftime("%H:%M:%S")
print("Current Time in pattern (hours,minutes,seconds): ",full_time)
#hours
hrs_time=int(time.strftime('%H'))
print("Hours : %s hrs"%(hrs_time))
#minutes
min_time=int(time.strftime("%M"))
print("Minutes : %s min"%(min_time))
#seconds
sec_time=int(time.strftime("%S"))
print("Seconds : %s sec"%(sec_time))
