import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, K_DOWN, QUIT, K_RIGHT, K_LEFT, K_UP
from pygame import Surface
import utils
import world
import visual
from visual import vecadd
from functools import cmp_to_key

(ROWS, COLS, BUILDINGS) = (300, 300, 500)


def draw(world_objects):
    d = [visual.draw_object(obj) for obj in world_objects]
    (min_x, min_y, max_x, max_y) = (None, None, None, None)
    for (move, surf) in d:
        min_x = move[0] if min_x is None or min_x > move[0] else min_x
        min_y = move[1] if min_y is None or min_y > move[1] else min_y
        max_x = move[0] + surf.get_rect().width if max_x is None or max_x < move[0] + surf.get_rect().width else max_x
        max_y = move[1] + surf.get_rect().height if max_y is None or max_y < move[1] + surf.get_rect().height else max_y

    view = Surface((max_x - min_x, max_y - min_y))
    view.fill(0xFF01FF)
    view.set_colorkey(0xFF01FF)
    print((min_x, min_y))
    for (move, surf) in d:
        view.blit(surf, vecadd((-min_x, -min_y), move))

    return view


def cmp_objects(a, b):
    return world.cmp_objects(a, b, ROWS * COLS)


def get_default_move(s, v):
    (_, _, w_s, h_s) = s.get_rect()
    (_, _, w_v, h_v) = v.get_rect()

    return (w_s - w_v) / 2, (h_s - h_v) / 2

objects = sorted(
    [
        ((0,   0, 300, 300,  0),   0,        0xCCCCCC),
        ((0,   0, 100, 100,  0),   0, utils.randclr()),
        ((0,   0,  50,  50,  0), 100, utils.randclr()),
        ((0,  80, 300,  10,  0),   0,        0x090909),
        ((90, 70,  60,  10,  0), 160, utils.randclr()),
        ((30, 70,  60,  10,  0), 160, utils.randclr()),
        ((80,  0,  10, 300,  0),   0,        0x090909),
        ((90,  0,  10,  60,  0), 200, utils.randclr()),
        ((70,  0,  10,  40,  0), 150, utils.randclr())
    ], key=cmp_to_key(cmp_objects))
print(objects)
surf = draw(objects)

#surf.fill((240, 240, 240))


running = True
redraw = True

screen = pygame.display.set_mode((1600, 900))
screen.fill((240, 240, 240))
move = get_default_move(screen, surf)

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