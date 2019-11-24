from tetris.settings import BLOCK_WIDTH, BLOCK_HEIGHT

class Block(object):
    def __init__(self, color, pos):
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
        self.color = color
        self.x, self.y = pos

    def __str__(self):
        return f'Color: {self.color}'
