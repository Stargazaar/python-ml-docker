from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

class Model:
    def __init__(self):
        self.model = LogisticRegression(max_iter=200)
        iris = load_iris()
        X, y = iris.data, iris.target
        self.model.fit(X, y)
        self.class_names = iris.target_names.tolist()

    def predict(self, data):
        predictions = self.model.predict(data).tolist()
        return [self.class_names[p] for p in predictions]

model = Model()
