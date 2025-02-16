# lab3.1.3div.py
# This program reads in two numbers, divides
# the first number by the second and outputs the integer and the remainder
# Author Orla Woods

x = int(input ("Enter first number: "))
y = int(input ("Enter second number: "))
answer = int(x / y) # // gives the integer division
remainder = x % y # gives the remainder
print("{} divided by {} is {} with remainder {}". format(x, y, answer, remainder))
