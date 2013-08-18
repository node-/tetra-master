#!/usr/bin/python
# Jake Kosberg
# http://github.com/node-/tetra-master
#

import os, pygame
from pygame.locals import *

def dirlock(fn):
    return os.path.join(os.path.dirname(__file__), fn)

class card(pygame.sprite.Sprite):
    def __init__(self, monster):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(dirlock('../data/cards/' + monster + '.bmp'))
        self.width, self.height = pygame.Surface.get_size(self.image)
        self.xpos = 0
        self.ypos = 0
        screen = pygame.display.get_surface()



def main():
    running = True
    z = 0
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Tetra Master')
    board = pygame.image.load(dirlock('../data/board.bmp')) 
    monsterone = card("one")
    monstertwo = card("two")

    while running:
        clock.tick(60)
        screen.blit(board,(0,0))
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if ((mx > monsterone.xpos) and (mx < monsterone.xpos + monsterone.width)):
                    z = 1
            elif event.type == MOUSEBUTTONUP:
                z = 0
            if z == 1:
                monsterone.xpos = mx
                monsterone.ypos = my

        screen.blit(monsterone.image,(monsterone.xpos, monsterone.ypos))
        pygame.display.update()

def gen_world():
    world = []
    for a in range(4):
        world.append([{}, {}, {} ,{}])

if __name__ == '__main__':
    main()
