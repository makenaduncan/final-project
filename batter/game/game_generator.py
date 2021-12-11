
import random
from game.weapon import Weapon
from game.detective import Detective
from game.people import People
from game import constants


class GameGenerator():

    def get_detective(self):
        boxes = []
        box = Detective()
        boxes.append(box)
        return boxes

    def get_weapons(self):
        weapons = []
        knife = Weapon(constants.IMAGE_KNIFE)
        rope = Weapon(constants.IMAGE_ROPE)
        pistol = Weapon(constants.IMAGE_PISTOL)
        candlestick = Weapon(constants.IMAGE_CANDLESTICK)  
        poison = Weapon(constants.IMAGE_POISON)
        axe = Weapon(constants.IMAGE_AXE)
        wrench = Weapon(constants.IMAGE_WRENCH)
        horseshoe = Weapon(constants.IMAGE_HORSESHOE)

        knife.set_text("clue 1")
        rope.set_text("clue 2")
        pistol.set_text("clue 3")
        candlestick.set_text("clue 4")
        poison.set_text("clue 5")
        axe.set_text("clue 6")
        wrench.set_text("clue 7")
        horseshoe.set_text("clue 8")

        weapons.append(knife)
        weapons.append(rope)
        weapons.append(pistol)
        weapons.append(candlestick)
        weapons.append(poison)
        weapons.append(axe)
        weapons.append(wrench)
        weapons.append(horseshoe)

        # for weapon in weapons:
        #     #weapon.set_text(constants.W_CLUES)
        #     weapon.set_status(False)

        #put the code to randomly select a weapon
        # chosen_index = random.randint(0,len(weapons))
        # chosen_weapon = weapons[chosen_index]
        # chosen_weapon.set_text("this is the murder weapon")
        # chosen_weapon.set_status(True)
        return weapons

    def get_people(self):
        people = []
        mustard = People(constants.IMAGE_MUSTARD)
        plum = People(constants.IMAGE_PLUM)
        green = People(constants.IMAGE_GREEN)
        peacock = People(constants.IMAGE_PEACOCK)
        scarlet = People(constants.IMAGE_SCARLET)
        white = People(constants.IMAGE_WHITE)

        mustard.set_text("mustard")
        plum.set_text("plum")
        green.set_text("green")
        peacock.set_text("peacock")
        scarlet.set_text("scarlet")
        white.set_text("white")

        people.append(mustard)
        people.append(plum)
        people.append(green)
        people.append(peacock)
        people.append(scarlet)
        people.append(white)

        

        # for person in people:
        #     person.set_text(constants.P_CLUES)
        #     person.set_status(False)

        #put the code to randomly select a weapon
        # chosen_pindex = random.randint(0,len(people)-1)
        # chosen_person = people[chosen_pindex]
        # chosen_person.set_text("This is the murderer")
        # chosen_person.set_status(True)

        # add a marquee to diplay the hints

        return people