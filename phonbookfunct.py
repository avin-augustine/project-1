#phonebook
def add(name,phn):
    student[name]=phn 
    print("Details Added successfully")

def edit():
    n = input("Enter the name to be edit:")
    if(n in student.keys()):
        e_name = input("Enter your edit name:")
        e_phn = int(input("Enter your edit phone no:"))
        student[e_name] = student.pop(n)
        student[e_name] = e_phn  
        print("Details edited successfully")
    
def search(a):
    if(a in student.keys()):
        s = student[a]
        print("Searched element detail:",s)
    
def display():
    print("Student Details:")
    print(student)

def delete(x):
    if(x in student.keys()):
        student.pop(x)
    print("item deleted successfully")

def exits():
    exit()

student = {}

while(True):
    print("\nEnter Your choices:")
    print("1.Add\n2.Edit\n3.Search\n4.Display\n5.Delete\n6.Exit")
    choice = int(input())
    if(choice == 1):
        name = input("Enter name:")
        phn = int(input("Enter mobile no:"))
        add(name,phn)
    elif(choice == 2): 
        edit()
    elif(choice == 3):
        ele = input("Enter the name to search:")
        search(ele)
    elif(choice == 4):
        display()
    elif(choice == 5):
        x = input("Enter the name to be delete:")
        delete(x)
    elif(choice == 6):
        exits()
    else:
        print("Invalid choice! Re-enter the choice")