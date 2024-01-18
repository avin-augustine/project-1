'''#parameters in python
#default,keyword,reference,arbitary,keyarbitory parameterpassing
#default

def sum(a,b):
    c=a+b

#reference parameter passing
def square(mylist):
    sq=[]
    for x in mylist:
        sq.append(x**2)
        return sq

li=[3,5,6] #reference 
result=square(li)
print("square of the list = ",result())

#find the number of vowels in a list

lest=['a','b','c','d','e','f','g','h','i']
print(lest)
a=0
for i in lest:
    if a==('a','e','i'):
      print("it is vowels")
    else:
      print("it is not vowels")'''

#using function
'''def count():
    newlist=['a','c','i','h','o','x','z']
    vowels=['a','e','i','o','u']
    c=0

    for a in newlist:
        for b in vowels:
             if a == b:
                 c+=1
    print("number of vowels",c)
        
count()'''

newlist=['a','c','i','h','o','x','z']
vowels = ['a','e','i','o','u']
def vowels(x):
    c=0
    for i in x:
        if(i in x):
            c+=1
    print(c)
vowels(newlist)


#find the greater of three number

lest=[4,8,2]
print("the largest among three")
def large(l):
    a=0
    for i in l:
        if (i>a):
            a=i
            print("the largest is ",a)
large(lest)




