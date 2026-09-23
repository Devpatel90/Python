# Task 7 Sum of Natural Numbers:- Accept a positive number n and calculate the sum of all natural numbers from 1 to n using a loop.

# try:
    # num = int(input("Enter Number:- "))

    # sum = 0
    # for i in range(1,num+1):
    #     sum += i
    # print("sum of first n natural numbers is:-",sum)

# except ValueError:
    # print("Enter Valid Number!")

# -----------------------------------------------------------------------------------------

try:
    num = int(input("Enter Number:- "))

    sum = 0
    i = 0
    while i<=num:
        sum += i
        i += 1

    print("Sum of N Numbers is:-",sum)

except ValueError:
    print("Enter Valid Number!")