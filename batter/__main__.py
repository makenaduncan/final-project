import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.detective import Detective
from game.weapon import Weapon
from game.people import People
from game.moveActorsAction import MoveActorsAction
from game.controlActorsAction import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    boxes = []
    box = Detective()
    boxes.append(box)
    cast["boxes"] = boxes

    weapons = []
    knife = Weapon(constants.IMAGE_WEAPON)
    rope = Weapon(constants.IMAGE_WEAPON)
    pistol = Weapon(constants.IMAGE_WEAPON)
    candlestick = Weapon(constants.IMAGE_WEAPON)  
    poison = Weapon(constants.IMAGE_WEAPON)
    trophy = Weapon(constants.IMAGE_WEAPON)
    bat = Weapon(constants.IMAGE_WEAPON)
    dumbbell = Weapon(constants.IMAGE_WEAPON)
    weapons.append(knife)
    weapons.append(rope)
    weapons.append(pistol)
    weapons.append(candlestick)
    weapons.append(poison)
    weapons.append(trophy)
    weapons.append(bat)
    weapons.append(dumbbell)
    cast["weapons"] = weapons
    # for weapon in weapons:
    #     weapon.set_text(constants.W_CLUES)
    #     weapon.set_status(False)
    #put the code to randomly select a weapon
    chosen_index = random.randint(0,len(weapons))
    chosen_weapon = weapons[chosen_index]
    chosen_weapon.set_text("this is the murder weapon")
    chosen_weapon.set_status(True)

    people = []
    mustard = People(constants.IMAGE_PERSON)
    plum = People(constants.IMAGE_PERSON)
    green = People(constants.IMAGE_PERSON)
    peacock = People(constants.IMAGE_PERSON)
    scarlet = People(constants.IMAGE_PERSON)
    white = People(constants.IMAGE_PERSON)
    people.append(mustard)
    people.append(plum)
    people.append(green)
    people.append(peacock)
    people.append(scarlet)
    people.append(white)
    cast["people"] = people
    # for person in people:
    #     person.set_text(constants.P_CLUES)
    #     person.set_status(False)
    #put the code to randomly select a weapon
    chosen_pindex = random.randint(0,len(people))
    chosen_person = people[chosen_pindex]
    chosen_person.set_text("This is the murderer")
    chosen_person.set_status(True)

    # Finish creating the cast 

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    moveActorsAction = MoveActorsAction()
    controlActorsAction = ControlActorsAction(input_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [controlActorsAction]
    script["update"] = [moveActorsAction]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Clue")
    # audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    # audio_service.stop_audio()

if __name__ == "__main__":
    main()