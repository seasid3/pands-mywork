# This program generates 10 random numbers and prints out the top three.
# Author: Orla Woods

import random

# create a list of 10 random numbers
randomnumbers = [random.randint(0,101) for i in range(10)]

for i in range (0, 10):
    randomnumbers.append

print (f"10 random numbers: {randomnumbers}")

topones =randomnumbers
topones.sort(reverse=True)

print("The top 3 three are:", topones[:3])

#end 



