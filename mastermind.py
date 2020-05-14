import pygame
import time
import random

guesses = 0

#Possible Colors are red, yellow, blue, green, black, and white
colors = ["red", "blue", "yellow", "green", "black", "white"]
code = []
currentGuess = []


def selectRandomCode(colors):
    newcode=[]
    for i in range(0,4):
        x=random.randint(0,len(colors)-1)
        print(x)

        newcode.append(colors[x])
    return(newcode)


def checkGuess(secCode, myGuess):

    redPins = 0
    whitePins = 0

    for i in range(0,4):
        if secCode[i] == myGuess[i]:
            redPins = redPins + 1
            secCode[i] = "c"
            myGuess[i] = "g"





    return(redPins, whitePins)




code = selectRandomCode(colors)
print(code)



# Game Loop
# Computer selects random codecs


while guesses < 10:
    guess1 = input("Guess the first color: ")
    guess2 = input("Guess the second color: ")
    guess3 = input("Guess the third color: ")
    guess4 = input("Guess the fourth color: ")

    currentGuess = [guess1, guess2, guess3, guess4]

    if code == currentGuess:
        print("You win!!!")
        break


    else:

        print(checkGuess(code.copy(), currentGuess.copy()))
        print(code)
        print(currentGuess)

   # Check guess and respond with pins for player to use as clues

    print("Sorry, try again")



print("You ran out of guesses, you lose! The correct code was")
print(code)

    #make a guess

    #check to see if guess is correct - win if yes, continue if no

    #give feedback to guess


# Lose!

# ask to play again
