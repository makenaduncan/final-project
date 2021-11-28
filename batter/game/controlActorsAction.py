from game import constants
from game.action import Action

class ControlActorsAction(Action):
    def __init__(self, input_service):
        self.__input_service = input_service

    def execute(self, cast):
        direction = self.__input_service.get_direction()
        box = cast["boxes"][0]
        box.set_velocity(direction.scale(constants.BOX_SPEED))