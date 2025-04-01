# messing with numpy
# Author Orla Woods

import numpy as np # it's already installed in anaconda

list_of_number = [1,2,3,5, "asdf"] # a list so can have different types, has commas between the list items in output
print("list", list_of_number) # cant add a number here, can only combine lists i.e. [1,2,3,4] + [3]

numbers = np.array([1,2,3,4]) # cant have different types. output changed them to strings if numbers and strings
# numbers = numbers + 3 # adds to each number
numbers = numbers * [1,2,3,5] # multiplies 1 x 1, 2x 2, 3x3 and 4x5
print("array", numbers)

rando = np.random.randint(100, 200, 30) # 30 random nos between 100 and 200
print(rando)

normalrando = np.random.normal(loc = 50, scale = 20, size = 100) # 100 numbers normal distribution, mean is loc, scale 
# check w3 schools
print(normalrando)
