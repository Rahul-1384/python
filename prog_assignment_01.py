#1
print("f\ne\nd\nc\nb\na")

#2
city_1=input("enter the city name: ")
city_2=input("enter the city name: ")
city_3=input("enter the city name: ")
print(city_1,",",city_2,",",city_3)

#3
name=(input("enter your name: "))
address=(input("enter your address: "))
mob_no=eval(input("enter your mobile number: "))
print(name,"\n",mob_no,"\n",address)

#4
print("A,",end="")
print("B,",end="")
print("C,",end="")
print("D,",end="")
print("E,",end="")
print("F")

#5
a=input("enter the value of a: ")
print(type(a))
a=int(a)
print(type(a))

#6
str1="hello world"
a=str1.upper()
print(a)

#7
Pounds=10
Kilogram = Pounds*0.45
print("the value of pounds is: ",Pounds)
print("the value of kilogram is: ",Kilogram)

#8
r=eval(input("enter the radius: "))
print("radius: ",r)
pi=3.14
print("are of a circle is: ",(pi*(r**2)))

a=1234
p=a%10  #4
l=a//10#123
q=l%10#3
m=l//10#12
r=m%10#2
n=m//10#1
s=n%10#1

print(a    ,p,q,r,s)
