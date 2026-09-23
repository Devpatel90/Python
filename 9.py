# Task 9 Prime Number Checker:- Accept an integer and check whether it is a prime number.

# try:
    # num = int(input("Enter Number:- "))

    # count = 0
    # for i in range(1,num+1):
    #     if num % i == 0:
    #         count += 1
        
    # if count == 2:
    #     print(f"{num} is Prime")
    # else:
    #     print(f"{num} is Not Prime")
    
# except ValueError:
    # print("Enter Valid Number")


# -----------------------------------------------------------------------------------------

try:
    num = int(input("Enter Number:- "))

    count = 0
    i = 1
    while i<=num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(f"{num} is Prime")
    else:
        print(f"{num} is Not Prime")
        
except ValueError:
    print("Enter Valid Number")