# this program puts 10 random numbers into a queue(list),
# Then outputs all the values in the queue,
# then takes the numbers from the queue one at a time, prints it and the current numbers in the queue.
# hte command pop(0) takes the first element from the list.
# Author: Orla Woods

import random

# Add 10 random numbers to the queue

queue = []
numberofnumbers = 10
rangeTo = 100

for n in range(0, numberofnumbers):
    queue.append(random.randrange(0,rangeTo)) # i went back to w3 schools to remind myself of the random function
print(f"Queue is {queue}") # this gives a list of 10 random numbers

while len(queue) != 0:
    currentNumber = queue.pop(0) # this goes through the list of numbers in the queue
    print(f"current Number is {currentNumber} and queue is {queue}") # this uses f-string
    # to print variables in strings. i.e. the current number and the queue after the number is removed

print("The queue is now empty") # this prints when the queue is empty

