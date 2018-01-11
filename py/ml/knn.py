import math
import numpy as np
from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)


class KNeighborsClassifier:
    def __init__(self, k):
        self.k = k

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
        nearests = []

        for index, train_x in enumerate(self.train_x):
            dist = euc(x, train_x)
            if index < self.k:
                nearests.append([index, dist])
            else:
                if dist < max([item[1] for item in nearests]):
                    nearests.remove(max(nearests))
                    nearests.append([index, dist])

        rated_dist = []

        for i, item in enumerate(nearests):
            match_neigh = [self.train_y[item[0]] for item in nearests].count(self.train_y[item[0]])
            rated_dist.append([self.train_y[item[0]], item[1] / match_neigh])

        nearest_index = [item[1] for item in rated_dist].index(min([item[1] for item in rated_dist]))
        nearest_label = rated_dist[nearest_index]
        return nearest_label
