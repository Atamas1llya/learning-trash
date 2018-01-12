from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import fetcher
import processor
from knn import KNeighborsClassifier

raw_data = fetcher.fetchVehicles()
processed_data = processor.process(raw_data)

train_x, test_x, train_y, test_y = train_test_split(processed_data["x"], processed_data["y"], test_size=0.5)

classifier = KNeighborsClassifier(1)
classifier.fit(train_x, train_y)
predictions = classifier.predict(test_x)

print(accuracy_score(test_y, predictions))
