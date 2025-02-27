# testif.py
# Program to show the format of an if statement

# format of an if statement
#if condition:
#   statements

# if condition:
#    statements (if true)
# else:
#    statements (if false)

# if conditinon1:
#    statements (if true)
# elif condition2:
#    statements (if condition 1 is false but 2 is true)
# else:
#    statements (if both false)

# Author: Orla Woods

b = 1 
if True: 
    print("we are in the if statement")
    b = 2
print("sanity", b)

c = 1
if isinstance(c, int) and c == 1:
    print ("c is one")
else:
    print ("c is not one")



d = 10
if not isinstance(d, int):
    print ("please give me an int")
elif d < 0:
    print ("d is negative") 
elif d >= 10:
    print ("d is 10 or higher")
else: 
    print ("d is between 0 and 9 (inclusive)")

print("sanity", b)





