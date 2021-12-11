import random
from game.actor import Actor
from game import constants
from game.point import Point
from game import grid

class Weapon(Actor):
    def __init__(self, image_path):
        super().__init__()
        self.set_image(image_path)
        self.set_height(constants.WEAPON_HEIGHT)
        self.set_width(constants.WEAPON_WIDTH)

        # x = constants.WEAPON_X
        # y = constants.WEAPON_Y
        # position = Point(x,y)
        # self.set_position(position)

        x = random.randint(0, constants.MAX_X - constants.WEAPON_WIDTH)
        y = random.randint(1, constants.MAX_Y - constants.WEAPON_HEIGHT)
        # position = Point(x, y)
        pos = grid.POSITION.next()
        position = Point(pos[0], pos[1])
        self.set_position(position)