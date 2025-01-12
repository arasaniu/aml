from sklearn.linear_model import LinearRegression

# Thorax data serves as input, abdomen data as target
def train_linear_model(thorax_data, abdomen_data):
    model = LinearRegression()
    model.fit(thorax_data, abdomen_data)
    return model
