students = {}

while True:
    
    print("\n--------SMS--------")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6.Exit")
    
    choice = input("Enter Choice:- ")
    
    if choice == "1":
        name = input("Enter Name:- ")
        mark = int(input("Enter Mark:- "))
        students[name] = mark
        
        print("Added Successfully")
        
    elif choice == "2":
        for name, mark in students.items():
            print("\n",name, ":", mark)
            
    elif choice == "3":
        name = input("Enter Name:- ")
        
        if name in students:
            marks = int(input("Enter Marks:- "))
            students[name] = marks
        
            print("Updated")
        
        else:
            print("Student Not Found")
            
    elif choice == "4":
        name = input("Enter Name:- ")
        
        if name in students:
            del students[name]
            print("Deleted")
        
        else:
            print("Student Not Found")
            
    elif choice == "5":
        
        name = input("Enter Name:- ")
        if name in students:
            print("Marks:- ", students[name])
            
        else:
            print("Student Not Found")
            
    elif choice == "6":
        print("Exited")
        break

    else:
        print("invalid choice")