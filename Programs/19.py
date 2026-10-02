"""

Task 19 Number Triangle Pattern:- Accept the number of rows and print a triangle in which each row contains its row number repeated.

1
22
333
4444
55555

"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

# try:
    # r = int(input("Enter Rows:- "))

    # for i in range(1,r+1):
    #     for j in range(i):
    #         print(i, end="")
    #     print()

# except ValueError:
    # print("Enter Valid Number")

# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    

try:
    r = int(input("Enter Rows:- "))

    i = 1
    while i <= r:
        j = 1
        while j<=i:
            print(i,end="")
            j += 1
        print()
        i += 1    
        
except ValueError:
    print("Enter Valid Number")