#salary
bs=int(input("enter the basic salary ="))
if bs<10000:
    da=bs*0.25
    hra=bs*0.3
    pf=bs*0.08
elif bs>=10000 and bs<20000:
    da=bs*0.20
    hra=bs*0.25
    pf=bs*0.06
elif bs>=20000 and bs<30000:
    da=bs*0.10
    hra=bs*0.15
    pf=bs*0.02
ns=bs+da+hra-pf
print("basic salary =",bs)
prit("DA = ",da)
print("HRA =",hra)
print("PF =",pf)
print("net salary =",ns)




[10:48 am, 14/06/2023] Suhail BCA: num=int(input("Enter the number : ")) 
print("Menu") 
print("1.Automorphic")
print("2. Trimorphic")
choice=int(input("Enter your choice : "))
l=len(str(num))
if choice==1:
    sq=num*2 
    if sq%(101)==num: 
         print(num," is automorphic") 
    else: 
         print(num," is not automorphic") 
elif choice==2:
       cb=num
       if cb% (10*1)==num: 
         print(num," is trimorphic") 
       else: 
         print(num," is not trimorphic")
else:
    
     print("Invalid choice!!!")'''
[10:49 am, 14/06/2023] Suhail BCA: '''type=input("Enter the type of connection :") 
u=int(input("Enter the units consumed : "))
charge=0 
if type=="domestic": 
    if u<=100: 
        charge=u*1 
    elif u<150: 
        charge (100*1)+(u-100)*1.5 
    elif u<=200: 
        charge (100*1)+(50*1.5)+(u-150)*2 
    else: 
        charge=(100*1)+(50*1.5)+(50*2)+(u-200)*3
elif type=="commercial":
    if u<=100: 
        charge=u*3 
    elif u<150: 
        charge (100*3)+(u-100)*4 
    elif u<=200: 
         charge=(100*3)+(50*4)+(u-150)*6 
    else:
         charge (100*3)+(50*4)+(50*6)+(u-200)*10 
else: 
    print("Invalid connection type ") 
    print("Tarriff: ",charge)'''