import json
import os.path
from sklearn.model_selection import train_test_split

cache_folder = '__train_split__'

if not os.path.exists(cache_folder):
    os.makedirs(cache_folder)

wot_dataset = json.load(open('./datasets/wot_v2.json'))

data_x = wot_dataset['X']
data_y = wot_dataset['Y']

train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.5)

json.dump(train_x, open(f'./{cache_folder}/train_x.json', 'w'))
json.dump(train_y, open(f'./{cache_folder}/train_y.json', 'w'))
json.dump(test_x, open(f'./{cache_folder}/test_x.json', 'w'))
json.dump(test_y, open(f'./{cache_folder}/test_y.json', 'w'))
