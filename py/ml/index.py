from knn import KNeighborsClassifier
from knn_exp import KNeighborsClassifierExp
from k1nn import K1NeighborsClassifier


from sklearn import datasets
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

knn = KNeighborsClassifier(4)
knn_exp = KNeighborsClassifierExp(4)

knn.train(X_train, y_train)
knn_exp.train(X_train, y_train)
predictions = knn.predict(X_test)
predictions_exp = knn_exp.predict(X_test)

print(accuracy_score(y_test, predictions))
print(accuracy_score(y_test, predictions_exp))
