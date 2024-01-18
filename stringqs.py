'''print(dir(str))'''
#convert a string to a lower
word="  Python Programming"
print(word.lower())
#write a python program to use capitilize method
print(word.upper())
#remove white spaces from the beginig of a string
print(word)
print(word.lstrip())
#write a python progrom to use end s with the method
print(word.endswith('s'))
#write a program to check wether a cretain character or phrase is present in a string or not
n=str(input("character and phrase is present or not"))
print(n in word)
#write a python program to find the length of the string
print(len(word))
#write a python program to split the atrings into substrings
print(word.split())
#write a python program to use the case fold method
print(word.casefold())
#write a python program to replace a string with other,get the first charcater of the string txt.
txt='welcome to python'
i=txt.replace('w','c')
print(i)

#get the characters from index 2 to index 4,txt="welcome to python"
txt="welcome to python"
print(txt[2:5])
#22. Return the string without any whitespace at the beginning of the end. txt = " Welcome to python " 
txt = " Welcome to python " 
print(txt.strip())
#23. Using the type() function assign the type of the variable to answer_1, then print it. 
x="8"
answer_1=type(x)
print(answer_1)
#25.str="It's always darkest before dawn." ,Replace the (.) with (!)
str="It's always darkest before dawn."
print(str.replace('.','!'))
#str="EVERY Strike Brings Me Closer to the Next Home run.", Reassign str so that, all its characters are lowercase. 
str="EVERY Strike Brings Me Closer to the Next Home run."
print(str.lower())
#Make the string so that everything is properly and the first letter is capital str="there are no traffic JamS Along with The extra " 
str=" there are no traffic JamS Along with The extra " 
print(str.strip())
i=str.strip()
print(i.capitalize())
#print the types of two given variables with the print function,v_1="1",v_2=1
v_1="1"
v_2=1
print(type(v_1))
print(type(v_2))
#what is the length of the given string,str="1.975.000"
str="1.975.000"
print(len(str))
#write a pytho  program to add an item to a tuple
t=(2,8,10)
print(t)
print(type(t))
print(t.add(6))











