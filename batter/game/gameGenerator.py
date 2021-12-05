import random
from game import constants
from game.actor import Actor
from game.action import Action
from game.weapon import Weapon
from game.detective import Detective
from game.people import People

class GameGenerator(Actor):
    
    def get_detective(self,cast):
        boxes = []
        box = Detective()
        boxes.append(box)
        # cast["boxes"] = boxes
    #This is where I will put the code that is currently in main
        return boxes

    def get_weapons(self,cast):
    #This is where I will put the code that is currently in main
    #Then put the code to call the random clues
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
        for weapon in weapons:
            weapon.set_text(constants.W_CLUES)
            weapon.set_status(False)
    #put the code to randomly select a weapon
        chosen_index = random.randint(0,len(weapons))
        chosen_weapon = weapons[chosen_index]
        chosen_weapon.set_text("this is the murder weapon")
        chosen_weapon.set_status(True)
    #put code to set clue to chosen object
        return weapons

    def get_people(self,cast):
    #This is where I will put the code that is currently in main
    #Then put the code to call the random clues
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
        for person in people:
            person.set_text(constants.P_CLUES)
            person.set_status(False)
    #put the code to randomly select a weapon
        chosen_index = random.randint(0,len(people))
        chosen_person = people[chosen_index]
        chosen_person.set_text("This is the murderer")
        chosen_person.set_status(True)

    #put the code to set clue to chosen object
        return people



    #Notes
    #I will set a specific key on the keyboard that will count as the users "guess" 
    #so that when the push it (and are overlapping the object) it will either return
    #True or False

    #set keyboard functions
    #set up function to randomly select an object
    #set up a function to assign clues