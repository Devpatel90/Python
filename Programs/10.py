# Task 10 Fibonacci Series:- Accept the number of terms and print the Fibonacci series starting with 0 and 1.

# try:
    # num = int(input("Enter Number:- "))

    # a = 0
    # b = 1
    # for i in range(num):
    #     print(a ,end="")
    #     c = a+b
    #     a = b
    #     b = c
    
# except ValueError:
    # print("Enter Valid Number")

# -----------------------------------------------------------------------------------------

try:
    num = int(input("Enter Number:- "))

    a = 0
    b = 1
    if (num > 0 ):  
        i=0
        while i<num:
            print(a ,end="")
            c = a+b
            a = b
            b = c
            i += 1
    else:
        print("Enter +ve Number")
        
except ValueError:
    print("Enter Valid Number")