# Good Service Tax (GST) Calculator.

COP=eval(input("etner the cost of production: "))
CGST=eval(input("enter CGST rate: "))
SGST=eval(input("enter SGST rate: "))
print("the cost of production is: ",COP)
print("the central GST is: ",CGST,end="%\n")
print("the state GST is: ",SGST,end="%\n")
TCOP=COP + (CGST/100)*COP + (SGST/100)*COP
print("Total Cost Of Production Is: ",TCOP)

