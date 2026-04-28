# Regression: the term regression is  used when you try to find the relationship between the variables. in ML and statiscal modeling that relationship is used to predict the outcome of the future events.

#linear Regression: it is basically uses the relationship between the data points  to draw a straight line through all of them, this line can be used to predict the future.

# How does it wroks:
import sys

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.scatter(x,y)
plt.show()

#now we will import scipy: it is for (scientific python) and draw theline of linear regression
import matplotlib.pyplot as plt
from scipy import stats
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86]
slope, intercept, r, p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


# R for relationship - it is very imp to know how the relationship between the variables x axis and y axis if there is no relationship then the linear regression cannot be used to predict anything. then this relationship is called R and an also known as the cofficient of corelation.
#the R value ranges from -1 to 1, where 0 means no relationship, 1 means a perfect positive relationship and -1 means a perfect negative relationship.

#know we will know how well does the data fit in a linear regression:
from scipy import stats
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86]
slope, intercept, r, p, std_err = stats.linregress(x,y)
print(r)

# predict future values: lets try to find the speed of 10 years old car.
from scipy import stats 
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86]
slope, intercept, r, p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
speed = myfunc(10)
print(speed)


# bad fit: lets create an example where linear regression does not fit the data well:
import matplotlib.pyplot as plt
from scipy import stats
x = [89, 43, 36, 36,95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40  ]
y = [21, 46, 3, 36, 67 ,95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

slope, intercept, r, p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()