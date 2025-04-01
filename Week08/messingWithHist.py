# messing with histograms
# Author Orla Woods

import numpy as np
import matplotlib.pyplot as plt

'''

np.random.seed(1) # it's actually pseudorandom
normData = np.random.normal(size = 10)

plt.hist(normData)

plt.show() # each time i run this the hist will be different as the numbers are generated each time
# unless i do above and see the random generator to be the same each time it's run
# wont appear normal until a lot of numbers in'
'''

# pie charts

fruit = np.array(['Apples', 'Orange', 'Banana'])
numbers = np.array([23, 77, 500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()