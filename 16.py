""" 

Task 16 Right Triangle Star Pattern:- Accept the number of rows and print a right-angled triangle star pattern using nested loops.
*
**
***
****
*****

"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

# try:
    # r = int(input("Enter Rows:- "))

    # for i in range(1,r+1):
    #     for j in range(i):
    #         print("*",end="")
            
    #     print()

# except ValueError:
    # print("Enter Valid Number")
    
# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    

# try:
    # r = int(input("Enter Rows:- "))

    # i = 1 
    # while i <= r:
    #     j = 1
    #     while j <= i:
    #         print("*",end="")
    #         j += 1
    #     print()
    #     i +=1

# except ValueError:
    # print("Enter Valid Number")    
    
"""
    
    *
   **
  ***
 ****
***** 

"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

# try:
    # r = int(input("Enter Rows:- "))

    # for i in range(1,r+1):
    #     for j in range(r-i):
    #         print(" ", end="")
    #     for j in range(i):
    #         print("*",end="")
            
    #     print()
# except ValueError:
    # print("Enter Valid Number") 
       
# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    

try:

    r = int(input("Enter Rows:- "))
    i = 1 
    while i <= r:
        j = 1
        while j <= r-i:
            print(" ", end="")
            j += 1
        j = 1
        while j <= i:
            print("*", end="")
            j += 1
        print()
        i += 1
except ValueError:
    print("Enter Valid Number")        