#!/usr/bin/python
# Jake Kosberg
# http://github.com/node-/tetra-master
#

import os, pygame
from pygame.locals import *

def dirlock(fn):
    return os.path.join(os.path.dirname(__file__), fn)

class card(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(dirlock('../data/cards/001-one.bmp'))
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9



def main():
    print pygame.image.get_extended()
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Tetra Master')
    board = pygame.image.load(dirlock('../data/board.bmp'))
    screen.blit(board,(0,0))
    bomb = card()
    gen_world()

    while True:
        clock.tick(6)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        pygame.display.flip()
        screen.blit(bomb.image,(0,0))

def gen_world():
    world = []
    for a in range(4):
        world.append([{}, {}, {} ,{}])

if __name__ == '__main__':
    main()
