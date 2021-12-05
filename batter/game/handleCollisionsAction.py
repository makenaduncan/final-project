from game.actor import Actor
from game import constants
from game.point import Point
from batter import __main__

class HandleCollisionsAction(Actor):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
         # there's only one
        boxes = cast["boxes"][0] # there's only one
        weapons = cast["weapons"]
        people = cast["people"]
        people.set_text("")
        for cast in __main__:
            if self._physics_service.is_collision(boxes, weapons, people):
                description = cast.get_description()
                boxes.set_text(description) 