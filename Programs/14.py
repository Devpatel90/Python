# Task 14 Number Guessing Game:-Generate a random number from 1 to 100 and allow the user to guess it. Display Too high or Too low until the answer is correct.

# try:
    # import random

    # ran = random.randint(1,100)

    # num =int(input("Guess Number b/w (0-100):- "))

    # while ran != num:
    #     if num > ran:
    #         print("Too High!")
    #     elif num < ran:
    #         print("Too Low!")
            
    #     num =int(input("Guess Again b/w (0-100):- "))
    # print("Correct")    

# except ValueError:
    # print("Enter Valid Number")

# -----------------------------------------------------------------------------------------------------------

try:
    import random

    ran = random.randint(1,100)

    for i in range(1,11):
        num =int(input("Guess Number b/w (0-100):- "))
        if num > ran:
            print("Too High!")

        elif num < ran:
            print("Too Low!")

        else:
            print("Correct!")
            break

    else:
        print("Game Over!")
        print("The Number was:", ran)
    
except ValueError:
    print("Enter Valid Number")