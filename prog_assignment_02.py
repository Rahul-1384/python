#1
subjects=5
total=0
for i in range(subjects):
    a=eval(input("enter the marks of subject %sst: "%(i+1)))
    total+=a
    percentage = total/subjects
print("the aggregate and percentage of a student is: ",total,"and",percentage,end="%")

#2
num=eval(input("enter the four digit no: "))
sum=0
for i in range(4):
    ld=int(num%10)
    sum+=ld
    num/=10
print(sum)

#3
km=eval(input("distance b/w mathura and jhaansi is: "))
meter=1000*km
cm=100000*km
miles=0.6213*km
print("distance b/w mathura and jhaansi is: ",km,end=" km\n")
print("distance b/w mathura and jhaansi is: ",meter,end=" m\n")
print("distance b/w mathura and jhaansi is: ",cm,end=" cm\n")
print("distance b/w mathura and jhaansi is: ",miles,end=" miles")

#4
d=eval(input("enter the distance: "))
t=eval(input("enter the time: "))
print("the distaqnce is: ",d,end=" m\n")
print("the distaqnce is: ",t,end=" sec\n")
s=d/t
print("the speed is: ",s)