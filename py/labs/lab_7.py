
def setValues(*names):
    values = [];

    for key in names:
        print(f"Input {key}:", end="")
        values.append(input())

    return values;

[x, y, z] = [float(item) if item else 0 for item in setValues("X", "Y", "Z")];

if x != 0 and y != 0 and z != 0:
    result = ((2 * x - 5.7 * z + z / x) / 3 * x) - ((3 * x + 5 * y - 2.5 * y / z) / (10 * pow(y, 2)))
    print(f"Result: {result:.2}")
else:
    print("Input error. The values must be greater than 0")
