import pygame 
import world
import visual

screen = pygame.display.set_mode((1280, 840))


screen.fill((240, 240, 240))
b = world.place(world.new_object((2, 8), (2, 8), (20, 50)), (5, 15))
visual.draw_object(screen, b)

pygame.display.flip()

running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
