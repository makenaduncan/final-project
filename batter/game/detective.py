from game.actor import Actor
from game import constants
from game.point import Point
import pygame

class Detective(Actor):
    def __init__(self):
        super().__init__()
        self.set_image(constants.IMAGE_DETECTIVE)
        self.set_height(constants.DETECTIVE_HEIGHT)
        self.set_width(constants.DETECTIVE_WIDTH)

        x = constants.DETECTIVE_X
        y = constants.DETECTIVE_Y
        position = Point(x,y)
        self.set_position(position)

        pygame.mixer.init()
        file = "./batter/assets/spooky.mp3"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()