from tetris.settings import (
    GUI_WIDTH, GUI_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
from tetris.gui import gui

class CollissionDetector:
    def hasTileReachedBottom(tile):
        for block in tile.blocks:
            if block.y >= (GUI_HEIGHT - BLOCK_HEIGHT):
                return True
        else:
            return False

    def wouldTileHitAnotherTileFromLeft(tile, stationary_tiles):
        for stationary_tile in stationary_tiles:
            for stationary_block in stationary_tile.blocks:
                for block in tile.blocks:
                    if (block.x + BLOCK_WIDTH == stationary_block.x and 
                            block.y == stationary_block.y):
                        return True
        else:
            return False

    def wouldTileHitAnotherTileFromRight(tile, stationary_tiles):
        for stationary_tile in stationary_tiles:
            for stationary_block in stationary_tile.blocks:
                for block in tile.blocks:
                    if (block.x - BLOCK_WIDTH == stationary_block.x and 
                            block.y == stationary_block.y):
                        return True
        else:
            return False

    def hasTileHitAnotherTileFromAbove(tile, stationary_tiles):
        for stationary_tile in stationary_tiles:
            for stationary_block in stationary_tile.blocks:
                for block in tile.blocks:
                    if (block.x == stationary_block.x and
                            block.y + BLOCK_HEIGHT == stationary_block.y):
                        return True
        else:
            return False

    def hasTileReachedRightBorder(tile):
        for block in tile.blocks:
            if block.x >= GUI_WIDTH - BLOCK_WIDTH:
                return True
        else:
            return False

    def hasTileReachedLeftBorder(tile):
        for block in tile.blocks:
            if block.x <= 0:
                return True
        else:
            return False

    def canTileMoveDown(tile):
        for block in tile.blocks:
            if gui.data[0][block.x//BLOCK_WIDTH] != 0:
                return False
        else:
            return True
