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

GAME_WIDTH = 6
GAME_HEIGHT = 10

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = 'Rock'
    SOLID = True

class Character(GameElement):
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You got a gem! You have %d items!" %(len(player.inventory)))

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    #we all want a rock to tie a piece of string around
    rock_positions = [
        (0, 0),
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

    global P1
    P1 = Character()
    GAME_BOARD.register(P1)
    GAME_BOARD.set_el(0, GAME_HEIGHT-1, P1)

    global P2
    P2 = Character()
    GAME_BOARD.register(P2)
    GAME_BOARD.set_el(GAME_WIDTH-1, GAME_HEIGHT-1, P2)

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

    GAME_BOARD.draw_msg("Your message here for the low low price of one human child!")

def keyboard_handler():
    direction1 = None
    direction2 = None

    #p1 keys
    if KEYBOARD[key.UP]:
        direction1 = "up"
    if KEYBOARD[key.DOWN]:
        direction1 = "down"
    if KEYBOARD[key.LEFT]:
        direction1 = "left"
    if KEYBOARD[key.RIGHT]:
        direction1 = "right"

    #p2 keys
    if KEYBOARD[key.W]:
        direction2 = "up"
    if KEYBOARD[key.S]:
        direction2 = "down"
    if KEYBOARD[key.A]:
        direction2 = "left"
    if KEYBOARD[key.D]:
        direction2 = "right"


    if direction1:
        next_location = P1.next_pos(direction1)
        next_x = next_location[0]
        next_y = next_location[1]

        x_range = range(GAME_WIDTH)
        y_range = range(GAME_HEIGHT)

        if next_x in x_range and next_y in y_range:

            existing_el = GAME_BOARD.get_el(next_x, next_y)
            if existing_el:
                existing_el.interact(P1)

            if existing_el is None or not existing_el.SOLID:
                GAME_BOARD.del_el(P1.x, P1.y)
                GAME_BOARD.set_el(next_x, next_y, P1)
    if direction2:
        next_location = P2.next_pos(direction2)
        next_x = next_location[0]
        next_y = next_location[1]

        x_range = range(GAME_WIDTH)
        y_range = range(GAME_HEIGHT)

        if next_x in x_range and next_y in y_range:

            existing_el = GAME_BOARD.get_el(next_x, next_y)
            if existing_el:
                existing_el.interact(P2)

            if existing_el is None or not existing_el.SOLID:
                GAME_BOARD.del_el(P2.x, P2.y)
                GAME_BOARD.set_el(next_x, next_y, P2)