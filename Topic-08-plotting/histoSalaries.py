# This program will plot a histogram of the previously determined salaries (part 1 of this lab)
# Author Orla Woods

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # so the same numbers are returned each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries) # random integers
print(salaries)

plt.hist(salaries, color = "blue")
plt.title("Salaries")
plt.show()

