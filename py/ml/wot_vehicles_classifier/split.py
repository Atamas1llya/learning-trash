import json
from sklearn.model_selection import train_test_split

wot_dataset = json.load(open('./datasets/wot_v2.json'))

data_x = wot_dataset['X']
data_y = wot_dataset['Y']

train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.5)

json.dump(train_x, open('./train_data/train_x.json', 'w'))
json.dump(train_y, open('./train_data/train_y.json', 'w'))
json.dump(test_x, open('./train_data/test_x.json', 'w'))
json.dump(test_y, open('./train_data/test_y.json', 'w'))
