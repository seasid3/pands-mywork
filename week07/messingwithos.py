# messing with the os module
# author Orla Woods

import os 

FILENAME = "messingwithfiles.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print (line, end = "")
else:
    print (FILENAME, "does not exist")


# os.remove("data2.txt")
