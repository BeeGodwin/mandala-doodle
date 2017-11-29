import pygame
import sys
from pygame.locals import *

from branch import Branch, Point


def main():
    pygame.init()

    res = wid, hi = 1024, 768
    d_surf = pygame.display.set_mode(res)

    point = Point(wid / 2, hi / 2)
    n = 9
    branch_list = []
    for i in range(n):
        branch = Branch(point, angle=360 / n * i, dev=27, dst=100, max_dep=6)
        branch_list.append(branch)

    while True:

        d_surf.fill((0, 0, 0))
        for branch in branch_list:
            draw_branch(d_surf, branch)
            # branch.inc_tree_angle(-0.2, 3)  # borked either way. this would be straight rotation
            # branch.inc_angle(0.6, 3)  # push angles breaks
            branch.inc_dev(0.04, 2)  # doesn't work without push angles
            branch.inc_tree_dev(0.04)  # ditto
            branch.propagate()

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == 27:
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