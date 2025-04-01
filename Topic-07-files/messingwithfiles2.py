# this program will count the amount of times an external file is accessed and overwrite the new number each
# time it is opened
# Author: Orla Woods

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

# test it
# num = readNumber()
# print(num)

# take in a number and overwrite a file with that number (count.txt)

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
# writeNumber(25)

# main code
num = readNumber()
num += 1
print(f"we have run this program {num} times")
writeNumber(num)