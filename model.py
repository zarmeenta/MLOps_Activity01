import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

# Load and prepare the Iris dataset
iris_dataset = sns.load_dataset("iris")

# Shuffle the dataset
iris_dataset = iris_dataset.sample(frac=1, random_state=42).reset_index(drop=True)

X = iris_dataset.iloc[:, :4]
y = iris_dataset["species"]

# Combine features and target
train_iris = pd.concat([X, y], axis=1).reset_index(drop=True)
train_iris["distance"] = ''

class KNN:
    def __init__(self, k):
        self.k = k

    def distance(self, sepal_length, sepal_width, petal_length, petal_width, row):
        return np.sqrt(
            np.square(row['sepal_length'] - sepal_length) +
            np.square(row['sepal_width'] - sepal_width) +
            np.square(row['petal_length'] - petal_length) +
            np.square(row['petal_width'] - petal_width)
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
