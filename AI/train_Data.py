import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
df = pd.read_csv("dataset.csv")


# Split the data into features and target variable
y = df[["Water"]]
x = df.drop("Water", axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
# Train the model
model = RandomForestRegressor(random_state=0)
model.fit(x_train, y_train)

# Save the model to a file
joblib.dump(model, "trained_model.pkl")

y_pred = model.predict(x_test)
print("the lower mse the better")
print("mse = ", mse(y_pred, y_test))
