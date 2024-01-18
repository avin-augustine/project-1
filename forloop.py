'''#write a python program print 1 to 50 numbers using for loop
print("enter the number")
for i in range(1,51):
    print(i)
#break the program in 10
print("enter the number")
for i in range(1,51):
    if i==10:
        break
    print(i)'''

#to count the number of even and odd numbers in a series of numbers
#number series : numbers =(1,2,3,4,5,6,7,8,9)

print("odd and even numbers")
num=(1,2,3,4,5,6,7,8,9)
odd=0
even=0
for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("odd numbers = ",odd)
print("even numbers = ",even)





    

    