import random

from .block import Block
from tetris.game import shapes, directions
from tetris.settings import GUI_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_COLORS
from math import sin, cos, radians

all_shapes = [
    shapes.CUBE, shapes.I, shapes.S, shapes.Z,
    shapes.L, shapes.J, shapes.T]

class Tile(object):
    def __init__(self, shape, pos=((GUI_WIDTH//BLOCK_WIDTH//2*BLOCK_WIDTH), -BLOCK_HEIGHT)):
        if shape == 'random':
            self.shape = all_shapes[random.randint(0, len(all_shapes)-1)]
        else:
            self.shape = shape
        self.color = BLOCK_COLORS[self.shape]
        self.x, self.y = pos
        self.rotation = 0

        self.blocks = [Block(self.color, pos) for _ in range(4)]
        self.adjustBlockPositionsForShape()

    def adjustBlockPositionsForShape(self):
        # self.blocks[0] is ALWAYS the centre block (+ rotation center)
        if self.shape == shapes.CUBE:
            self.blocks[1].x += BLOCK_WIDTH
            self.blocks[2].y += BLOCK_HEIGHT
            self.blocks[3].x += BLOCK_WIDTH
            self.blocks[3].y += BLOCK_HEIGHT
        if self.shape == shapes.I:
            self.blocks[1].x -= BLOCK_WIDTH
            self.blocks[2].x += BLOCK_WIDTH
            self.blocks[3].x += 2* BLOCK_WIDTH
        if self.shape == shapes.S:
            self.blocks[1].x += BLOCK_WIDTH
            self.blocks[2].y += BLOCK_HEIGHT
            self.blocks[3].x -= BLOCK_WIDTH
            self.blocks[3].y += BLOCK_HEIGHT
        if self.shape == shapes.Z:
            self.blocks[1].x -= BLOCK_WIDTH
            self.blocks[2].y += BLOCK_HEIGHT
            self.blocks[3].x += BLOCK_WIDTH
            self.blocks[3].y += BLOCK_HEIGHT
        if self.shape in (shapes.L, shapes.J, shapes.T):
            self.blocks[1].x -= BLOCK_WIDTH
            self.blocks[2].x += BLOCK_WIDTH
            self.blocks[3].y += BLOCK_HEIGHT
            if self.shape == shapes.L:
                self.blocks[3].x -= BLOCK_WIDTH
            if self.shape == shapes.J:
                self.blocks[3].x += BLOCK_WIDTH

    def move(self, direction):
        if direction == directions.DOWN:
            for block in self.blocks:
                block.y += BLOCK_HEIGHT
        elif direction == directions.RIGHT:
            for block in self.blocks:
                block.x += BLOCK_WIDTH
        elif direction == directions.LEFT:
            for block in self.blocks:
                block.x -= BLOCK_WIDTH

    def rotate(self):
        if self.shape == shapes.CUBE:
            return None

        rotation_center = self.blocks[0]
        for block in self.blocks[1:]:
            old_vector = getVectorFromBlockToBlock(rotation_center, block)
            new_vector = getRotatedVector(vector=old_vector, rotationAngle=radians(90))
            block.x = rotation_center.x + new_vector[0]
            block.y = rotation_center.y + new_vector[1]            

    def __str__(self):
        line1_2 = f'Shape: {self.shape} \nColor: {self.color} \n'
        line3   = f'Blocks: {[str(block) for block in self.blocks]}\n'
        return line1_2 + line3

def getVectorFromBlockToBlock(block1, block2):
    x = block2.x - block1.x
    y = block2.y - block1.y
    return (x, y)

def getRotatedVector(vector, rotationAngle):
    x, y = vector
    newX = x * cos(rotationAngle) - y * sin(rotationAngle)
    newY = x * sin(rotationAngle) + y * cos(rotationAngle)
    return (round(newX), round(newY))
