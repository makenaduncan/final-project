from game.game_generator import GameGenerator
from game import constants
from game.action import Action
from game.handleCollisionsAction import HandleCollisionsAction
import __main__

class ControlActorsAction(Action):
    def __init__(self, input_service):
        self.__input_service = input_service

    def execute(self, cast):
        direction = self.__input_service.get_direction()
        box = cast["boxes"][0]
        box.set_velocity(direction.scale(constants.BOX_SPEED))

        if self.__input_service.is_hint():
            HandleCollisionsAction.execute(self, cast)
        #display hint or yes/no
        #set up count and if it's == 2 (game over)
        #rest of code is in input_service.py

        # if self.__input_service.is_guess():
        #     HandleCollisionsAction.execute(self, cast)
            

        
        # def is_guess_correct(self, cast):
        #     if is_guess_correct == GameGenerator.chosen_person:
        #         self.is_guess_correct == True
                