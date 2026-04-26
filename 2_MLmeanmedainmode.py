# in ML and also in maths there are basically 3 values that are actaully intrested to us:
#1 mean: the average value
#2 median: the mid point value
#3 mode: the most common value

#here in this example we have speed of 13 
#mean:
import numpy as np
Speed = [99, 86, 87, 88, 111, 86, 103, 87, 94 ,78, 77, 85, 86]
Atif = np.mean(Speed)
print(Atif)

#median:
import numpy as np
Speed = [99, 86, 87, 88, 111, 86, 103, 87, 94 ,78, 77, 85, 86]
Atif = np.median(Speed)
print(Atif)

#mode: the value that appears most number of time:
from scipy import stats
Speed = [99, 86, 87, 88, 111, 86, 103, 87, 94 ,78, 77, 85, 86]
Atif = stats.mode(Speed)
print(Atif)
