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

GAME_WIDTH = 10
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = 'Rock'
    SOLID = True

class Character(GameElement):
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    curr_position = 0 
    IMG_list = ['Cat', 'Girl', 'Horns', 'Princess', 'Boy', 'Rock']
    IMAGE = IMG_list[curr_position]

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

    def change_char(self):
        print "YAYE I speeleeed things wronnnng"
        self.IMAGE = self.IMG_list[self.curr_position % len(self.IMG_list)]
        GAME_BOARD.register(self)
        self.curr_position += 1


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

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

    GAME_BOARD.draw_msg("Your message here for the low low price of one human child!")

def keyboard_handler():
    if KEYBOARD[key.SPACE]:
        print "Yay! TOAST~!"
        PLAYER.change_char()

    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        x_range = range(GAME_WIDTH)
        y_range = range(GAME_HEIGHT)

        if next_x in x_range and next_y in y_range:

            existing_el = GAME_BOARD.get_el(next_x, next_y)
            if existing_el:
                existing_el.interact(PLAYER)

            if existing_el is None or not existing_el.SOLID:
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
                GAME_BOARD.set_el(next_x, next_y, PLAYER)
