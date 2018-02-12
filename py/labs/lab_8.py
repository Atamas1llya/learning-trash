import os
import sys
import json
import random

cache_path = './files/matrix.json'

def min_in_max(matrix):
    return min([max(column) for column in matrix]);

def random_matrix(rows, cols):
    return [[random.randint(1,101) for i in range(rows)] for j in range(cols)]

def save_matrix(matrix):
    open(cache_path, "w").write(json.dumps(matrix, indent=2))

def read_matrix():
    return json.load(open(cache_path))


# small test

try:
    matrix = random_matrix(5, 5)
    print('✅  Matrix created')

    save_matrix(matrix)
    print('✅  Matrix cached')

    cached_matrix = read_matrix()
    print('✅  Matrix cache retreived')

    print(f'✅  Minimal value of maximal col found: { min_in_max(cached_matrix) }')

except Exception as e:
    *rest, exc_tb = sys.exc_info()
    print(f'🛑  Error on line {exc_tb.tb_lineno}: {e}')
