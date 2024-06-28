# if statement.
a=eval(input("enter the value: "))
b=eval(input("enter the value: "))
if a==b:
    print("Equals")

r=eval(input("enter the radius: "))
if r>0:
    pi=3.14
    area=pi*r*r
    circum=2*pi*r
    print(area,circum)

#if else statement.
a=eval(input("enter the value: "))
b=eval(input("enter the value: "))
if a>b:print("%s is greater"%a)
else:print("%s is greater"%b)


a=eval(input("enter the value: "))
if a%5==0 and a%10==0:
    print("number is divisible by both")
if a%5==0 or a%10==0:
        print("number is divisible")


#nested if.
a=eval(input("enter hte value: "))
b=eval(input("enter hte value: "))
c=eval(input("enter hte value: "))

# if a>b and a>c:
#     print("%s is greater"%a)
# elif b>a and b>c:

#     print("%s is greater"%b)
# else:
#      if c>a and c>b:
#         print("%s is greater"%c)
if a>b and a>c:
    print("%s is greater"%a)
    if b>c:
        print("then %s"%b)
        print("then %s"%c)
if b>a and b>c:
    print("%s is greater"%b)
    if a>c:
        print("then %s"%a)
        print("then %s"%c)
if c>a and c>b:
    print("%s is greater"%c)
    if b>a:
        print("then %s"%b)
        print("then %s"%a)





    
     