# more messing with functions
# variable scope
# Author: Orla woods

# when a variable is defined in a code block it is not visible outside that code block

# dont use global variable

x = 999

def fun(num):
    print(num)

def fun2(x): # this x is different to the x in x=999. so dont use x, define it better, better names. the scope
    #of this x is just within this indented section
    print(f"in fun2 x {x}")
    x = 21 # this x=21 does not affect the x=999
    print(f"in fun2 x {x}")

fun2(x)
print(f"in fun2 x is {x}")

# python will let you use two variables with the same name but this isnt a good idea

# variables have scope just with inside the function
# do not define variables in a function the same as the outside.
# think of a function as a black box. define it and then return a value. dont try to do it globally. 
# it's bad practice. 