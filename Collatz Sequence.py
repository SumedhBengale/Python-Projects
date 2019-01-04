def collatz(userInput):
    while userInput != 1:
        if userInput %2 == 0:
            userInput = userInput // 2
            print(userInput.__round__(0))
        elif userInput %2 == 1:
            userInput = 3*userInput+1
            print(userInput.__round__(0))


strUserInput = input("Please enter a Number:")
userInput = int(strUserInput)
print("We are running Collatz Sequence.")
print("The following is the Collatz sequence for " + strUserInput +".")
collatz(userInput)
exitInput = input("")
