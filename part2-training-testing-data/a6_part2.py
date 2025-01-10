import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1, 1)

# Create the model
model = LinearRegression().fit(xtrain, ytrain)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(model.coef_[0], 2)
intercept = round(model.intercept_, 2)
rsq = round(model.score(xtrain, ytrain), 2)

# Print out the linear equation and r squared value:
print(f"y = {coef}x + {intercept}")
print(f"R^2 = {rsq}")

'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
x = x.reshape(-1, 1)

# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(x)

# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)

# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for i in range (len(xtest)):
    print(f"[{xtest[i]}] Predicted: {predict[i]}, Actual: {ytest[i]}")

'''
**********CREATE A VISUAL OF THE RESULTS**********
'''

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue')
plt.scatter(xtest, ytest, color='purple')
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure vs Age")
plt.plot(x, coef * x + intercept, c='red', label='Best Fit')
plt.legend()
plt.show()
