# this program will read in a dict object from a file.
# Author: Orla Woods

import json
FILENAME = "testdict.json"

def readDict():
    # this will throw an error if the file does not exist
    # it should readly just retutn an empty dict
    # we can do this later
    with open(FILENAME) as f:
        return json.load(f)
    
# test the function
somedict = readDict()
print(somedict)
