# Task 12 Armstrong Number Checker:- Accept a positive integer and check whether it is an Armstrong number


try:
    num = int(input("Enter Number:- "))

    og = num    
    dig = len(str(num))
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** dig
        num = num // 10

    if sum == og:
        print(f"Yes {og} is Armstrong Number")
    else:    
        print(f"No {og} is Not Armstrong Number")
        
except ValueError:
    print("Enter Valid Number!")