from random import randint
import json
from functools import reduce

CELL_WITH = 16
CELL_HEIGHT = 8

CELL_WITH_DIV_2 = CELL_WITH // 2
CELL_HEIGHT_DIV_2 = CELL_HEIGHT // 2

COLORS = 255 * 255 * 255


def ij_to_xy(i, j):
    return CELL_WITH_DIV_2 * (i + j), CELL_HEIGHT_DIV_2 * (j - i)


def randclr():
    return randint(0, 255 * 255 * 255)


def intersects(rect_a, rect_b):
    (x_a, y_a, w_a, h_a) = rect_a
    (x_b, y_b, w_b, h_b) = rect_b
    return (x_a < x_b + w_b) and (x_b < x_a + w_a) and (y_a < y_b + h_b) and (y_b < y_a + w_a)


def flatten(l):
    return reduce(list.__add__, [flatten(x) if isinstance(x, list) else [x] for x in l], [])


def parse_config(file):
    with open(file) as data:
        h = json.loads(data.read())

    return h
