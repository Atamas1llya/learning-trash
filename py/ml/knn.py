import math
import numpy as np
from scipy.spatial import distance

X = [[0], [1], [2], [3]]
Y = [0, 0, 1, 1]


def euc(a, b):
    return distance.euclidean(a, b)


class KNeighborsClassifier:
    def train(self, train_x, train_y):
        self.train_x = train_x
        self.train_y = train_y

    def predict(self, test_x):
        predictions = []

        for X in test_x:
            label, nearest = self.find_nearest(X)
            predictions.append(label)

        # print(f'Nearest distance: {nearest}')
        return predictions

    def find_nearest(self, x):
        nearest_dist = euc(x, self.train_y[0])
        nearest_index = 0


        for index, train_x in enumerate(self.train_x):
            dist = euc(x, train_x)
            if (dist < nearest_dist):
                nearest_dist = dist
                nearest_index = index

        return self.train_y[nearest_index], nearest_dist


from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)


classifier = KNeighborsClassifier()
classifier.train(X_train, y_train)

predictions = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predictions))
