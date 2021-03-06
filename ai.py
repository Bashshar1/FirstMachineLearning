# -*- coding: utf-8 -*-
"""Ai

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WMT6hJ_JFs-6FVXYjW7jZzcbuTuLcHZJ
"""

import tensorflow
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

# Input data
celsius = [-40, -10,  0,  8, 15, 22, 38]

# Desired output data
fahrenheit = [-40, 14, 32, 46, 59, 72,  100]

# Dense represents a fully connected layer (i.e. every input is 
# connected to every output by a weight)
layer_0 = Dense(1)

# Assemble layers into a model (neural network)
model = Sequential()
model.add(layer_0)
# Compile the model
model.compile(Adam(0.1), mean_squared_error)
model.fit(celsius,fahrenheit,epochs=100)
# Now we're able to test values for the network
string = input("Enter a celsius value to test: ")

while string != "exit":
    # Prepare the testing data
    inputData = [int(string)]
    
    # Put this data through the model
    prediction = model.predict(inputData)
    
    # Print the result
    print(prediction)
    
    # Prompt for another value
    string = input("Enter a value to test: ")

