#normal data distribution: in numpy probability theory this kind of data dist os known as data dist. where the values are concentrated aroound a given value.
import numpy as np
import matplotlib.pyplot as plt
Atif = np.random.normal(5.0, 1.0, 100000)
plt.hist(Atif, 100)
plt.show()
