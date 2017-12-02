import pygame
import sys
from pygame.locals import *
import random

from branch import Branch, Point
from colour import Colours


def main():
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    res = wid, hi = 1440, 870
    d_surf = pygame.display.set_mode(res)

    point = Point(wid / 2, hi / 2)
    n = 17
    max_dep = 5

    cols = Colours((0, 0, 0),
                   (255, 0, 0),
                   (255, 165, 0),
                   (255, 255, 0),
                   (0, 0, 0),
                   (0, 0, 0),
                   (0, 0, 40),
                   (255, 255, 255)
                   )

    col_spd = 2

    branch_list = []
    for i in range(n):
        branch = Branch(point, angle=360 / n * i, dev=90 / n, dst=150, max_dep=max_dep)
        branch_list.append(branch)

    set_colours(branch_list, cols)

    while True:

        cols.inc_colours(col_spd)
        d_surf.fill((0, 0, 0))
        for branch in branch_list:  # PH code to test methods: a better gen method reqd!
            branch.push_angles()
            branch.inc_tree_angle(-0.4)  # all works now, but order is important!
            branch.inc_angle(4, 3)
            branch.inc_angle(-2, 4)  # push_angle first
            branch.inc_tree_dev(0.08)  # then angle ops, tree-wide first
            branch.inc_dev(-0.8, 2)  # then dev ops, tree-wide first.
            branch.propagate()  # then propagate.
            # draw_circles(d_surf, branch, max_dep)
            draw_branch(d_surf, branch, cols)

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == 27:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(fps)


def set_colours(branch_list, cols):
    def walk_branch(branch):
        cols.assign_colour(branch, init_col_id[branch.dep - 1])
        for ch in branch.chn:
            walk_branch(ch)

    dep = branch_list[0].max_dep
    init_col_id = [random.randrange(0, cols.range - 1) for _ in range(dep)]
    for b in branch_list:
        walk_branch(b)


def draw_branch(d_surf, branch, cols):
    """recurses down a branch and draws it."""
    pygame.draw.line(d_surf,
                     cols.palette[cols.get_colour(branch)],
                     (branch.x, branch.y),
                     (branch.end_x, branch.end_y), 2)
    for ch in branch.chn:
        draw_branch(d_surf, ch, cols)


def draw_circles(d_surf, branch, size):
    """draws circles around points recursively"""
    step_size = 255 / size
    for i in range(size):
        shade = i * step_size
        pygame.draw.circle(d_surf,
                           (shade, shade, shade),
                           (int(branch.end_x), int(branch.end_y)),
                           (size - i) * 5,
                           5)
    for ch in branch.chn:
        draw_circles(d_surf, ch, size - 1)


if __name__ == '__main__':
    main()
