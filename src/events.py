#!/usr/bin/python
# Jake Kosberg
#
# Events module

import pygame
from pygame.locals import *

import utils
import pieces

def watch(cards,selection,mouse_pos,_world):
    mx, my = mouse_pos
    _world = _world.grid


    if selection:
        for row in _world:
            for cell in row:
                if cell:
                    if utils.cell_hovered(cell,mouse_pos) and not cell.card: 
                        cell.card = selection
                        cards = selection.remove_from_hand(cards)
    selection = utils.event_selected(cards,mx,my)
    return cards, selection
