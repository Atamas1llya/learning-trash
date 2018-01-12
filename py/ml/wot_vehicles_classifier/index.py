from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import fetcher
import processor
import normalizer
from knn import KNeighborsClassifier

raw_data = fetcher.fetchVehicles()
processed_data = processor.process(raw_data)
normalized_data_x = normalizer.normalize(processed_data["x"])

train_x, test_x, train_y, test_y = train_test_split(normalized_data_x, processed_data["y"], test_size=0.5)

classifier = KNeighborsClassifier(1)
classifier.fit(train_x, train_y)
predictions = classifier.predict(test_x)

print(accuracy_score(test_y, predictions))
