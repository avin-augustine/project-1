import phonebookproa


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