"""

Task 20 Floyd Triangle:- Accept the number of rows and print Floyd's triangle using consecutive integers.

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

# --------------------------------------------------------------------------ForLoop-----------------------------------------------------------    

# try:
    # r = int(input("Enter Rows:- "))

    # num = 1   
    
    # for i in range(1,r+1):
    #     for j in range(i):
    #         print(num, end="")
    #         num += 1
    #     print()
    
# except ValueError:
    # print("Enter Valid Number")
    
    
# --------------------------------------------------------------------------WhileLoop-----------------------------------------------------------    
    
try:
    r = int(input("Enter Rows:- "))

    num = 1   

    i = 1
    while i <= r:
        j = 1
        while j <= i:
            print(num,end="")
            num += 1
            j += 1
        print()
        i += 1

except ValueError:
    print("Enter Valid Number")