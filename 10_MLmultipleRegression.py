# Multiple Regression: it is like a linera regression but with more than one independent value, meaning that we try to predict a value based on two or more other variables.

import pandas as pd
from sklearn import linear_model
df = pd.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)         
predictedCO2 = regr.predict(   [[2300, 1300]])
print(predictedCO2)

#coefficients this is a factor that describe the relationship with an uknown variable.
#here we will print the coefficient of the regression object..
import pandas as pd
from sklearn import linear_model
df = pd.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_)