# generate primes
# Author: Orla Woods

'''
'
primes = []

for candidate in range(2, 101): # for each number between 2 and 100
    print(candidate)
    isPrime = True # assume it's true
    for divisor in range(2, candidate):
 #check all numbers to see if they are prime
    # if the candidate is divisible by any number between 2 and the candidate itself, then it is not
    # a prime number
        if (candidate% divisor ==0):
            isPrime = False
            break # come out of the 4 loop
    if isPrime:
        primes.append(candidate)

print (primes)

'''

# above is not the most efficient way to do this, but it is the most readable. it is checking all of them

primes = []
upto = 100000

for candidate in range(2, upto): # for each number between 2 and 100
    print(candidate)
    isPrime = True # assume it's true
    # only need to check if divisible by prime 
    for divisor in primes:
        # if it is divisible by an int it in not a prime number 
        if (candidate % divisor == 0):
            isPrime = False
            # so there is no reason to keep checking
            break # come out of the 4 loop
    if isPrime:
        primes.append(candidate)

print (primes)