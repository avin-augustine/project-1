'''#find sum and avereage of list in python
newlist=[4,7,9,5]
print(newlist)
sum=0
for i in newlist:
    sum=sum+i
print("sum = ",sum)
avg=sum/len(newlist)
print("average = ",avg)

#second largest number in a list
lst=[5,2,4,8,9,10]
print(lst)
large=0
for i in lst:
    if i>large:
        large=i
    else:
        i+=1
print(large)
lst.remove(large)
print(lst)
high=0
for h in lst:
    if h>high:
        high=h
    else:
        h+=1
print(high)

lest=[8,10,3,7,9,2,5]
print(lest)
l=sorted(lest)
print(l)
print("second largest num = ",l[-2])
print("largest num =",l[-1])
print("smallest num = ",l[0])



#smallest number in a list
newlist=[6,3,5,8,9,10]
print(newlist)
s=0
small=0
for s in newlist:
    if s<small:
        small=s
    else:
        s+=1
print("smallest num =",small)

k=sorted(newlist)
print(k)
print("smallest num =",k[0])'''

'''#find the size of the tuple
newtuple=(8,3,0,4,5,3,7,9)
print(newtuple)
print(len(newtuple))'''
#sort a list of tuples by second item
#capitalize the first and last character of each word in a string
#count the number of matching caracters in a pair of string
streng1="4,8,0,2,4,7"
streng2="8,4,7,9,3,5"
a=0
for i in streng1:
   for m in streng2:
    if(i==m):
        a+=1
print(a)
#removing i'th character from a string'''





