# this program will show that variables can be of type function, and we can call those
# variables
# Author: Orla Woods

def fun1():
    print("this is fun1")
def fun2(): 
    print("this is fun2")

whichFun = fun1
whichFun()
whichFun = fun2
whichFun()

