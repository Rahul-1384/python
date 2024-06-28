# import calendar
# june_month=list(calendar.month(2023,6))
# print(june_month)
# print(june_month[46])
# from datetime import datetime
# d=datetime.now()
# dt=d.strftime("%d-%m-%Y")
# print(dt)

# import datetime
# d=datetime.date(2023,6,29)
# print(d)

# import calendar
# year=int(input("enter the current year: "))
# month=int(input("enter the current month: "))
# current_month_days=calendar.monthrange(year,month)
# print("weeks and days in current month: \n",current_month_days)

# import calendar
# m=list(calendar.monthrange(2023,6))
# print(m)
# print(m[1])
# for i in m:
#     if(m[0]==30):
#         print("hello")
#     elif(m[0]==3):
#         print("Hit Suuiiii")
#         break

# import datetime
# data1 = datetime.datetime.now()
# data2 = datetime.datetime.now()

# diff = data2 - data1

# days, seconds = diff.days, diff.seconds
# hours = days * 24 + seconds // 3600
# minutes = (seconds % 3600) // 60
# seconds = seconds % 60

# print(hours,minutes,seconds)

# from datetime import datetime, timedelta
# days_left=7
# dt = datetime.now()
# td = timedelta(days=days_left)
# # your calculated date
# my_date = dt + td
# print(my_date)
# print(td)
# import datetime
# then=datetime.time(11,59,59,999999)
# print(then)

# print(0o12)     #octal
# print(0b0010)   #binary
# print(0xAB)     #hexadecimal

# a=7
# b=0o12
# print(float(a))
# print(float(b))

# a=2+3j
# print(type(a))
# print(a)

# a,b=1,2
# print(a,b)

# print("the flight attendant asked,\"may i see your boarding pass\" ")
# print("hello rahul rajput \rworld")
# print("hello \frahul rajput")
# print('f\ne\nd\nc\nb\na')
# print("hello",end=" ")
# print("rahul rajput")

a=7
b=2
print(a,b)
a,b=b,a
print(a,b) 