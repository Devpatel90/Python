# Task 3 Largest of Three Numbers:- Write a program that accepts three numbers and displays the largest number without using max().

try:
    n1 = int(input("Enter First Number:- "))
    n2 = int(input("Enter Second Number:- "))
    n3 = int(input("Enter Third Number:- "))

    if n1 == n2 and n2 == n3:
        print("All three numbers are equal")
    elif n1 == n2 and n1 > n3:
        print("1st and 2nd numbers are equal and largest")
    elif n1 == n3 and n1 > n2:
        print("1st and 3rd numbers are equal and largest")
    elif n2 == n3 and n2 > n1:
        print("2nd and 3rd numbers are equal and largest")
    elif n1 > n2 and n1 > n3:
        print("First Number is Greater")
    elif n2 > n1 and n2 > n3:
        print("Second Number is Greater")
    else:
        print("Third Number is Greater")

except ValueError:
    print("Enter Valid Number")