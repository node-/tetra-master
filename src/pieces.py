#!/usr/bin/python
# Jake Kosberg
# 
# Pieces module

import pygame
import utils

class card(pygame.sprite.Sprite):
    def __init__(self, monster):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(utils.dirlock('../data/cards/' + monster + '.bmp'))
        self.width, self.height = (84, 102)
        self.name = monster
        self.xpos = 520
        self.ypos = 20
        self.blocked = True
        self.selected = False
        screen = pygame.display.get_surface()
    def select(self):
        for monster in get_hand():
            monster.selected = False
        self.selected = True
        return self.selected
    def deselect(self):
        self.selected = False
    def remove_from_hand(self,cards):
        cards = cards
        for monster in cards:
            if monster.name == self.name:
                cards.remove(monster)
        return cards


def get_hand():
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


class board_piece():
    def __init__(self,blocked=False):
        self.width, self.height = (84, 102)
        self.xpos = 0
        self.ypos = 0
        self.image = None
        self.card = None
        self.blocked = blocked
        if blocked:
            self.image = pygame.image.load(utils.dirlock('../data/brick.bmp'))
    def draw(self, image):
        self.image = image 

