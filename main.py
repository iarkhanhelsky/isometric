import pygame
import world
import visual
from functools import cmp_to_key
from utils import flatten

ROWS = 300
COLS = 300
BUILDINGS = 100


def draw(screen, objects):
    for obj in objects:
        visual.draw_object(screen, obj)

    pygame.display.flip()


def cmp_objects(a, b): return world.cmp_objects(a, b, ROWS * COLS)


screen = pygame.display.set_mode((600, 800))
screen.fill((240, 240, 240))

roads = [(x, 0, 0xCCCCCC) for x in
         flatten(world.road_populate([[0 for _ in range(COLS)] for _ in range(ROWS)], 10, 10, 0, 0, ROWS, COLS))]
buildings = world.populate(100, ROWS, COLS)
objects = sorted(roads + buildings, key=cmp_to_key(cmp_objects))

running = True

while running:
    event = pygame.event.poll()
    running = event.type != pygame.QUIT
    draw(screen, objects)