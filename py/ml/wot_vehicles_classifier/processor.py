
import urllib.request
import json

APP_ID = '8ca40e4d4a53687d8e5fae2b3f772674'

raw_data = json.load(open('./datasets/wot_raw.json', 'r'))

# model:
# X: [spec_power, damage_per_shot, avg_armor, view_range]
# Y: [type]

data_x = []
data_y = []

def request_tmm(tank_id, engines, guns, suspensions, radios, turrets, **keys):
    tmm_url = f'https://api.worldoftanks.ru/wot/encyclopedia/vehicleprofile/?application_id={APP_ID}\
        &tank_id={tank_id}\
        &engine_id={engines}\
        &gun_id={guns}\
        &suspension_id={suspensions}\
        &radio_id={radios}'

    if isinstance(turrets, int):
        tmm_url += f'&turret_id={turrets}'

    tmm_res = urllib.request.urlopen(tmm_url)

    tmm_json = tmm_res.read().decode('utf-8')
    tmm = json.loads(tmm_json)
    if (tmm['status'] == 'ok'):
        tank_tmm = tmm['data'][f'{tank_id}']
        tank_x = []

        tank_x.append(int(tank_tmm['engine']['power'] / tank_tmm['weight'] * 1000))
        tank_x.append(tank_tmm['ammo'][0]['damage'][1])
        tank_x.append(int(((tank_tmm['armor']['hull']['front'] + tank_tmm['armor']['hull']['sides']) / 2)))
        tank_x.append(tank_tmm['turret']['view_range'])

        return tank_x, keys['type']
    else:
        return None, keys['type']

for vehicle in raw_data:
    tmm, type = request_tmm(**vehicle)
    print(tmm, type)
