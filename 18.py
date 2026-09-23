"""

# Task 18 Centered Pyramid Pattern:- Accept the number of rows and print a centered pyramid star pattern using spaces and nested loops.

    *
   ***
  *****
 *******
*********

"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

# try:
    # r = int(input("Enter Rows:- "))

    # for i in range(1,r+1):
    #     for j in range(r-i):
    #         print(" ", end="")
        
    #     for j in range(2 * i - 1):
    #         print("*", end="")
            
    #     print()

# except ValueError:
    # print("Enter Valid Number!")
    
# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    

try:
    r = int(input("Enter Rows:- "))

    i = 1
    while i<=r:
        j=1
        while j<=r-i:
            print(" ",end="")
            j += 1
        j=1
        while j<=2*i-1:
            print("*",end="")
            j += 1
        print()
        i+=1
    
except ValueError:
    print("Enter Valid Number!")
    
"""

*********
 *******
  *****
   ***
    *
    
"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

# try:
    # for i in range(r-1,0,-1):
    #     for j in range(r-i):
    #         print(" ", end="")
        
    #     for j in range(2 * i - 1):
    #         print("*", end="")
            
    #     print()

# except ValueError:
    # print("Enter Valid Number!")


# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    

try:
    r = int(input("Enter Rows:- "))

    i = r
    while i>=1:
        j=1
        while j<=r-i:
            print(" ",end="")
            j += 1
        j=1
        while j<=2*i-1:
            print("*",end="")
            j += 1
        print()
        i-=1

except ValueError:
    print("Enter Valid Number!")