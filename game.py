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

GAME_WIDTH = 3
GAME_HEIGHT = 3

#### Put class definitions here ####
class Rock(GameElement):
    #some shit here!
    IMAGE = 'Rock'

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    #we all want a rock to tie a piece of string around
    rock = Rock()
    GAME_BOARD.register(rock)
    GAME_BOARD.set_el(2,2, rock)
    print "The rock is at", (rock.x , rock.y)

