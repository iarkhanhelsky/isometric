import pygame
from utils import ij_to_xy
import operator


def vecadd(a, b):
    return tuple(map(operator.add, a, b))


def draw_object(screen, obj):
    ((i, j, rows, cols, level), height, color) = obj

    minus_height = (0, -height)

    basement = [vecadd(ij_to_xy(*p), (0, -level)) for p in [(i, j), (i, j + cols), (i + rows, j + cols), (i + rows, j)]]

    top = [vecadd(p, minus_height) for p in basement]
    front = [basement[1], basement[2], top[2], top[1]]
    left = [basement[0], basement[1], top[1], top[0]]

    for side in [top, front, left]:
        pygame.draw.polygon(screen, color, side, 0)
        pygame.draw.polygon(screen, (0, 0, 0), side, 2)
