# Scale features: when your data has differnet alues and even the different measurement units, then it can be difficult to compare them. so the answer to this problem is scaling or scale features.
# there are two common methods for scaling features: normalization and standardization.
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pd.read_csv('cars2.csv')
x = df[['Weight', 'Volume']]
scaled_x = scale.fit_transform(x)
print(scaled_x)
#now with the above result we will predict the co2 emission.
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pd.read_csv('cars2.csv')
x = df[['Weight', 'Volume']]
y = df['CO2']
scaled_x = scale.fit_transform(x)
regr = linear_model.LinearRegression()
regr.fit(scaled_x, y)
scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
