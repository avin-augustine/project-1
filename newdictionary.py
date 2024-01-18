#dict program 1
bus={
    "routeno":5,
    "driver":"manu",
    "cleaner":"manu",
    "points":["karmana","PMG","pattom"]
}
print(bus)
print("the driver =",bus["driver"])
print(bus.get("driver"))
bus.keys()
bus.values()
bus.items()
bus["color"]="red"

bus["driver"]="mohan"
bus.pop("fare")
bus.popitem()
del bus["fare"]
del bus
bus.clear()

for x in bus:
    print(x)
for x in bus:
    print(bus[x])

'''#dict program 2
student={"name":"kiran",
          "age":25,
          "mark1":76,
          "mark2":85}
student["name"]
student.get("name")
student.keys()
student.values()

student["names"]="manu"
student["phone"]=958744123
student.update({"name":"mohan"})
student.update({"address":"kottayam"})

student.pop("name")
student.popitems()
del student["name"]
del student
student.clear()
candidate=student.copy()
candidate=dict(student)
#print(student) =>{name:kiran,age:25...}

#dict program 3
contactlist={}
n=int(input("enter the number of contacts : "))
for i in range(1,n+1):
    name=input("enter the contact name : ")
    phno=int(input("enter the phone number : "))
    contactlist[name]=phno
print("keys")
for x in contactlist.keys():
    print(x)
print("values")
for x in contactlist.values():
    print(x)
print("keys-value pairs")
for x,y in contactlist.items():
    print(x,"-",y)

#program 4
numberNames={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
positionvalues={0:'ones',1:'tens',2:'hundreds',3:'thousands',4:'ten thousands',5:'lakhs',6:'ten lakhs',7:'crore',8:'ten crore'}
num=input("enter any number")
reslut=''
l=len(num)-1
for ch in num:
    key=int(ch)
    value=numberNames[key]
    result=reslut + ' ' + value+' '+ positionvalues[1]
    l-=1
print("the number is : ",num)
print("the number name is : ",result)'''
