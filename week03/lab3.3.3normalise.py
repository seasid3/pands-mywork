# lab3.3.3normalise.py
# This program reads a string and strips any leading or trailing spaces. 
# It also converts all letters to lower case.
# It then outputs the length of the original string and the normalised string.
# author: Orla Woods

rawstring = input("Please enter a string: ")
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len(rawstring)
lengthofnormalisedstring = len(normalisedstring)

print(f"That string normalised is: {normalisedstring}")
print(f"We reduced the input string from {lengthofrawstring} to {lengthofnormalisedstring} characters.")   

