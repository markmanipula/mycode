#!/usr/bin/env python3

# The game is simple, all you need to do is figure out the different codes (0~9) and their position generated by game system. When the code is correct and in its position, then the system will give you (1A). If the code is correct but not in the right position, then the system will give you (1B). Game system will tell you how many(1A) or (1B) you got, right after your every guess.

#guess the 3 digit code to defeat the computer!

import random

print("Guess the 3-digit code to defeat the computer! If the guessed number is in the correct position its an A. If the guessed number is in the code but in the wrong position, its a B. Goal is to get 3 A's!")
print("Some rules to know: First number cant start at 0 \nThere are no repeating numbers")

#first number cant be 0. just how the rules are
firstNumber = random.randint(1,9)

#there will be no repeating numbers to guess so need a while loop
secondNumber = random.randint(0,9)
while firstNumber == secondNumber:
    secondNumber = random.randint(0,9)

#third number cant be the same as first and second number
thirdNumber = random.randint(0,9)
while thirdNumber == firstNumber or thirdNumber == secondNumber:
    thirdNumber = random.randint(0,9)

#testing to see if there are repeats
#testing output as well for easy coding
#print(f"{firstNumber} {secondNumber} {thirdNumber}")

keepPlaying = True
A = 0
B = 0
X = "No hit!"
invalidInput = True
numberOfTries = 0

while keepPlaying:

    #validates if user have a non number input for first number
    #the continue here serves the purpose of going back to its while loop
    while invalidInput:
        try:
            playerGuessFirstNumber = int(input("Enter first number\n>"))
            #based on the rules first nubmer cant start at 0
            #this will prevent the user to input 0
            if playerGuessFirstNumber <= 0 or playerGuessFirstNumber > 9:
                print("First number must be between 1 -9 inclusive")
                continue
            break
        except:
            print("Enter a valid first number")

    #validates if user have a non number input for second number
    while invalidInput:
        try:
            playerGuessSecondNumber = int(input("Enter second number\n>"))
            if playerGuessFirstNumber == playerGuessSecondNumber:
                print("You cant have repeating numbers!")
                continue
            if playerGuessSecondNumber < 0 or playerGuessFirstNumber > 9:
                print("Second number must be between 0 -9 inclusive")
                continue
            break
        except:
            print("Enter a valid second number")

    #validates if user have a non number input for third number
    while invalidInput:
        try:
            playerGuessThirdNumber = int(input("Enter third number\n>"))
            if playerGuessThirdNumber == playerGuessSecondNumber or playerGuessThirdNumber == playerGuessFirstNumber:
                print("You cant have repeating numbers!")
                continue
            if playerGuessThirdNumber < 0 or playerGuessThirdNumber > 9:
                print("Third number must be between 0 -9 inclusive")
                continue
            invalidInput = False
            break
        except:
            print("Enter a valid third number")

    numberOfTries += 1
    #goal of the game is to get all three numbers in the right order
    if firstNumber == playerGuessFirstNumber:
        A+=1
    if secondNumber == playerGuessSecondNumber:
        A+=1
    if(thirdNumber == playerGuessThirdNumber):
        A+=1
    if A == 3:
        keepPlaying = False
        print(f"Congratulations, you cracked the 3-digit code!\n>The numbers are {firstNumber}-{secondNumber}-{thirdNumber} \n>Number of tries: {numberOfTries}")    
        break

    if(firstNumber == playerGuessSecondNumber or firstNumber == playerGuessThirdNumber):
        B+=1
    if(secondNumber == playerGuessFirstNumber or secondNumber == playerGuessThirdNumber):
        B+=1
    if(thirdNumber == playerGuessFirstNumber or thirdNumber == playerGuessSecondNumber):
        B+=1

    if(A == 0 and B == 0):
        print(X)
    else:
        #this is the hint given
        print(f"Your input is {playerGuessFirstNumber}-{playerGuessSecondNumber}-{playerGuessThirdNumber} ---> {A}-A {B}-B")

    #reset the value of a and b to keep the hints accurate
    invalidInput = True
    A = 0
    B = 0

    #asks the user if they want to give up after 5 tries
    if numberOfTries >= 5:
        giveUp = input("Would you like to give up? Enter y to give up OR press any key and ENTER to continue\n>").lower()
        if giveUp == "y":
            print(f"The 3-digit code is: {firstNumber}-{secondNumber}-{thirdNumber}")
            break


