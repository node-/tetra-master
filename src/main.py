#!/usr/bin/python
# Jake Kosberg
# http://github.com/node-/tetra-master
# Main Module

import os
import pygame
from pygame.locals import *

# Modules
import worldgen
import utils
import pieces
import events

def main():
    running = True
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Tetra Master')
    board = pygame.image.load(utils.dirlock('../data/board.bmp'))

    _selection = False
    _world = worldgen.gen_world()
    _hand = pieces.get_hand()

    while running:
        # Initialization
        clock.tick(60)
        screen.blit(board,(0,0))
        trayjizzle = pygame.font.Font(utils.dirlock("../data/Trajan-Bold.ttf"), 30)
        monospizzle = pygame.font.SysFont("monospace", 15, True)
        mx, my = pygame.mouse.get_pos()
        _mouse_pos = (mx, my)
        
        # Drawing
        pygame.draw.rect(screen, (100,40,80), (150,40, 336, 408))
        utils.print_world(_world, screen)
        display_mouse_coords = monospizzle.render("(" + str(mx) + ", " + str(my) + ")", 1, (255,255,255))
        screen.blit(display_mouse_coords, (5,5))

        front_card = _hand[-1]
        for monster in _hand:
            if monster.selected:
                screen.blit(monster.image,(monster.xpos, monster.ypos))
            if utils.cell_hovered(monster, _mouse_pos) and front_card != monster:
                _hand.insert(-1, _hand.pop(_hand.index(monster)))
            screen.blit(monster.image,(monster.xpos, monster.ypos))

        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
               _hand, _selection = events.watch(_hand,_selection,_mouse_pos,_world)

        pygame.display.update()

if __name__ == '__main__':
    main()
