# This programme prompts a user to enter a number and repeats unti the user gets it right
# Author: Orla Woods

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print("Wrong!")
    guess = int(input("Please guess again: "))

print ("well done! The number was", numberToGuess)


