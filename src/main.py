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
import worldgen
import events



def main():
    running = True
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Tetra Master')
    board = pygame.image.load(utils.dirlock('../data/board.bmp'))
    world = worldgen.gen_world()
    cards = pieces.get_cards() 
    selection = False

    while running:
        clock.tick(60)
        screen.blit(board,(0,0))
        myfont = pygame.font.Font(utils.dirlock("../data/Trajan-Bold.ttf"), 30)
        mx,my = pygame.mouse.get_pos()
        mouse_pos = (mx, my)
        pygame.draw.rect(screen, (100,40,80), (150,40, 336, 408))
        for a in world:
            for b in a:
                pygame.draw.rect(screen, (0,0,0), (b.xpos, b.ypos, 84, 102))
                if b.card:
                    b.draw(b.card.image)
                    screen.blit(b.image, (b.xpos, b.ypos))
        for monster in cards:
            screen.blit(monster.image,(monster.xpos, monster.ypos))
            if monster.selected == True:
                current_selected = myfont.render(monster.name + " is selected!", 1, (255,255,255))
                screen.blit(current_selected, (100, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
               cards, selection = events.watch(cards,selection,mouse_pos,world) 

        pygame.display.update()

if __name__ == '__main__':
    main()
