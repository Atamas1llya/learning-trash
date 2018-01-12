
import urllib.request
import json
import os.path

APP_ID = '8ca40e4d4a53687d8e5fae2b3f772674'

raw_data = json.load(open('./datasets/wot_raw_v2.json', 'r'))
cache_folder = '__tmcache__'

# model:
# X: [spec_power, damage_per_shot, avg_stun, siege, avg_armor, view_range, reload_time, traverse_speed]
# Y: [type]

data_x = []
data_y = []

def find_avg_dmg(ammo):
    sum = 0
    for item in ammo:
        sum += item['damage'][1]

    return sum / len(ammo)

def find_avg_stun(ammo):
    sum = 0
    for item in ammo:
        if item['stun']:
            sum += item['stun']['duration'][1]

    return sum / len(ammo)

def request_tmm(tank_id, engines, guns, suspensions, radios, turrets, **keys):
    url_link = f'&tank_id={tank_id}&engine_id={engines}&gun_id={guns}&suspension_id={suspensions}&radio_id={radios}'

    if isinstance(turrets, int):
        url_link += f'&turret_id={turrets}'

    if os.path.isfile(f'./{cache_folder}/{url_link}.json'):
        file = open(f'./{cache_folder}/{url_link}.json', 'r')
        tmm_json = json.load(open(f'./{cache_folder}/{url_link}.json'))
    else:
        tmm_res = urllib.request.urlopen(f'https://api.worldoftanks.ru/wot/encyclopedia/vehicleprofile/?application_id={APP_ID}{url_link}')
        tmm_json = tmm_res.read().decode('utf-8')


    if not os.path.isfile(f'./{cache_folder}/{url_link}.json'):
        file = open(f'./{cache_folder}/{url_link}.json', 'w')
        file.write(json.dumps(tmm_json))

    tmm = json.loads(tmm_json)
    if (tmm['status'] == 'ok'):
        tank_tmm = tmm['data'][f'{tank_id}']
        tank_x = []

        tank_x.append(int(tank_tmm['engine']['power'] / tank_tmm['weight'] * 1000))
        tank_x.append(find_avg_dmg(tank_tmm['ammo']))
        tank_x.append(find_avg_stun(tank_tmm['ammo']))
        # tank_x.append(int(bool(tank_tmm['siege'])))
        tank_x.append(int(((tank_tmm['armor']['hull']['front'] + tank_tmm['armor']['hull']['sides']))))
        tank_x.append(tank_tmm['turret']['view_range'])
        tank_x.append(tank_tmm['gun']['reload_time'])
        tank_x.append(tank_tmm['suspension']['traverse_speed'])

        return tank_x, keys['type']
    else:
        return None, keys['type']

for i, vehicle in enumerate(raw_data):
    print(f'{i} / {len(raw_data)}')
    tmm, type = request_tmm(**vehicle)
    if tmm and type:
        data_x.append(tmm)
        data_y.append(type)

data_obj = {
    "X": data_x,
    "Y": data_y
}

file = open('./datasets/wot_v2.json', 'w')
file.write(json.dumps(data_obj, indent=2))
