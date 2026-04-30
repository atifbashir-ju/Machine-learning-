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
