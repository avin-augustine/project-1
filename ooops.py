#oops contain a class and object,4 properties Inheritence,polymorphisim,encapsulation,class is a collection of objects
#inheritance,parent child relationship,public
#single multiple multilevel hireracrichial hybrid(types of inheritence)
#abstraction=hiding the data or hiding the process
#encapsulation=wrapping upon the data in a single unit,private
#polymorphism=same character with diffrent behavior ywo types,static and runtime polymorphisim
#method overloading=same method with diffrent parameter,***python not support***
#method overiding=same method with same parameter
#constructor= to handle or invoke  the objects in the class in python.to create use 'init'.***object keyword=new***
#default and parameterizd constructor
#self keyword=reference keyword
#module is a python file which conain python directories

'''#create a class
#basic 1
class Basic:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sample(self):
        print("my name is : ",self.name)
        print("my age is : ",self.age)

obj=Basic("mahan",20)
obj.sample()

#basic 2 without function
class Basic:
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj1=Basic("jack",20)
obj2=Basic("jill",21)
print(obj1.name)
print(obj1.age)

#non parameterized 
class Student:
    def __init__(self):
        print("haii everyone")

    def display(self,name):
        print("haii",name)

st=Student()
st.display("jill")'''

#default constructor ,single inheritence

class Animal:
    def speak(self):
        print("animal is speaking")

class Dog(Animal):
    def bark(self):
        print("dog is barking")

d=Dog()
d.speak()
d.bark()

        
