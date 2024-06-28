# abs() ---> returns absolute value.
print(abs(6),abs(-5))

# max() ---> returns largest number.
print(max(6,5))

# min() ---> returns the minimum value.
print(min(6,5))

# pow() ---> returns the X to the power Y.
print(pow(2,4))

# round() ---> returns an integer nearest to the value of a.
print(round(6.5))

import math as y

# ceil() ---> round X to next nearest integer and returns that integer.
print(y.ceil(6.5))

# floor() ---> round X to previous nearest integer and returns that integer.
print(y.floor(6.5))

# exp() ---> returns the exponential value for e to the power X
print(y.exp(1))

# log() ---> returns the value of log X.
# returns floating point no.
print(y.log(1))

# sqrt() ---> returns the square root.
# returns floating point no.
print(y.sqrt(9))

#program to calculate hypotenuse.
import math
base=eval(input("enter the base of the triangle: "))
height=eval(input("enter the height : "))
hyp=math.sqrt((pow(base,2)) + pow(height,2))
print("the hypotenuse is: ",hyp)