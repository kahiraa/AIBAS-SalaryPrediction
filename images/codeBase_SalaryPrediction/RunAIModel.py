import numpy
import pandas as pd
import tensorflow as tf
import keras
tf.config.set_visible_devices([], 'GPU')  # Disable GPU


activation_data = pd.read_csv("/tmp/activationBase/activation_data.csv")
print(activation_data.columns)
print("Activation data shape:", activation_data.shape)

activation_data = activation_data.drop(columns=["Salary"], axis=1)
print("Activation data shape:", activation_data.shape)

model = tf.keras.models.load_model("/tmp/knowledgeBase/currentAiSolution.keras", compile=False)
print("Model input shape:", model.input_shape)
activation_data = activation_data.to_numpy().reshape((-1, 14))

predictions = model.predict(activation_data)
denormalized_price = predictions * (250000 - 350) + 350
print("Salary", round(denormalized_price[0][0],2))