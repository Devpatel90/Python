# Task 13 Reverse and Sum Digits:- Accept an integer, reverse its digits and calculate the sum of its digits using a loop


try:
    num = input("Enter Number:- ")


    a = num[::-1]

    b = int(a) 

    print("Reverse Number:- ",b)

    Total = 0

    for i in num:
        Total += int(i)

    print("Sum of Digits:- ",Total)

except Exception as e:
    print(e)