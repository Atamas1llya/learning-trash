
import urllib.request
import json
import os.path

APP_ID = '8ca40e4d4a53687d8e5fae2b3f772674'
cache_folder = '__processor_cache__'

if not os.path.exists(cache_folder):
    os.makedirs(cache_folder)
    

def find_avg_dmg(ammo):
    return sum([item['damage'][1] for item in ammo]) / len(ammo)


def process_tmm(tmm):
    processed_tmm = [
        int(tmm['engine']['power'] / tmm['weight'] * 1000),
        find_avg_dmg(tmm['ammo']),
        int((tmm['armor']['hull']['front'] + tmm['armor']['hull']['sides'])),
        tmm['turret']['view_range'],
        tmm['gun']['reload_time'],
        tmm['suspension']['traverse_speed']
    ]

    return processed_tmm


def request_tmm(tank_id, engines, guns, suspensions, radios, turrets, **keys):
    query = f'&tank_id={tank_id}&engine_id={engines}&gun_id={guns}&suspension_id={suspensions}&radio_id={radios}'

    if isinstance(turrets, int):
        query += f'&turret_id={turrets}'

    cache_url = f'./{cache_folder}/{query}.json'

    if os.path.isfile(cache_url):
        file = open(cache_url, 'r')
        tmm_json = json.load(open(cache_url))
    else:
        tmm_res = urllib.request.urlopen(f'https://api.worldoftanks.ru/wot/encyclopedia/vehicleprofile/?application_id={APP_ID}{query}')
        tmm_json = tmm_res.read().decode("utf-8")

        file = open(cache_url, "w")
        file.write(json.dumps(tmm_json))

    tmm = json.loads(tmm_json)
    if (tmm["status"] == "ok"):
        return tmm["data"][f'{tank_id}']
    else:
        return None


def process(data):
    processed = { "x": [], "y": [] }

    for i, vehicle in enumerate(data):
        print(f'{i} / {len(data)}')

        tmm = request_tmm(**vehicle)

        if (tmm):
            processed_tmm = process_tmm(tmm)

            processed["x"].append(processed_tmm)
            processed["y"].append(vehicle["type"])

    return processed
