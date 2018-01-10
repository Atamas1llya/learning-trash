import json

def value_to_json(value, indentation, indent_char):
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, int) or isinstance(value, float):
        return value
    elif isinstance(value, dict):
        return json_stringify(value, indentation + indent_char, indent_char)
    else:
        raise ValueError(f'Unsupported type: {type(value)}')

def punctuate(chunk, index, json_size, indentation):
    if index == 0:
        return f'{{\n{indentation}{chunk},\n'
    elif index == json_size - 1:
        return f'{indentation}{chunk}\n{indentation}}}'
    else:
        return f'{indentation}{chunk},\n'

def json_stringify(dict, indentation, indent_char=""):
    if not indent_char: indent_char = indentation

    json_str = ""

    for index, key in enumerate(dict):
        json_value = value_to_json(dict[key], indentation, indent_char or indentation)
        json_chunk = f'"{key}": {json_value}'
        json_str += punctuate(json_chunk, index, len(dict), indentation)

    return json_str

d = {
    "test": "test",
    "test2": 1,
    "test3": "test3",
    "test4": {
        "test": "test",
        "test2": "test2",
        # "test3": [1, 2, 3],
        # "test4": (1, 2, 3),
        "test5": {
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
json_file.write(json_stringify(d, '\t'))
