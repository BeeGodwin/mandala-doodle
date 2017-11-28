import pygame
import sys
from pygame.locals import *

from branch import Branch, Point

def main():
    pygame.init()

    res = wid, hi = 640, 480
    d_surf = pygame.display.set_mode(res)

    point = Point(wid / 2, hi)

    branch = Branch(point, dev=30, dst=300)

    while True:

        d_surf.fill((0, 0, 0))

        draw_branch(d_surf, branch)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def draw_branch(d_surf, branch):
    """recurses down a branch and draws it."""

    pygame.draw.aaline(d_surf,
                       (255, 255, 255),
                       (branch.x, branch.y),
                       (branch.end_x, branch.end_y))
    if len(branch.chn) > 0:
        for ch in branch.chn:
            draw_branch(d_surf, ch)


if __name__ == '__main__':
    main()