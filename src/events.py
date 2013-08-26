#!/usr/bin/python
# Jake Kosberg
#
# Events module

import pygame
from pygame.locals import *

import utils
import pieces
import random

class Turn():
    def player(self,_hand,_selection,_mouse_pos,_world):
        mx, my = _mouse_pos
        if _selection:
            for row in _world.grid:
                for cell in row:
                    if cell:
                        if utils.cell_hovered(cell,_mouse_pos) and not cell.card:
                            cell.card = _selection
                            _hand = _selection.remove_from_hand(_hand)
                            _world.currentPlayer = not _world.currentPlayer
        _selection = utils.event_selected(_hand,mx,my)
        return _hand, _selection


    def ai(self,_world):
        xpos = random.randint(0,len(_world.grid)-1)
        ypos = random.randint(0,len(_world.grid[0])-1)
        cell = _world.grid[xpos][ypos]
        if not cell.card:
            cell.card = pieces.card("alex")
            _world.currentPlayer = not _world.currentPlayer
            print "AI Played:", (xpos, ypos)
