# Task 2 Even or Odd Number:- Write a program that accepts an integer and checks whether it is even or odd.
try:
    num = int(input("Enter Number to Check Even or Odd:- "))

    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

except ValueError:
    print("Enter Valid Number!!")