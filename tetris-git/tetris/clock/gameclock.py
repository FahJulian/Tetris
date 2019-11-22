import pygame

from tetris.game.tile import Tile
from tetris.game import shapes

def start():
    running = True
    while running:

        first_tile = Tile(shapes.CUBE, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            print(first_tile)
