print("enter the leapyear")
year=int(input("enter the year"))
if year%4==0 and year%100!=0:
    print("the year is leapyear")
else:
    print("the year is not leapyear")

