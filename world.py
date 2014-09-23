from pygame.rect import Rect
from utils import randclr, intersects
from random import randint
from rules import rule


def new_object(rows, cols, height):
    return (0, 0, randint(*rows), randint(*cols), 0), randint(*height), randclr()


def place(obj, at):
    ((i, j, rows, cols, lev), height, color) = obj
    return at + (rows, cols, lev), height, color


def populate(n, rows, cols):
    return [place(obj, (randint(0, rows), randint(0, cols))) for obj in
            [new_object((2, 8), (2, 8), (20, 50)) for _ in range(n)]]


def cmp_objects(a, b, max_rows):
    ((ai, aj, ar, ac, _), _, _) = a
    ((bi, bj, br, bc, _), _, _) = b
    if Rect((ai, aj, ar, ac)).contains(bi, bj, br, bc):
        return -1
    elif Rect(bi, bj, br, bc).contains(ai, aj, ar, ac):
        return 1
    else:
        return rule(ai + ar, aj, max_rows) - rule(bi + br, bj, max_rows)


def road_populate(w, stop_rows, stop_cols, i0, j0, rows, cols):
    if (rows - i0) > stop_rows and (cols - j0) > stop_cols:

        horizontal = randint(0, 1)
        if horizontal:
            i = randint(i0, rows - 1)
            road = (i, j0, 1, cols)
            for j in range(j0, cols):
                w[i][j] = 1
            return [road_populate(w, stop_rows, stop_cols, i0, j0, i, cols),
                    road_populate(w, stop_rows, stop_cols, i + 1, j0, rows, cols), road]
        else:
            j = randint(j0, cols - 1)
            road = (i0, j, rows - 1, 1)
            for i in range(i0, rows):
                w[i][j] = 1
            return [road_populate(w, stop_rows, stop_cols, i0, j0, rows, j),
                    road_populate(w, stop_rows, stop_cols, i0, j + 1, rows, cols), road]
    else:
        return []


def generate_sites(max_x, max_y, max_width, max_height, count):
    rects = []
    while len(rects) < count:
        (w, h) = (randint(1, max_width), randint(1, max_height))
        r = (randint(0, max_x - w), randint(0, max_y - h), w, h)
        if len([p for p in rects if intersects(r, p)]) == 0:
            rects = rects + [r]

    return rects


def generate_buildings(max_x, max_y, max_width, max_height, tall, count):
    sites = generate_sites(max_x, max_y, max_width, max_height, count)
    return [((x, y, r, c, 0), randint(0,tall), randclr()) for (x, y, r, c) in sites]