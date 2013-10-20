import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, K_DOWN, QUIT, K_RIGHT, K_LEFT, K_UP
from pygame import Surface
import world
import visual
from visual import vecadd
from functools import cmp_to_key

(ROWS, COLS, BUILDINGS) = (300, 300, 100)


def draw(view, world_objects):
    for obj in world_objects:
        visual.draw_object(view, obj)


def cmp_objects(a, b):
    return world.cmp_objects(a, b, ROWS * COLS)


objects = sorted(
    [
        ((120, 0, 100, 100,  0), 96, 0x404040),
        ((120, 0, 100, 100, 96),  0, 0x10FF10),
        ((60,  0, 300, 300,  0),  0, 0x10FF10)
    ], key=cmp_to_key(cmp_objects))

surf = Surface((10000, 10000))

surf.fill((240, 240, 240))
draw(surf, objects)

running = True
redraw = True

screen = pygame.display.set_mode((1600, 900))
screen.fill((240, 240, 240))
move = (-1390, -40)

#noinspection PyArgumentList
pygame.key.set_repeat(500, 30)

move_dict = {
    K_DOWN: (0, -10),
    K_UP: (0, 10),
    K_LEFT: (10, 0),
    K_RIGHT: (-10, 0)
}

while running:
    events = pygame.event.get()
    for e in events:
        running = e.type != QUIT and not (e.type == KEYDOWN and e.key == K_ESCAPE)
        if e.type == KEYDOWN and e.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
            redraw = True
            move = vecadd(move, move_dict[e.key])

    if redraw:
        redraw = False
        screen.fill((240, 240, 240))
        screen.blit(surf, move)

    pygame.display.flip()