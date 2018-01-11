import math
import numpy as np
from scipy.spatial import distance

X = [[0], [1], [2], [3]]
Y = [0, 0, 1, 1]


def euc(a, b):
    return distance.euclidean(a, b)


class K1NeighborsClassifier:
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
