import pygame

from tetris.gui import gui
from tetris.clock import gameclock

if __name__ == '__main__':
    pygame.init()
    
    gui.start()

    gameclock.start()
