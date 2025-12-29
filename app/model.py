from sklearn.linear_model import LogisticRegression
import numpy as np

class Model:
    def __init__(self):
        self.model = LogisticRegression()
        # Simple dummy data for training
        X_train = np.array([[1], [2], [3], [4], [5], [6]])
        y_train = np.array([0, 0, 0, 1, 1, 1])
        self.model.fit(X_train, y_train)

    def predict(self, data):
        return self.model.predict(data).tolist()

model = Model()
