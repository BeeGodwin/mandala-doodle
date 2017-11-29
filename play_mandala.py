import pygame
import sys
from pygame.locals import *

from branch import Branch, Point


def main():
    pygame.init()

    res = wid, hi = 1024, 768
    d_surf = pygame.display.set_mode(res)

    point = Point(wid / 2, hi / 2)
    n = 5
    branch_list = []
    for i in range(n):
        branch = Branch(point, angle=360 / n * i, dev=90 / n, dst=100, max_dep=6)
        branch_list.append(branch)

    while True:

        d_surf.fill((0, 0, 0))
        for branch in branch_list:  # PH code to test methods: a better gen method reqd!
            branch.push_angles()
            branch.inc_tree_angle(-0.2)  # all works now, but order is important!
            branch.inc_angle(2, 3)
            branch.inc_angle(-1, 4)# push_angle first
            branch.inc_tree_dev(0.04)  # then angle ops, tree-wide first
            branch.inc_dev(-0.4, 2)  # then dev ops, tree-wide first.
            branch.propagate()  # then propagate.
            draw_branch(d_surf, branch)

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
                       (branch.end_x, branch.end_y),
                       1)
    if len(branch.chn) > 0:
        for ch in branch.chn:
            draw_branch(d_surf, ch)


if __name__ == '__main__':
    main()
