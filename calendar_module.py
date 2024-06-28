import time
import calendar
#calendar
months=calendar.calendar(2023)
print(months)
#current month access
year=int(input("enter the current year: "))
month=int(input("enter the current month: "))
current_month_days=list(calendar.monthrange(year,month))
print("weeks and days in current month: \n",current_month_days)

#birthday month access
bday_month=(calendar.month(2023,7))
print("birthday mont: \n",bday_month)
#bithdate access
import datetime
YYYY=int(input("enter current year: "))
MM=int(input("enter current month: "))
DD=int(input("enter current date: "))
curr_date=datetime.date(YYYY,MM,DD)
print("Current Date: ",curr_date)
#accessing upcoming birth date 
YYYY_01=int(input("enter upcoming birth year: "))
MM_01=int(input("enter upcoming birth month: "))
DD_01=int(input("enter previous date than upcoming birth date: "))
upcmng_birth_date=datetime.date(YYYY_01,MM_01,DD_01)
print("upcoming birth day: ",upcmng_birth_date)

YYYY_02=int(input("enter birth year: "))
MM_02=int(input("enter birth month: "))
DD_02=int(input("enter birth date: "))
birth_date=datetime.date(YYYY_02,MM_02,DD_02)
print("Birth Day: ",birth_date)
# Time access
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

# for days in current_month_days:
#     if(current_month_days[1]==30):
#         days_left = (30-DD) + DD_01
#         print("Days Left: ",(days_left-1))
#         break
#     elif(current_month_days[1]==31):
#         days_left = (31-DD) + DD_01
#         print("Days Left: ",(days_left-1))
#         break
#     elif(current_month_days[1]==29):
#         days_left = (29-DD) + DD_01
#         print("Days Left: ",(days_left-1))
#         break
days_left=upcmng_birth_date-curr_date
print(days_left," are left for someone special's birthday🎂🥳🤩")
