import random
import sys
import os
import json

def port(key, value, shift, pop):
    json_str = ""
    if isinstance(value, str):
        json_str += f'{shift}"{key}": "{value}"{pop}'
    elif isinstance(value, int) or isinstance(value, float):
        json_str += f'{shift}"{key}": {value}{pop}'
    elif isinstance(value, dict):
        value = json_stringify(value)
        json_str += f'{shift}"{key}": {value}{pop}'
    return json_str

def json_stringify(dict):
    json_str = ""

    for index, key in enumerate(dict):
        if index == 0:
            json_str += port(key, dict[key], '{', ', ')
        elif index == len(dict) - 1:
            json_str += port(key, dict[key], '', '}')
        else:
            json_str += port(key, dict[key], '', ', ')

    return json_str

d = {
    "test": "test",
    "test2": 1,
    "test3": "test3",
    "test4": {
        "test": "test",
        "test2": "test2",
        "test3": 2,
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
