speed = [86, 87, 88, 86, 87, 85, 86]
#there are two types of SD: 1 Low Sd: 2 high SD.

#for low SD:
import numpy as np
speed = [86, 87, 88, 86, 87, 85, 86]
Atif = np.std(speed)
print(Atif)

#high SD:
import numpy as np
speed = [32, 111, 138, 28, 59, 77, 97]
Atif = np.std(speed)
print(Atif)


#varience
import numpy as np

data = [5, 7, 9]

variance = np.var(data)

print("Variance:", variance)