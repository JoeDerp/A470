def factorial(num):
    num0 = num
    fact = 1
    while num > 0:
        fact = fact * num
        num -= 1
    print("The factorial of",num0,"is",fact)

factorial(5)

def evens(range):
    print("The even numbers from 0 to",range,"are as follows:")
    i = 0
    while i <= range:
        if i % 2 == 0:
            print(i)
        i += 1

evens(20)

import random
rps = ["rock","paper","scissors"]
def rockPaperScissors():
    print("Let's play rock, paper, scissors!")
    
    while True:
        choice = str(input("Choose between rock, paper, scissors, or exit to not play --> ")).lower()
        if choice == "exit":
            print("Thank you for playing!")
            break
        elif choice != rps[0] and choice != rps[1] and choice != rps[2]:
            print("Check your spelling!")
        else:
            comp = random.choice(rps)
            if choice == comp:
                print("It's a tie, try again")
            elif choice == "rock" and comp == "paper" or choice == "paper" and comp == "scissors" or choice == "scissors" and comp == "rock":
                print("Computer chose",comp,"and you lose :(")
            else:
                print("Computer chose",comp,"and you win!!")

rockPaperScissors()