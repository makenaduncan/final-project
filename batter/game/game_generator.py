
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

        knife.set_text("knife")
        rope.set_text("rope")
        pistol.set_text("pistol")
        candlestick.set_text("candlestick")
        poison.set_text("poison")
        axe.set_text("axe")
        wrench.set_text("wrench")
        horseshoe.set_text("horseshoe")

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

        # put the code to randomly select a weapon
        chosen_index = random.randint(0,len(weapons) -1)
        chosen_weapon = weapons[chosen_index]
        chosen_weapon.set_text("this is the murder weapon")
        chosen_weapon.set_status(True)



        return weapons

    def get_people(self):
        people = []
        mustard = People(constants.IMAGE_MUSTARD)
        plum = People(constants.IMAGE_PLUM)
        green = People(constants.IMAGE_GREEN)
        peacock = People(constants.IMAGE_PEACOCK)
        scarlet = People(constants.IMAGE_SCARLET)
        white = People(constants.IMAGE_WHITE)

        mustard.set_text("I was cooking dinner when I heard a loud crash")
        plum.set_text("5 + 6 does not equal 3")
        green.set_text("I've always wanted a bright yellow tuxedo")
        peacock.set_text("I am always up for a game of cards")
        scarlet.set_text("This isn't really my seen")
        white.set_text("How was I suppose to know that someone was going to die?")

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
        chosen_pindex = random.randint(0,len(people)-1)
        chosen_person = people[chosen_pindex]
        chosen_person.set_text("This is the murderer")
        chosen_person.set_status(True)

        # add a marquee to diplay the hints

        return people