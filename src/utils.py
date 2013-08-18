#!/usr/bin/python
# Jake Kosberg
# 
# Utilities

import os
import sys

def dirlock(fn):
    return os.path.join(os.path.dirname(__file__), fn)

def event_selected(cards,mx,my):
    for monster in cards:
        if ((mx > monster.xpos and mx < monster.xpos + monster.width) and 
                (my > monster.ypos and my < monster.ypos + monster.width) and
                monster.selected == False):
            monster.select()
            return monster
        elif monster.selected == True:
            monster.deselect()
    return False
