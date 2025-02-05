'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import pygame
from gamelib.game import Game

def main():
    pygame.init();
    pygame.mixer.init(frequency=44100,buffer=1024)

    g = Game()
    g.run()
