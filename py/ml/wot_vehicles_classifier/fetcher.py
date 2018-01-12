import urllib.request
import json

def fetchVehicles():
    wot_res = urllib.request.urlopen('https://api.worldoftanks.ru/wot/encyclopedia/vehicles/?application_id=8ca40e4d4a53687d8e5fae2b3f772674')
    wot_data_json = wot_res.read().decode('utf-8')
    wot_data_raw = json.loads(wot_data_json)['data']

    required_keys = ['type', 'tier', 'engines', 'turrets', 'suspensions', 'guns', 'radios', 'tank_id']
    wot_data = []

    for index, item in enumerate(wot_data_raw):
        wot_data.append({})
        for key in wot_data_raw[item].keys():
            if key in required_keys:
                if isinstance(wot_data_raw[item][key], list) and len(wot_data_raw[item][key]) > 0:
                    wot_data[index][key] = wot_data_raw[item][key][-1]
                else:
                    wot_data[index][key] = wot_data_raw[item][key]

    return wot_data
