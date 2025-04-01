# This program will plot the frequncies of counties, first as a pie chart and then as a bar chart
# Author Orla Woods

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurrances
possibleCounties = ['Mayo', 'Sligo', 'Wicklow', 'Kildare', 'Dublin']
#pick 100 randomly from possible counties with the frequencies set up in p
counties = np.random.choice(
    possibleCounties, 
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

# we need the number of occurrences of each county, this returns a tuple of the unique values and how many times
# they appear
unique, counts = np.unique(counties, return_counts=True)
# we can not put this into a pie plot

# plt.pie(counts, labels = unique)
plt.bar(unique, counts)

plt.show()