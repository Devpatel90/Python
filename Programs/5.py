# Task 5 Student Grade Calculator Accept marks from 0 to 100 and display grade A, B, C, D or F. Reject marks outside the valid range.

# try:
    # mark = int(input("Enter Marks Between (0-100):-"))

    # if mark < 0 or mark > 100:
    #     print("Invalid Entry")

    # elif mark >= 90:
    #     print("Marks:-", mark)
    #     print("Grade:- A")

    # elif mark >= 80:
    #     print("Marks:-", mark)
    #     print("Grade:- B")

    # elif mark >= 70:
    #     print("Marks:-", mark)
    #     print("Grade:- C")

    # elif mark >= 60:
    #     print("Marks:-", mark)
    #     print("Grade:- D")

    # else:
    #     print("You are Fail!!")
# except ValueError:
    # print("Enter Valid Number")
    
# --------------------------------------------------------------------------------------------------------------------

try:
    mark = int(input("Enter Marks Between (0-100):-"))

    if mark < 0 or mark > 100:
        print("Invalid Entry")

    else:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"

        match grade:
            case "A":
                print("You Got A Grade")
            case "B":
                print("You Got B Grade")
            case "C":
                print("You Got C Grade")
            case "D":
                print("You Got D Grade")
            case "F":
                print("You are Fail!!")
            case _:
                print("Invalid Grade")
                
except ValueError:
    print("Enter Valid Number")

# --------------------------------------------------------------------------------------------------------------------

# try:
#     marks = int(input("Enter marks: "))

#     if marks < 0 or marks > 100:
#         print("Invalid marks!")

#     else:
#         match marks:
#             case marks if marks >= 90:
#                 print("Grade A")

#             case marks if marks >= 80:
#                 print("Grade B")

#             case marks if marks >= 70:
#                 print("Grade C")

#             case marks if marks >= 60:
#                 print("Grade D")

#             case _:
#                 print("Grade F")

# except ValueError:
#     print("Please enter a valid number!")