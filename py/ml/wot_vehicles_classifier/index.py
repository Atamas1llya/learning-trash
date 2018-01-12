import json
from knn import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


wot_dataset = json.load(open('./datasets/wot.json'))

data_x = wot_dataset['X']
data_y = wot_dataset['Y']

train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.5)

classifier = KNeighborsClassifier(1)
classifier.train(train_x, train_y)
predictions = classifier.predict(test_x)

print(accuracy_score(test_y, predictions))
