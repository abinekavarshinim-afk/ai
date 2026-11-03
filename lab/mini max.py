import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Input dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Output dataset (XOR)
y = np.array([[0],
              [1],
              [1],
              [0]])

# Create Feed Forward Neural Network
model = Sequential()

# Input and hidden layers
model.add(Dense(4, input_dim=2, activation='relu'))

# Output layer
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Test the model
predictions = model.predict(X)

# Display output
print("Predictions:")
for i in range(len(X)):
    print(X[i], "=", round(float(predictions[i][0])))

print("Accuracy:", model.evaluate(X, y, verbose=0)[1] * 100, "%")
