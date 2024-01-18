'''#area of triangle
b=5
h=6
area=b*h/2
print("the area is:",area)

#using function method

def area():
    b=5
    h=6
    area=b*h/2
    print("the area is = ",area)
area()

#factorail 
print("factorial")
num=int(input("enter the number"))
a=1
fact=1
while (num>=a):
    fact=fact*a
    a+=1
print(fact)'''

#using function method
def fact():
    num=int(input("enter the number"))
    a=1
    fact=1
    while (num>=a):
         fact=fact*a
         a+=1
    print(fact)
fact()







