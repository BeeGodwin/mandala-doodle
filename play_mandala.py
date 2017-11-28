import pygame
import sys
from pygame.locals import *

from branch import Branch, Point

def main():
    pygame.init()

    res = wid, hi = 640, 480
    d_surf = pygame.display.set_mode(res)

    point = Point(wid / 2, hi / 2)

    branch = Branch(point)

    while True:

        d_surf.fill((0, 0, 0))


        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()