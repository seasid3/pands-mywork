# lab3.2.4randomGenerator.py
# This program generates a random number between 1 and 10
# Author Orla Woods

import random
range = int(input ("Input the first number in a range: "))
range2 = int(input ("Input the end number in a range: "))
number = random.randint(range,range2)
print("Here is a random number: {}".format (number))

