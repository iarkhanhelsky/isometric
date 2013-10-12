from random import randint
import json
from functools import reduce

CELL_WITH = 16
CELL_HEIGHT = 8

COLORS = 255 * 255 * 255


def ij_to_xy(i, j):
    return 8 * (i + j), 4 * (j - i)


def randclr():
    return randint(0, 255 * 255 * 255)


def flatten(l):
    return reduce(list.__add__, [flatten(x) if isinstance(x, list) else [x] for x in l], [])


def parse_config(file):
    with open(file) as data:
        h = json.loads(data.read())

    return h

def merge(cfg_a, cfg_b):
    return