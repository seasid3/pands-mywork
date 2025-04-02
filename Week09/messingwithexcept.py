# This program is to show you how you can use try except
# Author: Orla Woods

# filename = 'data.txt'
import sys

# print (sys.argv)
try:
    filename = sys.argv[1]
    print(filename)
    with open(filename) as fp:
        print(fp.read())
except IndexError as ie: # use the index error to catch where the wrror is in the code
    print("please ender the filename as an argumet")
   # print(ie)
# if i use try catch i dont see where the error is in the terminal
except FileNotFoundError:
    print(f"file {filename} not found, please enter a file that exists") 