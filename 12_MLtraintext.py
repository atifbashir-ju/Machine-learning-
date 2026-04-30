# in ML we ceeate a model to predict outcome, to measure of the mode; is good enough or need to rectify , then we use a method called tarin test:
#what is train test?
#In machine learning, train-test (often called train-test split) is a basic concept used to check how well your model actually works.

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
Atif1 = np.random.normal(3, 1, 100)
Atif2 = np.random.normal(150, 40, 100)/Atif1
plt.scatter(Atif1, Atif2)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
plt.scatter(train_x, train_y)
plt.show()

#testing set:

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
plt.scatter(test_x, test_y)
plt.show()


#what abbout fit the data set.
#here we will draw a polynoial regression line to fit the data set.

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
myline = np.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
