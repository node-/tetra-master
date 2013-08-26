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
        self.currentPlayer = True
    def switch_turn(self):
        self.currentPlayer = not self.currentPlayer


def gen_world():
    _world = []
    brick_pos = []
    brick_amt = random.randint(2,6) # Don't set over 16
    print "Generating " + str(brick_amt) + " bricks at coords: " 
    for a in range(4):
        row = []
        for b in range(4):
            row.append(pieces.board_piece())
        _world.append(row)
    startingPoint = {"x" : 150,
                     "y" : 40}
    while brick_amt > 0:
        brick_xpos = random.randint(0,3)
        brick_ypos = random.randint(0,3)
        if not (brick_xpos, brick_ypos) in brick_pos:
            brick_amt -= 1
            brick_pos.append((brick_xpos, brick_ypos))
            _world[brick_xpos][brick_ypos].card = pieces.board_piece(True)
    
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
