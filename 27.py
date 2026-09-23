# Rock, Paper, Scissors Game

import random

try:
    playerp = 0
    computerp = 0
    choices = ["Rock", "Paper", "Scissors"]
    while True:
        
        computer = random.choice(choices)
        
        player = input("Enter Rock, Paper, Scissors or e to Exit:- ")
        
        
        if player == "e":
            print("Game Exited...")
            print("Player Points:- ", playerp)
            print("Computer Points:- ", computerp)
            break
        
        elif player not in choices:
            print("Invalid Choice")
            continue
            
        elif player == computer:
            print("Tie...!")
            print("Computer:-", computer)

        elif player == "Rock" and computer == "Scissors":
            print("You Won")
            print("Computer:-", computer)
            playerp += 1
            print("Player Points:- ", playerp)
        
        elif player == "Paper" and computer == "Rock":
            print("You Won")
            print("Computer:-", computer)
            playerp += 1
            print("Player Points:- ", playerp)
        
        elif player == "Scissors" and computer == "Paper":
            print("You Won")
            print("Computer:-", computer)
            playerp += 1
            print("Player Points:- ", playerp)
            
        else:
            print("Computer:-", computer)
            print("Computer Winsss")
            computerp += 1
            print("Computer Points:- ", computerp)
            
except ValueError as e:
    print("Error", e)
    
except Exception as f:
    print("Error", f)
    
finally:
    print("Thank You For Playing!!!")