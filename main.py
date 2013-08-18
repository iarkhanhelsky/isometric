import pygame 
import world
import visual

screen = pygame.display.set_mode((640, 480))


screen.fill((240, 240, 240))
b = world.building((2, 8), (2, 8), (20, 50))
visual.draw_object(screen, b)

pygame.display.flip()

running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
