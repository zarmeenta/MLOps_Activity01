import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# Load and prepare the Iris dataset using scikit-learn
iris = load_iris()
iris_dataset = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_dataset['species'] = iris.target

# Map target numbers to species names for easier understanding
species_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
iris_dataset['species'] = iris_dataset['species'].map(species_names)

# Shuffle the dataset
iris_dataset = iris_dataset.sample(frac=1, random_state=42).reset_index(drop=True)

X = iris_dataset.iloc[:, :-1]
y = iris_dataset["species"]

# Combine features and target
train_iris = pd.concat([X, y], axis=1).reset_index(drop=True)
train_iris["distance"] = ''

class KNN:
    def __init__(self, k):
        self.k = k

    def distance(self, sepal_length, sepal_width, petal_length, petal_width, row):
        return np.sqrt(
            np.square(row['sepal length (cm)'] - sepal_length) +
            np.square(row['sepal width (cm)'] - sepal_width) +
            np.square(row['petal length (cm)'] - petal_length) +
            np.square(row['petal width (cm)'] - petal_width)
        )

    def predict(self, sepal_length, sepal_width, petal_length, petal_width):
        for i in range(len(train_iris)):
            train_iris.loc[i, "distance"] = self.distance(
                sepal_length, sepal_width, petal_length, petal_width, train_iris.iloc[i]
            )
        sorted_df = train_iris.sort_values(by="distance")
        first_k = sorted_df.head(self.k)
        mode_result = first_k['species'].mode()
        return mode_result[0]
