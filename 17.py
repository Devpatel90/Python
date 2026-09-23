"""

Task 17 Inverted Star Pattern:- Accept the number of rows and print an inverted right-angled triangle star pattern.

*****
****
***
**
*

"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

try:
    r = int(input("Enter Rows:- "))

    for i in range(r,0,-1):
        for j in range(i):
            print("*", end="")
        print()

except ValueError:
    print("Enter Valid Number")
    
# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    

# try:

    # r = int(input("Enter Rows:- "))
    # i = r
    # while i>=0:
    #     j = 1
    #     while j <= i:
    #         print("*",end="")
    #         j += 1
    #     print()
    #     i-=1

# except ValueError:
    # print("Enter Valid Number")
    
"""

*****
 ****
  ***
   **
    *

"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

# try:
    # r = int(input("Enter Rows:- "))

    # for i in range(r,0,-1):
    #     for j in range(r-i):
    #         print(" ", end="")
    #     for j in range(i):
    #         print("*", end="")
    #     print()

# except ValueError:
    # print("Enter Valid Number")
    
# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    

try:
    r = int(input("Enter Rows:- "))
    i = r
    while i>=0:
        j = 1
        while j <= r-i:
            print(" ",end="")
            j += 1
        j=1
        while j<=i:
            print("*",end="")
            j+=1
        print()
        i-=1

except ValueError:
    print("Enter Valid Number")