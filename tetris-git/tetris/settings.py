from tetris.game import shapes

BACKGROUND_COLOR1   = (100, 100, 100)
BACKGROUND_COLOR2   = (120, 120, 120)

GUI_WIDTH           = 400
GUI_HEIGHT          = 600

BLOCK_HEIGHT        = 40
BLOCK_WIDTH         = 40

NORMAL_SPEED        = 1
ACCELERATED_SPEED   = 15

BLOCK_COLORS        = {
    shapes.CUBE:    (255, 255, 0),
    shapes.I:       (0, 255, 255),
    shapes.S:       (56, 179, 0),
    shapes.Z:       (255, 0, 0),
    shapes.L:       (255, 165, 0),
    shapes.J:       (0, 0, 255),
    shapes.T:       (255, 0, 255)
}