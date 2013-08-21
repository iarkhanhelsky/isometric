import pygame 
import world
import visual
from random import randint
from functools import cmp_to_key

screen = pygame.display.set_mode((1280, 840))

screen.fill((240, 240, 240))

for obj in sorted(world.populate(500, 200, 200), key=cmp_to_key(world.cmp_objects)):
	visual.draw_object(screen, obj)

pygame.display.flip()

running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
