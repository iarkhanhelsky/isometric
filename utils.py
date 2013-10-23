from random import randint
import json
from functools import reduce

CELL_WITH = 32
CELL_HEIGHT = 16

CELL_WITH_DIV_2 = CELL_WITH // 2
CELL_HEIGHT_DIV_2 = CELL_HEIGHT // 2

COLORS = 255 * 255 * 255


def ij_to_xy(i, j):
    return CELL_WITH_DIV_2 * (i + j), CELL_HEIGHT_DIV_2 * (j - i)


def randclr():
    return randint(0, 255 * 255 * 255)


def flatten(l):
    return reduce(list.__add__, [flatten(x) if isinstance(x, list) else [x] for x in l], [])


def parse_config(file):
    with open(file) as data:
        h = json.loads(data.read())

    return h
