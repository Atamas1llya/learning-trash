import json
from knn import KNeighborsClassifier
from sklearn.metrics import accuracy_score

train_x = json.load(open('./__train_split__/train_x.json'))
train_y = json.load(open('./__train_split__/train_y.json'))
test_x = json.load(open('./__train_split__/test_x.json'))
test_y = json.load(open('./__train_split__/test_y.json'))

classifier = KNeighborsClassifier(1)
classifier.train(train_x, train_y)
predictions = classifier.predict(test_x)

print(accuracy_score(test_y, predictions))
