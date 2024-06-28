s="spam"

print(len(s))

print(s[0])

print(s[0:len(s)])

print(s[len(s)-1])

s[0] = "y"        #ERROR

s = 'y' + s[1:]   #ANOTHER WAY
print(s)

s = s[0:] + "y"   #ANOTHER WAY
print(s)

#We can change the string by converting it into the list
s="rahul rajput"
l=list(s)
print(l)
l[0] = "R"
print(l)
print("".join(l))

  
# bytearray()

arr = bytearray(b"real madrid")
print(arr)
print(arr.decode())


arr=bytearray(b"real madrid")
for values in arr:
    print((values))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

list=[1,2,3,4]
arr=bytearray(list)
print(len(arr))


arr = bytearray(b'rahul rajput')
print("count of a is: ",arr.count(b"a"))


arr = bytearray()
print(arr)
print(arr.decode())


# s.find()
s = "spam"
print(s.find("pa"))


#  s.replace(old,new)
s="spam"
print(s.replace("p","y"))


# s.split(",")
s="rahul,manish,cr7"
print(s.split(","))


# s.upper()
s="spam"
print(s.upper())


# s.isalpha() &&  s.isdigit()
s="rahulrajput"
print(s.isalpha())
print(s.isdigit())


# s.strip() 
s="   rahul rajput   "
print(s)
print(s.strip())   #to remove whitespaces

s="   rahul rajput   "
print(s.strip("   rahul"))   #to remove character(" rahul") from beginning or endof string

s=" geeks for geeks "
print(s.strip(" gesk"))


# string.rsplit(separator,maxsplit)
s="tic-tac-toe"
print(s.rsplit("-"))

s="rahul rajput cr7"
print(s.rsplit("c",1))

s="rahul@rajput@cr7"
print(s.rsplit("a",2))


# Easy to understand rsplit().

# splits the string at index 12
# i.e.: the last occurrence of g
word = 'geeks, for, geeks'
print(word.rsplit('g', 1))

# Splitting at '@' with maximum splitting
# as 1
word = 'geeks@for@geeks'
print(word.rsplit('@', 1))


s="rahul rajput    "
print(s.rstrip(" utp"))


# .format() 
s="i have {an:.2f} rupees"
print(s.format(an=7))


s="%s and %s both are good"%("rahul","manish")
print(s)

s="{0} and {1} both are good".format("rahul","manish")
print(s)

s="{} and {} both are good".format("manish","rahul")
print(s)

s="{:.2f} , {:+05d}".format(299.634,-42)
print(s)            #+05d----> makes the number of 5 digits


# *********Padding/Filling*********

#when strings are passed as the arguments
#the space is generated in the in the right.
print("{0} and {1} both are good ....".format("rahul","manish"))

#when numerics are passed as the arguments
#the space is generated in the left.
print("the jersey no {0:8} is unique".format(7))

# Other methods of padding.
print("the jersey no {0:*<8} is unique".format(7))  # < -: left alligned
print("the jersey no {0:*>8} is unique".format(7))  # > -: right alligned
print("the jersey no {0:*^8} is unique".format(7))  # ^ -: center padding



s="rahul rajput 7"
print(s.ljust(40))    # .ljust() -: left alligned

s="rahul rajput 7"
print(s.rjust(40))    # .rjust() -: right alligned 

s="rahul rajput 7"
print(s.center(40))    # .center() -: center padding



# ***Getting Help***
s="spam"
print(dir(s))      # it returns all the string methods in the form of list

# Example of a method of string of concatenation
s="rahul"
print(s + " rajput")      # simple cancatenation

s="rahul"
print(s.__add__(" rajput"))     # concatenation by string method 


s="rahul rajput"
help(s.replace)
help(print)

s="rahul rajput"
for i in s:
    print(i)


# String slicing
s="rahul"
print(s[-1:len(s)-3])

 