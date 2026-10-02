# Task 8 Factorial of a Number:-
# Create a function that calculates the factorial of a non-negative integer. Handle 0 and reject negative input.

# try:
    # num = int(input("Enter Number:- "))

    # def fact(n):
    #     if (n >= 0):    
    #         fact = 1
    #         for i in range(1,n+1):
    #             fact *= i
    #         print(f"Factorial of {n} is:-",fact)
    #     else:
    #         print("Invalid Number!!")
    # fact(num)
    
# except ValueError:
    # print("Enter Valid Number")


# -----------------------------------------------------------------------------------------

try:
    num = int(input("Enter Number:- "))

    def fact(n):
        if (n >= 0):    
            fact = 1
            i = 1
            while i<=n:
                fact *= i
                i += 1
            print(f"Factorial of {n} is:-", fact)
        else:
            print("Invalid Number")

    fact(num)
    
except ValueError:
    print("Enter Valid Number!!")