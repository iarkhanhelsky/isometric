import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, K_DOWN, QUIT, K_RIGHT, K_LEFT, K_UP
from pygame import Surface
import world
import visual
from functools import cmp_to_key
from utils import flatten

ROWS = 300
COLS = 300
BUILDINGS = 100


def draw(view, world_objects):
    for obj in world_objects:
        visual.draw_object(view, obj)


def cmp_objects(a, b):
    return world.cmp_objects(a, b, ROWS * COLS)


roads = [(x, 0, 0xCCCCCC) for x in
         flatten(world.road_populate([[0 for _ in range(COLS)] for _ in range(ROWS)], 10, 10, 0, 0, ROWS, COLS))]
buildings = world.populate(BUILDINGS, ROWS, COLS)
objects = sorted(roads + buildings, key=cmp_to_key(cmp_objects))

surf = Surface((10000, 10000))

surf.fill((240, 240, 240))
draw(surf, objects)

running = True
redraw = True

screen = pygame.display.set_mode((600, 600))
screen.fill((240, 240, 240))
move = (-1390, -40)

while running:
    events = pygame.event.get()
    for e in events:
        if e.type == KEYDOWN:
            redraw = True

            if e.key == K_ESCAPE:
                running = False
            elif e.key == K_DOWN:
                move = (move[0], move[1] - 10)
            elif e.key == K_UP:
                move = (move[0], move[1] + 10)
            elif e.key == K_LEFT:
                move = (move[0] - 10, move[1])
            elif e.key == K_RIGHT:
                move = (move[0] + 10, move[1])
        elif e.type == QUIT:
            running = False

    if redraw:
        print(move)
        redraw = False
        screen.fill((240, 240, 240))
        screen.blit(surf, move)

    pygame.display.flip()