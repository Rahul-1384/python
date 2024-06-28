#division operator "/"
a=6
b=5             #it returns floating point no(s).
print(a/b)      #it also returns the decimal value after decimal point.


#floor division operator "//"
a=6
b=5             #it returns integer.
print(a//b)     #it ignores the value after decimal point.

a=eval(input("enter the value of a: "))
for i in range(1,11,1):
    print("%s * %s = %s"%(a,i,(a*i)))


import math
a=eval(input("enter the value: "))
b=eval(input("enter the value: "))
c=eval(input("enter the value: "))
result = (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)
print(result)

import math
print(math.sqrt(5))
print(4.6//15)