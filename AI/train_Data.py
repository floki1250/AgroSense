import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('dataset.csv')

# Preprocess the data
# ...

# Split the data into features and target variable
X = data[['Temperature', 'Humidity','Label']]
y = data['Water']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'model.pkl')
