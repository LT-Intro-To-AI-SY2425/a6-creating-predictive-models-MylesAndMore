import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print(x)
print(y)

# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler().fit(x)

# Step 3: Transform the data
x = scaler.transform(x)

# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Step 5: Create a LogsiticRegression object and fit the data
model = linear_model.LogisticRegression().fit(x_train, y_train)

# Step 6: Fit the data
model.fit(x_train, y_train)

# Step 7: Print the score to see the accuracy of the model
print(f"Accuracy: {model.score(x_test, y_test)}")

# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
predict = model.predict(x_test)
print(f"Predicted: {predict}")
print(f"Actual: {y_test}")

# Would a 34 year old Female who makes 56000 a year buy an SUV according to the model?
print(f"34F/$56K: {model.predict(scaler.transform([[34, 56000, 1]]))}")
