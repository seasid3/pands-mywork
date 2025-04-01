# Messing with functions
# to demonstrate the deining and using functions
# Author: Orla Woods

# x, y, z = (1, 2, 3)
# print(x, y, z, sep="", end="") # end means new line, sep is elements sepatated by. sep and 
# end are arguments we pass in
# print (f"{x}-{y}-{z}")
# print(1,2,3)

def toPower(number, power=3):   # the default power here is 3 if a power isnt added in below
    return(number**power)

# ans = cube(2)
# print(f"we got {ans}")
num = 10

print(f"and {num} is {toPower(num,2)}") #power here is the 2 value. 
