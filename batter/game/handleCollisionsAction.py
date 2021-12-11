from game.actor import Actor
from game import constants
from game.point import Point
from game.physics_service import PhysicsService

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
        box = cast["boxes"][0] # there's only one
        weapons = cast["weapons"]
        people = cast["people"]
        # people.set_text("")

        #for cast in __main__:
        for person in people:
            if PhysicsService().is_collision(box, person):
                description = person.get_text()
                box.set_text(description) 
                print(description)
                
        for weapon in weapons:
            if PhysicsService().is_collision(box, weapon):
                description = weapon.get_text()
                box.set_text(description) 
                print(description)
