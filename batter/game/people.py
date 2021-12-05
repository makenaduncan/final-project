import random
from game.actor import Actor
from game import constants
from game.point import Point

class People(Actor):
    def __init__(self, image_path):
        super().__init__()
        self.set_image(image_path)
        # self.set_image(constants.IMAGE_PERSON)
        self.set_height(constants.PERSON_HEIGHT)
        self.set_width(constants.PERSON_WIDTH)

        # x = constants.PEOPLE_X
        # y = constants.PEOPLE_Y
        # position = Point(x,y)
        # self.set_position(position)

        x = random.randint(0, constants.MAX_X - 1)
        y = random.randint(1, constants.MAX_Y - 1)
        position = Point(x, y)
        self.set_position(position)