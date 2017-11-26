import pygame
import sys
from pygame.locals import *

from branch import Branch


def main():
    pygame.init()

    res = wid, hi = 640, 480
    d_surf = pygame.display.set_mode(res)

    branch = Branch(ori=[wid/2, hi/2], dist=100, n=4, p=0.5)

    while True:

        d_surf.fill((0, 0, 0))

        draw_branch(branch, d_surf, 7)

        # branch.move([1, 0])

        branch.rotate(1)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def draw_branch(branch, d_surf, weight):
    end_x = branch.ori[0] + (branch.vct[0] * branch.dist)
    end_y = branch.ori[1] + (branch.vct[1] * branch.dist)
    pygame.draw.line(d_surf, (255, 255, 255), branch.ori, (end_x, end_y), weight)
    for pair in branch.branches:
        for child_branch in pair:
            draw_branch(child_branch, d_surf, weight - 2)


if __name__ == '__main__':
    main()