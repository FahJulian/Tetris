import pygame

from tetris.settings import GUI_WIDTH, GUI_HEIGHT

def start():
    screen = pygame.display.set_mode(size=(GUI_WIDTH, GUI_HEIGHT))
    pygame.display.set_caption('Tetris')
        