from tetris.settings import BLOCK_WIDTH, BLOCK_HEIGHT

class Block(object):
    def __init__(self, color):
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
        self.color = color

    def __str__(self):
        return f'Color: {self.color}'
