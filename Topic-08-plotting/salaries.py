# This program makes a list that has 10 random numbers between 20000-80000
# Author Orla Woods

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # so the same numbers are returned each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries) # random integers
print(salaries)

salariesPlus = salaries + 5000 # adds 5000 to each number

print(salariesPlus)

salariesMult = salaries * 1.05 # increases by 5%
newSalaries = salariesMult.astype(int) # as SalariesMult was float type array, it needs to be converted to int
print(newSalaries)