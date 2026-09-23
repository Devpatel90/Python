# Task 6 Multiplication Table:- Accept a number and print its multiplication table from 1 to 10 using a loop

# try:
    # num = int(input("Enter Number:- "))

    # for i in range(1,11):
        # print(f"{num} * {i} =", num*i)
# except ValueError:
    # print("Enter Valid Number")

# -----------------------------------------------------------------------------------------


try:
    num = int(input("Enter Number:- "))

    i = 1
    while i<=10:
        print(f"{num} * {i} =",num*i)
        i += 1
        
except ValueError:
    print("Enter Valid Number")