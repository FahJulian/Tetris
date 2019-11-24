import pygame

from tetris.game.tile import Tile
from tetris.game import shapes, directions
from tetris.gui import draw, gui
from tetris.actions.collissions import CollissionDetector
from tetris.settings import NORMAL_SPEED, ACCELERATED_SPEED, GUI_WIDTH, BLOCK_WIDTH

class OwnClock:
    def __init__(self):
        self.time_reference = pygame.time.get_ticks()
    def timeElapsed(self):
        return_value = pygame.time.get_ticks()-self.time_reference
        return return_value
    def updateTimeReference(self):
        self.time_reference = pygame.time.get_ticks()



clock = pygame.time.Clock()
stationary_tiles = []
moveDown_clock = OwnClock()

def start():
    moving_tile = Tile(shape='random')
    accelerate_speed = False
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    if not CollissionDetector.hasTileReachedRightBorder(moving_tile):
                        if CollissionDetector.wouldTileHitAnotherTileFromLeft(
                                                moving_tile, stationary_tiles):
                            stationary_tiles.append(moving_tile)
                            moving_tile = Tile(shape='random')
                            if not CollissionDetector.canTileMoveDown(moving_tile):
                                running = False
                        else:
                            moving_tile.move(direction=directions.RIGHT)

                if event.key == pygame.K_LEFT:
                    if not CollissionDetector.hasTileReachedLeftBorder(moving_tile):
                        if CollissionDetector.wouldTileHitAnotherTileFromRight(
                                                moving_tile, stationary_tiles):
                            stationary_tiles.append(moving_tile)
                            moving_tile = Tile(shape='random')
                            if not CollissionDetector.canTileMoveDown(moving_tile):
                                running = False
                        else:
                            moving_tile.move(direction=directions.LEFT)

                if event.key == pygame.K_DOWN:
                    accelerate_speed = True

                if event.key == pygame.K_UP:
                    moving_tile.rotate()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    accelerate_speed = False


        if not (CollissionDetector.hasTileReachedBottom(moving_tile) or 
                CollissionDetector.hasTileHitAnotherTileFromAbove(moving_tile, stationary_tiles)):
            if accelerate_speed:
                if moveDown_clock.timeElapsed() >= 1000 // ACCELERATED_SPEED:
                    moving_tile.move(direction=directions.DOWN)
                    moveDown_clock.updateTimeReference()
            elif moveDown_clock.timeElapsed() >= 1000 // NORMAL_SPEED:
                moving_tile.move(direction=directions.DOWN)
                moveDown_clock.updateTimeReference()

        else:
            if moveDown_clock.timeElapsed() >= 1000 // NORMAL_SPEED:
                stationary_tiles.append(moving_tile)
                moving_tile = Tile(shape='random')
                if not CollissionDetector.canTileMoveDown(moving_tile):
                    running = False

        gui.update_data(moving_tile, stationary_tiles)
        for index, line in enumerate(gui.data):
            if not (0 in line):
                gui.erase_line(index)

        draw.Draw.drawBackground()

        for line in gui.data:
            for block in line:
                if not block == 0:
                    draw.Draw.drawBlock(block)

      
        draw.Draw.drawTile(moving_tile)

        pygame.display.update()
