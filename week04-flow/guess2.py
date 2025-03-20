# This programme prompts a user to enter a number and repeats unti the user gets it right. 
# The output will tell the user if they are too high or too low.
# Author: Orla Woods

'''
numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess > numberToGuess:
        print("Too High!")
    elif guess < numberToGuess:
        print("Too Low!")
    guess = int(input("Please guess again: "))

print ("well done! The number was", numberToGuess)'
'''
import random

numberToGuess = 30

randomnumber = random.randint(0,101)

print("The random numner is:", randomnumber)

while randomnumber != numberToGuess:
    if randomnumber > numberToGuess:
        print("Too High!")
    elif randomnumber < numberToGuess:
        print("Too Low!")
    randomnumber = random.randint(0,101)
    print("The random numner is:", randomnumber)

print ("well done! The number was", numberToGuess)