#percentile:
import numpy as np
ages = [5, 88, 89, 31, 43, 48, 50, 41, 11, 59, 67, 45 ,23 ,45, 56, 67, 23]
Atif = np.percentile(ages, 75)
print(Atif)

#what is the age of 90% people younger than?
import numpy as np
ages = [5, 88, 89, 31, 43, 48, 50, 41, 11, 59, 67, 45 ,23 ,45, 56, 67, 23]
Atif = np.percentile(ages, 90)
print(Atif)