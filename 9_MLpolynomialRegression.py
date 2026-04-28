# Polynmoial Regression: if your data point clearly will not fit a LR means (starught line) then it might be ideal for a polyniomial regression, it is a curve line that can fit the data points better than a straight line.
#it is also uses to find relationship b\w the variables x and y to find the best way to draw a line through data point.

#How does it works: here we will register 18 cars as they were passing through certain tollbooth
import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99]
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.show()

# now here we will import numpy and matplotlib and draw the line of polynomial regression:
import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99]
mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

#R - Squared: if there is no relationship b\w x and y then the polynomial regression cannot be used to predict anything, this relationship is called R-squared and it ranges from 0 to 1, where 0 means no relationship and 1 means a perfect relationship.
#python and the sklearn module will compute this value for us.
import numpy as np
from sklearn.metrics import r2_score
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99]
mymodel = np.poly1d(np.polyfit(x, y, 3))
print(r2_score(y, mymodel(x)))

#for predicting future values: here we will predict the speed of a car pasing at 17pm.
import numpy as np
from sklearn.metrics import r2_score
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99]
mymodel = np.poly1d(np.polyfit(x, y, 3))
speed = mymodel(17)
print(speed)

