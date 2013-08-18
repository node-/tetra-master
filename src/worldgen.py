#!/usr/bin/python
# Jake Kosberg
# 
# World Generation module


import random
import pieces
import utils

brick_amt = random.randint(2,6)

def gen_world():
    world = []
    print "Generating " + str(brick_amt) + " bricks."
    for a in range(4):
        row = []
        for b in range(4):
            row.append(pieces.board_piece())
        world.append(row)
    j = 0
    startingPoint = {"x" : 150,
                     "y" : 40}
    for row in world:
        i = 0
        for cell in row:
            cell.xpos = i * (84 + 2) + startingPoint["x"]
            cell.ypos = j * (102 + 2) + startingPoint["y"]
            i += 1
        j += 1
    return world
