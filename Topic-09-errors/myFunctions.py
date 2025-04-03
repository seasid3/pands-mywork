# This program will define the function Fibonacci which takes a number and retuns a list containing
# a Fibonacci sequence of that many mumbers.
# Author Orla Woods

import logging
#logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number == 0:
        return []
    if number <0:
        raise ValueError('number must be > 0')
    
    a = 0
    b = 1
    fibonacciSequence = [0]
    # we have one in the list already so number - 1 times
    # this is not the most efficient code
    # could have used yield


    for i in range(1,number):
        fibonacciSequence.append(b)
        # this is funky code make a = b and b =  a+b
        a , b = b , a + b
   
    logging.debug("d: %s, %s", number, fibonacciSequence)
    return fibonacciSequence


return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]

assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'

try:
    fibonacci(-1)
except ValueError:
    # we want this exception to be thrown
    # so this is an example where we want to do nothing
    pass
else:
    # if the exception was not thrown we should throw
    # assertion error
    assert False, 'Fibonacci missing VlaueError'
    # or
    # raise AssertionError ('fibonacci no valueError')

if __name__ == "__main__":
    # tests will go here
    print("all good")