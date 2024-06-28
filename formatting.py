#syntax   format(item, fromat-specifier)
a=7.123456
b=format(a,".2f")
print(b)

#format() in print statement
#floating pint numbers formatting
a=7.12345
print("the value of a is:",format(a,"<10.2f"),"hello world")    #left justify
print("the value of a is:",format(a,"10.2f"),"hello world")     #right justify

                #OR

a=7.12345
print("the value of a is:",format(a,"<10.2f"),"hello world")    #left justify
print("the value of a is:",format(a,"10.2f"),"hello world")     #right justify


#area of circle
r=eval(input("enter the value: "))
pi=3.1428
area=pi*(r**2)
print("the are of cirlce is: ",format(area,".2f"))


#integer formatting
a=1234
#10x ---> converts into hexadecimal
print("the value of a is:",format(a,"<10x"),"hello world")    #left justify
print("the value of a is:",format(a,">10x"),"hello world")     #right justify

a=1234
print("the value of a is:",format(a,"<10d"),"hello world")    #left justify
print("the value of a is:",format(a,"10d"),"hello world")     #right justify

#string formating
a="hello "
print("the value of a is:",format(a,"20s"),"hello world")    #left justify
print("the value of a is:",format(a,">20s"),"hello world")   #right justify


#formatting as a percentage
a=0.8335
print("the avalue of a is: ",format(a,"<10.2%"),"hello 7")   #left justify
print("the avalue of a is: ",format(a,"10.2%"),"hello 7")    #right justify

