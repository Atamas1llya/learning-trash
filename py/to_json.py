import json

def value_to_json(value):
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, int) or isinstance(value, float):
        return value
    elif isinstance(value, dict):
        return json_stringify(value)
    else:
        return '"UNSUPPORTED"'

def punctuate(chunk, index, json_size, indentation):
    if index == 0:
        return f'{{{chunk},'
    elif index == json_size - 1:
        return f'{chunk}}}'
    else:
        return f'{chunk},'

def json_stringify(dict):
    json_str = ""

    for index, key in enumerate(dict):
        json_value = value_to_json(dict[key])
        json_chunk = f'"{key}": {json_value}'
        json_str += punctuate(json_chunk, index, len(dict), False)

    return json_str

d = {
    "test": "test",
    "test2": 1,
    "test3": "test3",
    "test4": {
        "test": "test",
        "test2": "test2",
        "test3": (1, 2, 3),
        "test4": {
            "test": "test",
            "test2": "test2",
            "test3": 3,
            "test4": {
                "test": 4.2,
                "test2": "test2",
                "test3": "test3",
            }
        }
    }
}

json_file = open('json_data.json', 'w')
json_file.write(json_stringify(d))
