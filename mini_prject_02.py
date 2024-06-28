month=eval(input("enter the month number: "))
if month==2:
    year=eval(input("enter the year: "))
    if year%4==0 or year%400==0 and year%100!=0:
        print("the no of days are 29")
    else:
        print("the no of days are 28")
elif month in (1,3,5,7,8,10,12):
    print("the no of days are 31")
elif month in (4,6,9,11):
    print("the no of days are 30")
