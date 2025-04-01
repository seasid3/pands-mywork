# messing with matplotlib
# author Orla Woods

import numpy as np
import matplotlib.pyplot as plt 

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = "x squared")
plt.plot(xpoints, xpoints, label = "straight", color = "blue")


# plt.savefig("Lecture1.png")

# need to close the plot to stop the program running
# image saves as a png if you save it. will see it in the same dir as the code

#scatterplot

randompoints = np.random.randint(1, 1000, 100) # 100 values btwn 1 and 1000
plt.scatter(xpoints, randompoints, label = "random")

plt.legend()
plt.show() # to show. it is made at this point so have at the end