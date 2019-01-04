#Rock-Paper-Scissor Game
import random


print("Please enter your name:")
userName = input()
print("Welcome " + userName)
print("The following are the rules of the game:")
print("Press 'R' for Rock")
print("Press 'P' for Paper")
print("Press 'S' for Scissor")
print("This will be a 10 point match")

userTally = 0
compTally = 0


def gameProcess(): #The process of the game. It increments or decrements the value depending on the result
    print("Your turn:")
    userInput = input()
    computerChoice = random.choice(["R","P","S"])
    global userTally, compTally

    if userInput == "R": #User Inputs R for Rock

        if computerChoice == "R":
            print("The computer chose Rock")
            print("It's a Tie")
        elif computerChoice == "P":
            print("The computer chose Paper")
            print("Computer Won")
            compTally = compTally + 1
        elif computerChoice == "S":
            print("The computer chose Scissor")
            print("You Won")
            userTally = userTally + 1

    elif userInput == "P": #User Inputs P for Paper

        if computerChoice == "R":
            print("The computer chose Rock")
            print("You Won")
            userTally = userTally + 1
        elif computerChoice == "P":
            print("The computer chose Paper")
            print("It's a Tie")
        elif computerChoice == "S":
            print("The computer chose Scissor")
            print("Computer Won")
            compTally = compTally + 1

    elif userInput == "S": #User Inputs S for Scissor

        if computerChoice == "R":
            print("The computer chose Rock")
            print("Computer Won")
            compTally = compTally + 1
        elif computerChoice == "P":
            print("The computer chose Paper")
            print("You Won")
            userTally = userTally + 1
        elif computerChoice == "S":
            print("The computer chose Scissor")
            print("It's a Tie")
    return(userTally,compTally)

def tryCount(): #The number of tries....
    tryNum = 1
    while tryNum < 11:

        gameProcess()
        tryNum = tryNum + 1

tryCount()


print("You scored " + str(userTally))
print("The computer scored " + str(compTally))
if userTally > compTally:
    print("CONGRATULATIONS, YOU WON.")
elif userTally < compTally:
    print("Sorry, better luck next time.")
close = input()
if close == "Random Input.":
    exit()
else:
    exit()

