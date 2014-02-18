import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    #some shit here!
    IMAGE = 'Rock'

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    #we all want a rock to tie a piece of string around
    rock_positions = [
        (2, 1),
        (1, 2),
        (3, 2),
        (2, 3),
        (4, 4)
        ]

    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    for rock in rocks:
        print rock
