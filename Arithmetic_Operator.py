#This is my first try to make a arithmetic operator in Python...

def perform():# Perform the Operations...
    print("Please enter your choice. *Choices are case sensitive")
    print("Press 'A' for Addition")
    print("Press 'S' for Subtraction")
    print("Press 'M' for Multiplication")
    print("Press 'D' for Division")
    def conditions(): #Conditions...
        userinput = input()
        if userinput == "A":
            def addition(): #Addition
                x = float(input("Please enter the first number:"))
                y = float(input("Please enter the second number:"))
                z = x+y
                print("The sum of " + str(x) + " and " + str(y) + " gives " + str(z.__round__(2)))
            addition()
        elif userinput == "S":
            def subtraction(): #Subtraction
                x = float(input("Please enter the first number:"))
                y = float(input("Please enter the second number:"))
                z = x-y
                print("The difference between "+str(x)+ " and " +str(y)+ " is " +str(z.__round__(2)))
            subtraction()
        elif userinput == "M":
            def multiplication(): #Multiplication
                x = float(input("Please enter the Multiplicant:"))
                y = float(input("Please enter the Multiplier:"))
                z = x*y
                print("The product of " +str(x)+ " and " +str(y)+ " is " +str(z.__round__(2)))
            multiplication()
        elif userinput == "D":
            def division(): #Division
                x = float(input("Please enter the Divident:"))
                y = float(input("Please enter the Divisor:"))
                z = x/y
                print("The division of " +str(x)+ " by " +str(y)+ " gives" +str(z.__round__(2)))
            division()
        else:
            print("Invalid Input.")
    conditions()
    
def restartChoice():#Choices for restarting code...
    print("Do you want to restart?")
    print("Press 'Y' for Yes, or 'N' for No.")
    restart = input()
    if restart == "Y":
        perform()
        restartChoice()
    elif restart == "N":
        exit()
    else:
        print("Invalid Input.")
        print("Please enter the correct input.")
        restartChoice()

#Start of Code...
print("This is a Basic Arithmetic Operator")
print ("Do you want to perform Arithmetic Operations")
print("Please note that the choices are case-sensitive, please use CAPITAL letters,\n Thank You")
print("Press 'Y' for Yes, or 'N' for No.")
userwish = input()
if userwish == "Y":
    perform()
    restartChoice()
elif userwish == "N":
    exit()
else:
    print("Invalid Input.")
