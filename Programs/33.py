students = ["\nRaj", "Mehul", "Samay", "Sunny"]

is_o = True
while is_o:
    
    print("\n------SMS------")
    print("1. Show Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    cho = input("Enter Number:- ")
    
    if cho == "1":
        
        for student in students:
            print(student)
            
    elif cho == "2":
        
        name = input("Enter Name to Add:- ")
        
        students.append(name)
        print(f"{name} Added Successfully")
        
    elif cho == "3":
        
        oldname = input("Enter Old Name:- ")
        
        if oldname in students:
            newname = input("Enter New Name:- ")
            
            ind = students.index(oldname)
            students[ind] = newname
            
            print("Updated Successfully")
        
        else:
            print("Student Not Found")
                
    elif cho == "4":
        
        dele = input("Enter Name to Del:- ")
        
        if dele in students:
            students.remove(dele)
            print("Student Deleted")
        
        else:
            print("Student Not Found")
            
    elif cho == "5":
        print("Exited")
        is_o = False
    
    else:
        print("Invalid Choice")