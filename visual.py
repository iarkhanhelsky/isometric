import pygame
from pygame import Surface
from utils import ij_to_xy
import operator
from point import Point


def vecadd(a, b):
    return tuple(map(operator.add, a, b))


def draw_object(obj):
    ((i, j, rows, cols, level), height, color) = obj
    minus_height = Point(0, -height)

    basement = [Point(*vecadd(ij_to_xy(*p), (0, -level)))
                for p in [(0, 0), (0, 0 + cols), (0 + rows, 0 + cols), (0 + rows, 0)]]
    top = [vecadd(p, minus_height) for p in basement]
    front = [basement[1], basement[2], top[2], top[1]]
    left = [basement[0], basement[1], top[1], top[0]]

    v_move = -basement[3][1]
    delta = ij_to_xy(i, j)
    rect = (delta[0], delta[1] - (height + level), basement[2].x, basement[1].y - basement[3].y + height)
    surf = Surface((rect[2], rect[3]))
    surf.set_colorkey(0xFF01FF)
    surf.fill(0xFF01FF)
    for side in [top, front, left]:
        side = [(x, y + v_move + height) for (x, y) in side]
        pygame.draw.polygon(surf, color, side, 0)
        pygame.draw.polygon(surf, (0, 0, 0), side, 2)

    return Point(rect[0], rect[1] - v_move), surf