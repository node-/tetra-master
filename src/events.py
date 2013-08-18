#!/usr/bin/python
# Jake Kosberg
# http://github.com/node-/tetra-master
# Main Module

import pygame
from pygame.locals import *

import utils
import pieces

def watch(cards,selection,mouse_pos,world):
    mx, my = mouse_pos


    if selection:
        for row in world:
            for cell in row:
                if (mx > cell.xpos and mx < cell.xpos + cell.width and 
                        my > cell.ypos and my < cell.ypos + cell.height):
                    cell.card = selection
                    cards = selection.remove_from_hand(cards)
    selection = utils.event_selected(cards,mx,my)
    return cards, selection
