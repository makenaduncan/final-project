from time import sleep

import pygame
from game import constants

class Director:

    def __init__(self, cast, script):
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._keep_playing = False



    def _cue_action(self, tag):
        for action in self._script[tag]:
            action.execute(self._cast)