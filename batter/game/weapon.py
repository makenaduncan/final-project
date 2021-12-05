import random
from game.actor import Actor
from game import constants
from game.point import Point

class Weapon(Actor):
    def __init__(self, image_path):
        super().__init__()
        # self.set_image(image_path)
        self.set_height(constants.WEAPON_HEIGHT)
        self.set_width(constants.WEAPON_WIDTH)

        # x = constants.WEAPON_X
        # y = constants.WEAPON_Y
        # position = Point(x,y)
        # self.set_position(position)

        x = random.randint(0, constants.MAX_X - 1)
        y = random.randint(1, constants.MAX_Y - 1)
        position = Point(x, y)
        self.set_position(position)