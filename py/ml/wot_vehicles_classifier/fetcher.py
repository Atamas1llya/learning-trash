import urllib.request
import json
import os

cache_folder = '__fetcher_cache__'

if not os.path.exists(cache_folder):
    os.makedirs(cache_folder)


def fetchVehicles():
    query = '&tier=8,9,10'
    cache_url = f'{cache_folder}/{query}.json'
    if os.path.isfile(cache_url):
        return json.load(open(cache_url))

    else:
        wot_res = urllib.request.urlopen(
            f'https://api.worldoftanks.ru/wot/encyclopedia/vehicles/?application_id=8ca40e4d4a53687d8e5fae2b3f772674{query}'
        ).read().decode('utf-8')
        wot_data_raw = json.loads(wot_res)['data']

    required_keys = [
        'type', 'tier', 'engines', 'turrets',
        'suspensions', 'guns', 'radios', 'tank_id'
    ]
    wot_data = []

    for index, item in enumerate(wot_data_raw):
        wot_data.append({})
        for key in wot_data_raw[item].keys():
            if key in required_keys:
                if isinstance(wot_data_raw[item][key], list) and len(wot_data_raw[item][key]) > 0:
                    wot_data[index][key] = wot_data_raw[item][key][-1]
                else:
                    wot_data[index][key] = wot_data_raw[item][key]

    file = open(cache_url, "w")
    file.write(json.dumps(wot_data))

    return wot_data
