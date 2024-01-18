#simple calculater
'''num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
sum=num1+num2
difference=num1-num2
multiply=num1*num2
division=num1/num2
print("sum =",sum)
difference("difference =",difference)
print("multiply =",multiply)
print("division =",division)

count=0
while (count<9):
    print("the count is =",count)
    count+=1
print("result")

print("multiplication table")
num=int(input("enter the number"))
n=1
while (n<11):
    print(n,"*",num,"=",n*num)
    n+=1
print("result")'''

'''print("factorial")
num=int(input("enter the number"))
a=1
fact=1
while (num>=a):
    fact=fact*a
    a+=1
print(fact)'''


def myfunction(*formal):
	print(type(formal))
	s=0
	for x in formal:
		s=s+x
	print("Sum is ",s)
myfunction(10,20)
myfunction(10,20,30,40,50)
myfunction(10.2,15.5,26.3)

    

   









