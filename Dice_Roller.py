import random
def start():
    print("Do you want to roll a Dice?")
    print("Press 'Y' to continue")
    print("Press 'N' to exit")
    x = input()
    if x == "Y" :
        y = random.randint(1, 6)
        print("Your dice shows the number " + str(y))
        def restart():
            print("Do you want to play again")
            print("Press 'Y' to restart")
            print("Press 'N' to exit")
            restartQuery = input()
            if restartQuery =="Y":
                start()
            elif restartQuery == "N":
                exit()
            else:
                print("Invalid Input")
                restart()
        restart()
    elif x == "N":
        exit()
    else:
        print("Invalid Input")
        start()

start()

