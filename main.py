import pygame 
import world
import visual
from random import randint
from functools import cmp_to_key
from utils import flatten

screen = pygame.display.set_mode((1920, 1080))

screen.fill((240, 240, 240))



for obj in sorted([(x, 0, 0xCCCCCC) for x in flatten(world.road_populate([[0 for _ in range(300)] for _ in range(300)], 10, 10, 0, 0, 300, 300)) ], key=cmp_to_key(world.cmp_objects)):
	visual.draw_object(screen, obj)

pygame.display.flip()

running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
