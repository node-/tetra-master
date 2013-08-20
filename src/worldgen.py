#!/usr/bin/python
# Jake Kosberg
# 
# World Generation module


import random
import pieces
import utils


class World():
    def __init__(self,_world):
        self.grid = _world
        self.player = True
        

    def switch_turn(self):
        self.player = not self.player


def gen_world():
    _world = []
    brick_pos = []
    blocked = True
    brick_amt = random.randint(3,6) # Don't set over 16, since there are only 16 on the grid
    print "Generating " + str(brick_amt) + " bricks at coords: " 
    for a in range(4):
        row = []
        for b in range(4):
            row.append(pieces.board_piece())
        _world.append(row)
    startingPoint = {"x" : 150,
                     "y" : 40}
    remaining_bricks = []

    for i in range(0,brick_amt):
        remaining_bricks.append(i)

    while len(remaining_bricks) > 0:
        brick_xpos = random.randint(0,3)
        brick_ypos = random.randint(0,3)
        if not (brick_xpos, brick_ypos) in brick_pos:
            remaining_bricks.pop()
            brick_pos.append((brick_xpos, brick_ypos))
            _world[brick_xpos][brick_ypos].card = pieces.board_piece(blocked)
    
    print brick_pos
    j = 0
    for row in _world:
        i = 0
        for cell in row:
            cell.xpos = i * (84 + 2) + startingPoint["x"]
            cell.ypos = j * (102 + 2) + startingPoint["y"]
            i += 1
        j += 1
    _world = World(_world)

    return _world
