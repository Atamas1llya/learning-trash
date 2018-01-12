
import urllib.request
import json

raw_data = json.load(open('./datasets/wot_raw.json', 'r'))

for vehicle in raw_data:
    print(vehicle)
