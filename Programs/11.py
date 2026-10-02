# Task 11 Palindrome Checker:- Accept a word or number and check whether it reads the same forward and backward. Ignore letter case.

# try:
#     n = input("Enter Name or Number:- ")

#     n = n.lower()

#     reverse = n[::-1]

#     if n == reverse:
#         print(f"Yes {n} is Palindrome")
#     else:
#         print(f"No {n} is Not Palindrome")

# except Exception as e:
#     print(e)
    
# -----------------------------------------------------------------------------------------
    

try:
    text = input("Enter a word or number: ")

    text = text.lower()

    reverse = ""

    for i in text:
        reverse += i

    if text == reverse:
        print("It is a palindrome.")

    else:
        print("It is not a palindrome.")

except Exception as e:
    print(e)