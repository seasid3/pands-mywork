# isEven.py
# a program to ask if a number is even or odd and give even or odd
# as an output
# Author: Orla Woods



''' 
# first code, enter an integer

number = int(input("enter an integer:"))

if (number % 2) == 0:
    print(f"{number} is an even number")
else: 
    print  (f"{number} is an odd number")
'''

'''
# next code enter a float, round this and then see if it is even
# or odd and output even or odd

number = float(input("enter a number:"))

roundnumber = round(number)
print (f"Rounded to the nearest whole number this is: {roundnumber}")

if (roundnumber % 2) == 0:
    print(f"{roundnumber} is an even number")
else: 
    print  (f"{roundnumber} is an odd number")

'''
# this code uses a loop to define that if a condition is not met
# it will keep asking until the correct condition calls for a break

number = int(input("enter an integer that is less than ten:"))

while number >= 0:
    anothernumber = int(input("enter another integer that is less than ten:"))

    if anothernumber == -1:
         break

print("The number IS -1!")

if (anothernumber % 2) == 0:
    print(f"{anothernumber} is an even number")
else: 
    print  (f"{anothernumber} is an odd number")

'''
if (number % 2) == 0:
    print(f"{number} is an even number")
else: 
    print  (f"{number} is an odd number")
'''