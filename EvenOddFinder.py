#Even or Odd Number Finder.
def start():
    userInput = input("Please input your number:")
    userInput = int(userInput)
    if userInput %2 == 0:
        print("The number " + str(userInput) + " is Even.")
    else:
        print("The number " + str(userInput) + " is Odd.")
    def restart():
        print("Do you want to restart?")
        print("Y/N")
        restartornot = input()
        if restartornot == "Y":
            start()
        elif restartornot == "y":
            start()
        elif restartornot == "N":
            exit()
        elif restartornot == "n":
            exit()
        else:
            print("Invalid Input.")
            restart()
    restart()
start()