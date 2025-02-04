import numpy as np
import pandas as pd
import statsmodels.api as sm
import pickle

# Load data
data = pd.read_csv("/tmp/activationBase/activation_data.csv")
print(data.columns)
print("Data shape:", data.shape)

# Separate features and target variable
X = data.drop(columns=["Salary"], axis=1)
y = data["Salary"]

X = sm.add_constant(X, has_constant='add')
print("Shape of X after adding constant:", X.shape)

with open("/tmp/knowledgeBase/OLS/currentOlsSolution.pkl", "rb") as f:
    ols_model = pickle.load(f)

print("Shape of X:", X.shape)

predictions = ols_model.predict(X)

denormalized_price = predictions * (250000 - 350) + 350
print("Predicted Salary:", round(denormalized_price[0], 2))
