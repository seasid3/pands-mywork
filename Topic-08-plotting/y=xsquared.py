# This program plots the function y=x**2
# Author Orla Woods

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints**2

plt.plot(xpoints, ypoints, color = "red")
plt.show()