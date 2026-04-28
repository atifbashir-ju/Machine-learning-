# Data distribution: how to we get big data set?
# here noe we will create array containing 250 random floats between 0.0 to 5.0
import numpy as np
import matplotlib.pyplot as plt
Atif = np.random.uniform(0.0, 5.0, 250)
#visualization:
plt.hist(Atif, 5)
plt.show()

#big data distribution:
# now we will create an array with 1 lakh random numbers and display them
import numpy as np
import matplotlib.pyplot as plt
Atif = np.random.uniform(0.0, 5.0, 100000)
#visualization:
plt.hist(Atif, 100)
plt.show()
