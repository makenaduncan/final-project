from game.actor import Actor
from game import constants
from game.point import Point

class Box(Actor):
    def __init__(self):
        super().__init__()
        self.set_image(constants.IMAGE_BOX)
        self.set_height(constants.BOX_HEIGHT)
        self.set_width(constants.BOX_WIDTH)

        x = constants.BOX_X
        y = constants.BOX_Y
        position = Point(x,y)
        self.set_position(position)