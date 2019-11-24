import pygame

import tetris.gui.gui as gui
from tetris.settings import (
    BACKGROUND_COLOR1, BACKGROUND_COLOR2, 
    GUI_WIDTH, BLOCK_WIDTH, GUI_HEIGHT)

class Draw:
    def drawBackground():
        for col in range(GUI_WIDTH//BLOCK_WIDTH):
            background_rect = pygame.Rect(
                        ((col * BLOCK_WIDTH), 0), (BLOCK_WIDTH, GUI_HEIGHT))
            if col%2 == 0:
                pygame.draw.rect(
                    gui.screen, BACKGROUND_COLOR1, background_rect)
            else:
                pygame.draw.rect(
                    gui.screen, BACKGROUND_COLOR2, background_rect)

    def drawBlock(block):
        border_rect = pygame.Rect(
                (block.x, block.y),
                (block.width, block.height))
        border_rect2 = pygame.Rect(
                (block.x+1, block.y+1),
                (block.width-2, block.height-2))
        block_rect = pygame.Rect(
                (block.x+2, block.y+2),
                (block.width-4, block.height-4))
        pygame.draw.rect(
            gui.screen, (0, 0, 0), border_rect)
        pygame.draw.rect(
            gui.screen, (255, 255, 255), border_rect2)
        pygame.draw.rect(
            gui.screen, block.color, block_rect)

    def drawTile(tile):
        for block in tile.blocks:
            Draw.drawBlock(block)
