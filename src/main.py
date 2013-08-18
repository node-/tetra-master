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
        self.name = monster
        self.xpos = 520
        self.ypos = 20
        self.selected = False
        screen = pygame.display.get_surface()
    def select(self):
        for monster in get_cards():
            monster.selected = False
        self.selected = True
        return self.selected
    def deselect(self):
        self.selected = False


def get_cards():
    monsterone = card("one")
    monstertwo = card("two")
    monsterthree = card("three")
    monsterfour = card("four")
    monsterfive = card("five")
    cards = [monsterone,
            monstertwo,
            monsterthree,
            monsterfour,
            monsterfive]
    i = 0
    for monster in cards:
        monster.ypos += monster.height * i * .84
        i += 1
    return cards

def event_selected(cards,mx,my):
    for monster in cards:
        if ((mx > monster.xpos and mx < monster.xpos + monster.width) and 
                (my > monster.ypos and my < monster.ypos + monster.width) and
                monster.selected == False):
            monster.select()
        elif monster.selected == True:
            monster.deselect()


def main():
    running = True
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Tetra Master')
    board = pygame.image.load(dirlock('../data/board.bmp'))

    cards = get_cards()
    

    while running:
        clock.tick(60)
        screen.blit(board,(0,0))
        myfont = pygame.font.SysFont("monospace", 30)
        for monster in cards:
            screen.blit(monster.image,(monster.xpos, monster.ypos))
            if monster.selected == True:
                current_selected = myfont.render("'" + monster.name + "' is selected!", 1, (255,255,255))
                screen.blit(current_selected, (100, 100))
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                event_selected(cards,mx,my)

        pygame.display.update()

def gen_world():
    world = []
    for a in range(4):
        world.append([{}, {}, {} ,{}])

if __name__ == '__main__':
    main()
