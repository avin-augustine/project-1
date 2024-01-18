'''#write python program to find the eletricity bill
print("Electricity bill")
unit=float(input("enter the unit ="))
amount=0
if unit<=100:
    amount=unit*0.50
    print(amount)
if unit>100 and unit<150:
    amount=unit*0.7
    print(amount)
if unit>150 and unit<200:
    amount=unit*1
    print(amount)
if unit>=200:
    amount=unit*2
    print(amount)'''

unit=int(input("enter the unit ="))
cost=0
if unit<=100:
    cost=unit*0.5
elif unit<=150 and unit>100:
    cost= 0.5*100 +(unit-100)*0.75
elif unit<=200 and unit>150:
    cost= 0.5*100 + .75*50 +(unit-150)*1
elif unit>200:
    cost= 0.5*100 + .75*50 + 1*50 +(unit-200)*2
print(cost)


