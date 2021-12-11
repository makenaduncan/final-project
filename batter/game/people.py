import random
from game.actor import Actor
from game import constants
from game.point import Point
from game import grid

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

        x = random.randint(0, constants.MAX_X - constants.PERSON_WIDTH)
        y = random.randint(1, constants.MAX_Y - constants.PERSON_HEIGHT)
        # position = Point(x, y)
        pos = grid.POSITION.next()
        position = Point(pos[0], pos[1])
        self.set_position(position)