#!/usr/bin/python
# Jake Kosberg
#
# Events module

import pygame
from pygame.locals import *

import utils
import pieces

def watch(cards,selection,mouse_pos,world):
    mx, my = mouse_pos


    if selection:
        for row in world:
            for cell in row:
                if cell:
                    if utils.cell_hovered(cell,mouse_pos):
                        cell.card = selection
                        cards = selection.remove_from_hand(cards)
    selection = utils.event_selected(cards,mx,my)
    return cards, selection
