# Task 4 Simple Calculator:- Create a calculator that performs addition, subtraction, multiplication and division based on the user's choice. 
# Handle division by zero.

# try:
    # num1 = int(input("Enter First Number:- "))
    # num2 = int(input("Enter Second Number:- "))
    # op = input("Enter Your Choice(+,-,*,/,%,**):-")

    # if (op == "+"):
    #     ans = num1 + num2
    #     print("Addition of Number1 and Number2 is:- ", ans)
    # elif (op == "-"):
    #     ans = num1 - num2
    #     print("Subtraction of Number1 and Number2 is:- ", ans)
    # elif (op == "*"):
    #     ans = num1 * num2
    #     print("Multiplication of Number1 and Number2 is:- ", ans)
    # elif (op == "/"):
    #      if num2 == 0:
    #         print("Cannot divide by zero")
    #      else:
    #         ans = num1 / num2
    #         print("Division of Number1 and Number2 is:- ", ans)
    # else:
    #     print("Invalid Input")
# except ValueError:
    # print("Enter Valid Entry")

# -----------------------------------------------------------------------------------------

try:
    while True:

        num1 = int(input("Enter First Number:- "))
        num2 = int(input("Enter Second Number:- "))
        op = input("Enter Your Choice(+,-,*,/,%,**,e):-")

        match op:
        
            case "+":
                ans = num1 + num2
                print("Addition of Number1 and Number2 is:- ", ans)
                
            case "-":
                ans = num1 - num2
                print("Subtraction of Number1 and Number2 is:- ", ans)
                
            case "*":
                ans = num1 * num2
                print("Multiplication of Number1 and Number2 is:- ", ans)
        
            case "/":
                    ans = num1 / num2
                    print("Division of Number1 and Number2 is:- ", ans)
                           
            case "%":
                    ans = num1 % num2
                    print("Modulus of Number1 and Number2 is:- ", ans)
                        
            case "**":
                ans = num1 ** num2
                print("Exponent of Number1 and Number2 is:- ", ans)
                
            case "e":
                print("Exited Successfully")
                break
            
            case _:
                print("Invalid Input! Enter Choice (+,-,*,/,%,**,e):- ")

except ValueError:
    print("Enter Valid Entry!!")
    
except ZeroDivisionError:
    print("Cannot Divided by Zero")