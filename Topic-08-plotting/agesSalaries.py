# This program will make a list called ages, to go with salaries already determined
# and will plot a scatter plot of the same
# Author Orla Woods

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

minSalary = 20000
maxSalary = 80000
numberOfEntries = 1000 # increased no of salaries for better distrib
minAge = 21
maxAge = 65
numberAges = 1000 # increased no of ages for better distrib

np.random.seed(1) # so the same numbers are returned each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries) # random integers
ages = np.random.randint(minAge, maxAge, numberAges)
print(salaries, ages)

# scatter plot
plt.scatter(salaries, ages, color = "blue", label = "salaries")
plt.title("Salaries versus Ages")
# plt.show() 

# x squared line plot
xpoints = np.array(range(1,101))
ypoints = xpoints**2
plt.plot(xpoints, ypoints, color = "red", label = "x squared")

# hplotting a line of normal distrib based on salary data
# calculate the mean and SD of the salaries
mean_salary = np.mean(salaries)
std_salary = np.std(salaries)

# generate x-vlaues (range of values for normal distrib curve)
xmin, xmax = plt.xlim() # current x axis limits
x = np.linspace(xmin, xmax, 100)

# calculate the corresponding y-values for the normal distribution
normal_dist = stats.norm.pdf(x, mean_salary, std_salary)

#plot the normal distrib curve
plt.plot(x, normal_dist, 'k', label = "Normal Distribution Line", linewidth = 2)

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend()

# plt.show() # see both

plt.savefig('prettier-plot.png')
