# this program will initialise the file 
# author Orla Woods

import os.path

FILENAME = "count.txt"

def writeNumber(number):
    with open(FILENAME, 'w') as f:
         f.write(str(number)) # write the number to the file

if not os.path.isfile(FILENAME):
    print ("File does not exist")
    #initilize file here
    writeNumber(0) # initialize the file with 0

def readNumber():
    try: 
        with open (FILENAME) as f:
            number = int(f.read()) # read the number and convert to an integer
            return number
    except IOError: # if any I/O error
        # this file will be created when we write bacck.
        # no file assumes first time running
        # ie 0 previous runs
        print("Error reading that file.")
        return 0
    
# test readNumber function
number = readNumber()
print(f"the number read from file is: {number}")

