# lab3.1.5randomfruit.py
# This program prints out a random fruit
# Author Orla Woods

import random
fruits = ["pple", "banana", "raspberry", "strawberry", "orange", "kiwi", "grape", "mango", "peach"]
index = random.randint(0, len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))
