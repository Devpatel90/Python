# Task 15 GCD and LCM Calculator:- Create separate functions to calculate the GCD and LCM of two positive integers.

try:
    num1 = int(input("Enter First Number:- "))
    num2 = int(input("Enter Second Number:- "))

    def gcd(a,b):
        gcd = 1
        for i in range(1,min(a, b)+1):
            if a % i == 0 and b % i == 0:
                gcd = i
        return gcd

    def lcm(a,b):
        lcm = (a * b) // gcd(a,b)
        return lcm

    if num1 <= 0 or num2 <= 0:
        print("Please Enter Positive Numbers")
    else:
        print("GCD is:-",gcd(num1, num2))
        print("LCM is:-",lcm(num1, num2))

except ValueError:
    print("Enter Valid Number")