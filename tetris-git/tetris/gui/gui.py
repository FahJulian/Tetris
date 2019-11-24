import pygame

from tetris.settings import (
    GUI_WIDTH, GUI_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)

def generateEmptyLine():
    return [0 for _ in range(GUI_WIDTH//BLOCK_WIDTH)]
def generateEmptyGrid():
    return [generateEmptyLine() for _ in range(GUI_HEIGHT//BLOCK_HEIGHT)]

data = generateEmptyGrid()

def start():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(size=(GUI_WIDTH, GUI_HEIGHT))
    pygame.display.set_caption('Tetris')
        
def update_data(moving_tile, stationary_tiles):
    global data
    all_tiles = stationary_tiles[:]
    all_tiles.append(moving_tile)
    data = [[0 for _ in range(GUI_WIDTH//BLOCK_WIDTH)] for _ in range(GUI_HEIGHT//BLOCK_HEIGHT)]
    for tile in all_tiles:
        for block in tile.blocks:
            print(block.x, block.y)
            try:
                data[int(block.y//BLOCK_HEIGHT)][int(block.x//BLOCK_WIDTH)] = block
            except:
                del block

def erase_line(index):
    # data[line] = [0 for _ in range(GUI_WIDTH//BLOCK_WIDTH)]
    for line in data:
        for block in line:
            if not block == 0:
                block.y += BLOCK_HEIGHT
    for block in data[index]:
        del block
    data.pop(index)
    data.insert(0, generateEmptyLine())

def dropAllAbove(given_line):
    global data
    reversed_data = data[::-1]
    for index, line in enumerate(reversed_data[given_line:-1]):
        reversed_data[index] = reversed_data[index+1]
    reversed_data[-1] = generateEmptyLine()
    data = reversed_data[::-1]

