#Write a shutting down program:

def shut_down(s):
    if s=='yes':
        return("shutting down")
    elif s=='no':
        return("shutdown aborted")
    else:
        return("sorry")

a=input("enter yes or no =")
p=shut_down(a)
print(p)

#cube program

def cube(number):
    return(number**3)
def by_three(number):
    if number%3==0:
        c=cube(number)
        return(c)
    else:
        return("false")
a=int(input("enter number"))
p=cube(a)
b=by_three(a)
print(p)
print(b)

#