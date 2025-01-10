import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(model.coef_[0], 2)
intercept = round(model.intercept_, 2)
rsq = round(model.score(x, y), 2)

# Print out the linear equation and r squared value
print(f"y = {coef}x + {intercept}")
print(f"R^2 = {rsq}")

# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction
x_predict = 43
prediction = model.predict([[x_predict]])
print(f"Predicted blood pressure: {prediction[0]}")

# Create the model in matplotlib and include the line of best fit
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue')
plt.scatter(x_predict, prediction, color='purple')
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure vs Age")
plt.plot(x, coef * x + intercept, c='red', label='Best Fit')
plt.legend()
plt.show()
