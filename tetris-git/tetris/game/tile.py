from .block import Block

class Tile(object):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.blocks = [Block(color) for _ in range(4)]

    def __str__(self):
        line1_2 = f'Shape: {self.shape} \nColor: {self.color} \n'
        line3   = f'Blocks: {[str(block) for block in self.blocks]}\n'
        return line1_2 + line3
