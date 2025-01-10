import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.around(model.coef_, 2)
intercept = np.around(model.intercept_, 2)
rsq = np.around(model.score(x, y), 2)

print(f"y = {coef[0]}miles + {coef[1]}age + {intercept}")
print(f"R^2 = {rsq}")

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")

for i in range(len(xtest)):
    print(f"Miles: {xtest[i][0]}, Age: {xtest[i][1]}")
    predict = np.around(model.predict([xtest[i]]), 2)
    print(f"Predicted: {predict[0]}, Actual: {ytest[i]}")

# What does the model predict a 10-year-old car with 89000 miles is worth?
# What about a car that is 20 years old with 150000 miles?

print("***************")
print("Predictions")

print(f"10-year-old car with 89000 miles: {model.predict([[89, 10]])[0]}")
print(f"20-year-old car with 150000 miles: {model.predict([[150, 20]])[0]}")
