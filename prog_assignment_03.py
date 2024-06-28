#1
year=eval(input("enter the year: "))
if year%4==0 or year%400==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")

#2
hours=eval(input("enter the hours: "))
if hours==1:
    print("Internet browsing bill= ",20,end="$\n")
elif hours==0.5:
    print("Internet browsing bill= ",10,end="$\n")
else:
    print("Internet browsing bill= ",100,end="$\n")

#3
temp=(input("etner the temperature: "))
humidity=(input("etner the humidity: "))
 
if temp=="warm":
    if humidity== "dry":
        print("play basketball")
    if humidity=="humid":
        print("play tennis")
if temp=="cold":
    if humidity=="dry":
        print("play football")
    if humidity=="humid":
        print("swim")


#4
num=eval(input("enter the number: "))

if num%10==5:
    num**=2
    print(num)

#5
age=eval(input("etner the age: "))
if age!=15 and age!=16 and age!=17 and age!=18:
    print("student can't enroll")
else:
    print("student can enroll")