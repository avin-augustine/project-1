a=int(input("mark 1="))
b=int(input("mark 2="))
c=int(input("mark 3="))
total=a+b+c
print("total =",total)
average=total/3
print("average =",average)
if average<20:
    print("failed")
if average>20 and average<40:
    print("grade D")
if average>40 and average<60:
    print("grade C")
if average>60 and average<80:
    print("grade B")
if average>80 and average<100:
    print("grade A")