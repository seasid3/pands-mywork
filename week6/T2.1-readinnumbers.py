# read in two numbers and multiply them together
# author: Orla Woods
# this uses the default. it is neater than defining code for num1, num 2 etc. and it's reuseable. 
# can put the top bit in a file and write the bottom bit from num1 = readNum()....

def readNum(message = "enter a number: "): # message defaults to this unless we say otherwise. see num2 below
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("that was not a number, ", end="") # keeps it on the same line
    return num

num1 = readNum()
num2 = readNum("enter num2: ")

answer = num1 * num2

print(f"answer is {answer}")