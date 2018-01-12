# normalize data 0-1

def normalize(data):
    normalized = []

    for i in range(len(data[0])):
        col_min = min([item[i] for item in data])
        col_max = max([item[i] for item in data])

        for q, item in enumerate([item[i] for item in data]):
            if len(normalized) > q:
                normalized[q].append((item - col_min) / (col_max - col_min))
            else:
                normalized.append([])
                normalized[q].append((item - col_min) / (col_max - col_min))

    return normalized
