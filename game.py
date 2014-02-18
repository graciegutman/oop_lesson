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

class Character(GameElement):
    IMAGE = 'Horns'

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

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("Your message here for the low low price of one human child!")

def keyboard_handler():
    if KEYBOARD[key.UP]:
        GAME_BOARD.draw_msg("You pressed up")
        next_y = PLAYER.y - 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
    elif KEYBOARD[key.DOWN]:
        GAME_BOARD.draw_msg("You pressed down")
        next_y = PLAYER.y + 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
    elif KEYBOARD[key.RIGHT]:
        GAME_BOARD.draw_msg("You pressed right")
        next_x = PLAYER.x + 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
    elif KEYBOARD[key.LEFT]:
        GAME_BOARD.draw_msg("You pressed wrong. loljk left.")
        next_x = PLAYER.x - 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
    elif KEYBOARD[key.SPACE]:
        GAME_BOARD.erase_msg()

