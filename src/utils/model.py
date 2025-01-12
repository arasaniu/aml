import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Thorax data serves as input, abdomen data as target
def train_linear_model(thorax_data, abdomen_data):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# # Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(
#     thorax_data, abdomen_data, test_size=0.2, random_state=42
# )

# Initialize and train the linear regression model
# model = train_linear_model(X_train, y_train)

# Predict on the test set
abdomen_prediction = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error on Test Set: {mse:.4f}")

# Save the trained model for later use
import joblib
joblib.dump(model, "linear_regression_model.pkl")

# Example usage: Predict maternal signal for new thoracic data
# new_thorax_data = np.array([[0.5, -0.3], [0.2, -0.1]])  # Replace with actual test data
# maternal_prediction = model.predict(new_thorax_data)
# print("Predicted Maternal Signal:", maternal_prediction)
