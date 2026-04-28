#scatter plot: A scatter plot is a diagram where each value in the data set represented by the dots. it basically needs two array of the same length, one for the x coordinates and one for the y coordinates.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()