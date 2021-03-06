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
        min_x = (lambda x: x if min_x is None or min_x > x else min_x)(move.x)
        min_y = (lambda y: y if min_y is None or min_y > y else min_y)(move.y)
        max_x = (lambda x: x if max_x is None or max_x < x else max_x)(move.x + surf.get_rect().width)
        max_y = (lambda y: y if max_y is None or max_y < y else max_y)(move.y + surf.get_rect().height)

    view = Surface((max_x - min_x, max_y - min_y))
    view.fill(0xFF01FF)
    view.set_colorkey(0xFF01FF)

    for (move, surf) in d:
        view.blit(surf, vecadd((-min_x, -min_y), move))

    return view


def cmp_objects(a, b):
    return world.cmp_objects(a, b, ROWS * COLS)


def get_default_move(s, v):
    (_, _, w_s, h_s) = s.get_rect()
    (_, _, w_v, h_v) = v.get_rect()

    return (w_s - w_v) / 2, (h_s - h_v) / 2


def main():
    objects = sorted(
        #[
        #    ((0,   0, 300, 300,  0),   0,        0xCCCCCC),
        #    ((0,   0, 100, 100,  0),   0, utils.randclr()),
        #    ((0,   0,  50,  50,  0), 100, utils.randclr()),
        #    ((0,  80, 300,  10,  0),   0,        0x090909),
        #    ((90, 70,  60,  10,  0), 160, utils.randclr()),
        #    ((20, 70,  60,  10,  0), 160, utils.randclr()),
        #    ((80,  0,  10, 300,  0),   0,        0x090909),
        #    ((90,  0,  10,  60,  0), 200, utils.randclr()),
        #    ((70,  0,  10,  40,  0), 150, utils.randclr())
        #]
        world.generate_buildings(300, 300, 40, 40, 500, 100)
        , key=cmp_to_key(cmp_objects))

    surf = draw(objects)

    running = True
    redraw = True

    screen = pygame.display.set_mode((1600, 900))
    screen.fill((240, 240, 240))
    move = get_default_move(screen, surf)

    #noinspection PyArgumentList
    pygame.key.set_repeat(500, 30)

    move_dict = {
        K_DOWN:  (0, -10),
        K_UP:    (0,  10),
        K_LEFT:  (10,  0),
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

main()