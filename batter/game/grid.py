import random

# This class helps it so that none of the people or weapons touch each other or leave the screen

class Position:
    positions = []
    def __init__(self):

        for y in range(0, int((600-60)/60)):
            for x in range(0, int((800-60)/60)):
                self.positions.append((x*60,y*60))

        random.shuffle(self.positions)

    def next(self):
        return self.positions.pop()

POSITION = Position()