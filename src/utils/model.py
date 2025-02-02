import numpy as np
from sklearn.linear_model import LinearRegression

# Thorax data serves as input, abdomen data as target
def train_linear_model(thorax_data, abdomen_data):
    model = LinearRegression()
    model.fit(thorax_data, abdomen_data)
    return model

def create_lagged_features(signal, lags=3):
    lagged_features = np.hstack([np.roll(signal, shift=i) for i in range(lags)])
    return lagged_features
