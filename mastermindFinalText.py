import pygame
import time
import random
import sys

#Set max number of guesses and initial guess count
maxGuesses = 10
guesses = 0

#Possible Colors are red, yellow, blue, green, black, and white
colors = ["red", "blue", "yellow", "green", "black", "white"]

#Set blank lists for secret code and current guess
code = []
currentGuess = []

#Function to create and return secret code
def selectRandomCode(colors):
    newcode=[]
    for i in range(0,4):
        x=random.randint(0,len(colors)-1)
        print(x)

        newcode.append(colors[x])
    return(newcode)

#Function to take the current guess and the secret code and return number of correct pegs, and correct colors in incorrect locations.
def checkGuess(secCode, myGuess):

    redPins = 0
    whitePins = 0

    for i in range(0,4):
        if secCode[i] == myGuess[i]:
            redPins = redPins + 1
            secCode[i] = "c"
            myGuess[i] = "g"
        print(secCode)
        print(myGuess)

    for i in range(0,4):
        for j in range(0,4):
            if i != j:
                if myGuess[i] and secCode[j] != "c" or "g" or "pc" or "pg":
                    if myGuess[i] == secCode[j]:
                        whitePins = whitePins + 1
                        secCode[j] = "pc"
                        myGuess[i] = "pg"
            print (i,j)
            print(secCode)
            print(myGuess)

    return(redPins, whitePins)

code = selectRandomCode(colors)

while guesses < 10:
    guess1 = input("Guess the first color: ")
    guess2 = input("Guess the second color: ")
    guess3 = input("Guess the third color: ")
    guess4 = input("Guess the fourth color: ")

    currentGuess = [guess1, guess2, guess3, guess4]

    if code == currentGuess:
        print("You win!!!")
        sys.exit()

    else:

        print(checkGuess(code.copy(), currentGuess.copy()))

    print("Sorry, try again")

print("You ran out of guesses, you lose! The correct code was")
print(code)
