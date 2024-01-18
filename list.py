'''newlist=[3,5,7,9,2,8,4,7]
print(newlist)
print(newlist[0])
print(len(newlist))
newlist[0]=1
print(newlist)
newlist.reverse()
print(newlist)
newlist.append(10)
print(newlist)
a=0
max=0
for a in newlist:
    if a>max:
        max=a
    else:
        a+=1
print(max)
r=int(input("index of element = "))
print(newlist.index(r))
x=int(input("enter the element to count = "))
print(newlist.count(x))
#nestedlist
latestlist=[8,5,3,5,[7,9,1,3]]
print(latestlist)
print(latestlist[4][3])
print(latestlist[4][2])
fruit=["apple","banana","coco","coconut","mango"]
print(fruit)

#string
print(dir(list))'''
#interchange first and last elements in a list
sublist=["football","cricket","basketball",6,7,9]
'''print(sublist)
a=sublist[-1]
b=sublist[0]
sublist[0]=a
sublist[-1]=b
print("the result =",sublist)'''
#swap to elements in a list
'''sublist=[3,7,9,5,4]
print(sublist)
sublist[0],sublist[-1]=sublist[-1],sublist[0]
print("swaped list = ",sublist)
#swap elements in a string list'''
#ways to find the length of  a list
'''mylist=["heloo","haii",8,3,"welcome"]
print(mylist)
print(len(mylist))'''
#maximum of two numbers in python
'''newlist=[5,9]
print(newlist)
a=newlist[0]
print(a)
b=newlist[-1]
print(b)
if a>b:
    print("a is largest in newlist")
else:
    print("b is largest in newlist")'''
#minimum of two numbers in python
'''lest=[8,7]
c=lest[0]
d=lest[-1]
print("C = ",c)
print("d = ",d)
if c>d:
    print("d is the smallest")
else:
    print("c is the smallest")'''
#ways to check if an element exists in a list,check if 6 exists or not
'''lest=[1,4,6,8,9]
a=9
temp=0
for i in lest:
    if a==i:
        temp=1
if temp==1:
    print("exist")
else:
    print("not exist")'''
#ways to clear a list in python
'''lest=[8,9,"heloo","wlecome",9]
print(lest)
lest.clear()
print(lest)'''
#reversing a list in python
'''lest=[4,5,6,7,23]
lest.reverse()
print(lest)'''
#cloning or copying of list in python
'''lest=[6,7,4,1,8,10]
print(lest)
lest.copy()
print(lest)'''
#count occurences of an element in a list
'''lest=[6,2,6,7,8,9,6,7]
print(lest)
num=int(input("enter the number ="))
count=0
for i in lest:
    if i==num:
        print("number occured")
    else:
        i+=1'''
##Python Program to find sum and average of List in Python

'''list=[1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
print(list)
sum=0
i=0
while i<len(list):
    sum+=list[i]
    i+=1
print("sum of list=",sum)
avg=sum/len(list)
print("average of list=",avg)'''

#Python | Sum of number digits in List

'''list=[1,2,3,4,5]
print(list)
sum=0
i=0
while i<len(list):
    sum+=list[i]
    i+=1
print("sum of numbers digits in  list=",sum)'''

#Python | Multiply all numbers in the list

'''def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
 
list1 = [1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
list2 = [1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
print(multiplyList(list1))
print(multiplyList(list2))'''

#Python program to find smallest number in a list

'''list = [1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
list.sort()
print ("smallest number in a list :",list[0])'''

#Python program to find largest number in a list

'''list = [1,2,3,1000,4,7,7,7,5,90,6,7,8,9,10,11,66]
list.sort()
print ("largest number in a list :",list[-1])'''

#Python program to find second largest number in a list

'''list = [1,2,3,1000,4,7,7,7,101,5,90,6,7,8,9,10,11,66]
list.sort()
print ("Second largest number in a list :",list[-2])'''

#Python program to print even numbers in a list
'''list = [1,2,3,1000,4,7,7,7,101,5,90,6,7,8,9,10,11,66]
for num in list:
    if num % 2 == 0:
        print(num, end=" ")   '''


#Python program to print odd numbers in a List
'''list1 = [1,2,3,1000,4,7,7,7,101,5,90,6,7,8,9,10,11,66]
for num in list1:
    if num % 2 != 0:
       print(num, end=" ")'''


 
#Python program to print all even numbers in a range

'''for even_numbers in range(4,15,2):
    print(even_numbers,end=' ')'''


#Python program to print all odd numbers in a range

'''start, end = 9,50
for num in range(start, end + 1):
     
    if num % 2 != 0:
        print(num, end = " ")'''

#Python program to count Even and Odd numbers in a List

'''a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 
even , odd = 0,0
for num in a:
    if num % 2 == 0 :
        even+=1
    else:
        odd+=1
print("odd number:",odd)
print("even number:",even)'''

#Python program to print positive numbers in a list

'''list = [-10, 21, -4, -45,55,-87,95,70, -66, 93]
num = 0   
while(num < len(list)):
    if list[num] >= 0:
        print(list[num], end = " ")
    num += 1'''


#Python program to print negative numbers in a list

'''list = [-10, 21, -4, -45,55,-87,95,70, -66, 93]
for num in list:
    if num < 0:
     print(num, end=" ")'''


#Python program to print all positive numbers in a range

'''start, end = -4, 19
for num in range(start, end + 1):
    if num >= 0:
        print(num, end=" ")'''

#Python program to print all negative numbers in a range

'''def negativenumbers(a,b):
  out=[i for i in range(a,b+1) if i<0]
  print(*out)
a=-4
b=5
negativenumbers(a,b)'''

#Python program to count positive and negative numbers in a list

'''list1 = [10, -21, 4, -45, 66, -93, 1]
 
postivecount, negativecount = 0, 0
 
for num in list1:

    if num >= 0:
       postivecount += 1
 
    else:
       negativecount += 1
 
print("Positive numbers in the list: ",postivecount)
print("Negative numbers in the list: ", negativecount)'''

#Remove multiple elements from a list in Python

'''list = [11, 5, 17, 18, 23, 50, 87, 35, 45, 44]
for element in list:
    if  element % 2 == 0:
        list.remove( element)
print("New list after removing all even numbers: ", list)'''

#Python | Remove empty tuples from a list

'''def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [(), ('adhi','26','3'), (), ('rama', 'athira'),
          ('krishna', 'haritha', '35'), ('',''),()]
print(Remove(tuples))'''


#Python | Program to print duplicates from a list of integers

lis = [1,2,3,1000,4,7,7,7,101,5,90,9,5,6,3,1,1,2,2,89,8,9,6,7,8,9,10,11,66]
 
uniqueList = []
duplicateList = []
 
for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)

#listduplicate
a=[]
n=int(input("enter the number of elements ="))
print("enter the elements =")
for i in range(0,n):
    k=int(input())
    a.append(k)
i=0
while i<n-1:
    j=i=1
    while j<n:
        if a[i]==a[j]:
            a.pop(j)
            n=n-1
        else:
            j+=1
    i+=1
print(a)

#listdelete
a=[]
n=int(input("enter the number of elements ="))
printt("enter the elements =")
for i in range(0,n):
    k=int(input())
    a.append(k)
index=int(input("enter the index ="))
for i in range(index,n-1):
    a[i]==a[i+1]
n=n-1
print("list elements are =")
for i in range(0,n):
    print(a[i])

#listcount
a=[]
n=int(input("enter the number of elements ="))
print("enter the elements =")
for i in range(0,n):
    k=int(input())
    a.append(k)
count=0
ele=int(input("enter the element to count ="))
for x in a:
    if x==ele:
        count+=1
print(ele,"occured",count,"times") 

#listbig
a=[]
n=int(input("enter the number of elemnts ="))
print("enter the elements =")
for i in range(0,n):
    k=int(input())
    a.append(k)
big=a[0]
for i in range(1,n):
    if a[1]>big:
        big=a[i]
print("biggest =",big)

        
      




    



    



