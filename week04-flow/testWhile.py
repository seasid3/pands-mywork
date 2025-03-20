# Messinf with while loops
# Author: Orla Woods

# while condition:
#       statements
#
# two types
# Counter controlled loop
#      we usually use for loops for counter controlled loops
# Sentinel controlled loop
#      if you are reading in from a user, one pattern is read in from the user, check the while
#      and then read again in the body of the while loop
# Be careful of infinite loops
#      MAKE SURE YOU MODIFY WHAT YOURE CHECKING

# Example of a counter controlled loop

count = 0
while (count < 10):
      print ("count is", count)  
      count = count + 1 

print ("at the and count is ", count)

count  = 10
while count >= 0:
       print ("countdown", count)
       count -= 1 
print ("Blast off!")

# Example of a sentinel controlled loop

val = input("type something (q to quit):")
while val != "q":
       print ("Hi Mum")
       val = input("q to quit:")

print("all done")

