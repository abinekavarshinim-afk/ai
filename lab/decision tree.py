import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Outlook': [0, 0, 1, 2, 2, 2, 1, 0],
    'Temperature': [1, 1, 1, 2, 0, 0, 0, 2],
    'Humidity': [0, 0, 0, 0, 1, 1, 1, 0],
    'Wind': [0, 1, 0, 0, 0, 1, 1, 0],
    'Play': [1, 1, 0, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

# Input and output
X = df.drop('Play', axis=1)
y = df['Play']

# Create Decision Tree
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# Display tree
plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=X.columns,
          class_names=['No', 'Yes'],
          filled=True)

plt.show()

# Prediction
prediction = model.predict([[0, 1, 0, 0]])

print("Prediction:", prediction[0])
