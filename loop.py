'''count=0
while (count<9):
    print("the count is  =",count)
    count+=1
print("thank you")

#multiplication table
print("multiplication table")
num=int(input("enter the number"))
a=1
while (a<11):
    print(a,"*",num,"=",a*num)
    a=a+1
print("answer")

#factorial

print("factorial of the number")
num=int(input("enter the number"))
if num<0:
    print("fact is not found")
elif num==0 or num==1:
    print("fact is 1")
else:
    fact=1
    i=1
    while i<=num:
        fact=i*fact
        i+=1
        print("the fact value is =",fact)'''

#print all numbers from 0 to 6 except 3
a=0
while (a<7):
    a+=1
    if (a==3):
        continue
        print (a)
        








