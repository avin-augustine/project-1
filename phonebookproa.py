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