# This program keeps reading numbers until the user enters a 0.
# It then prints out each of the numbers entered and the average of them.
# Author: Orla Woods

numbers = []

# first number and then check if it is 0 in the while loop

number = int(input("enter number (0 to quit): ")) 
             
while number != 0:
    numbers.append(number)

# read the next number and check if it is 0)
    number = int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want the average to be a float

average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}.")

