# import pandas
# # from sklearn import linear_model
# from sklearn.preprocessing import StandardScaler
# scale = StandardScaler()
#
# df = pandas.read_csv("file.csv")
#
# X = df[['Weight','Volume']]
#
# scaledX = scale.fit_transform(X)
#
# print(scaledX)

# PREDICT CO2 VALUES

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("file.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1300]])
print(scaled)

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
