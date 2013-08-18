#!/usr/bin/python
# Jake Kosberg
# 
# World Generation module


import random
import pieces
import utils


def gen_world():
    world = []
    brick_pos = []
    blocked = True
    brick_amt = random.randint(3,6)
    print "Generating " + str(brick_amt) + " bricks at coords:"
    for a in range(4):
        row = []
        for b in range(4):
            row.append(pieces.board_piece())
        world.append(row)
    j = 0
    startingPoint = {"x" : 150,
                     "y" : 40}

    remaining_bricks = range(brick_amt)
    while len(remaining_bricks) > 0:
        for a in range(0,brick_amt):
            brick_xpos = random.randint(0,3)
            brick_ypos = random.randint(0,3)
            if not (brick_xpos, brick_ypos) in brick_pos:
                brick_pos.append((brick_xpos, brick_ypos))
                world[brick_xpos][brick_ypos].card = pieces.board_piece(blocked)
            remaining_bricks.pop()

    print brick_pos
    for row in world:
        i = 0
        for cell in row:
            cell.xpos = i * (84 + 2) + startingPoint["x"]
            cell.ypos = j * (102 + 2) + startingPoint["y"]
            i += 1
        j += 1
    return world
