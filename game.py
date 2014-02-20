import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
from random import randint

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10
LEVEL = 1

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = 'Rock'
    SOLID = True

class Character(GameElement):
    SOLID = True
    IMAGE = "Key"
    def __init__(self, name):
        GameElement.__init__(self)
        self.name = name
        self.inventory = []


    # @param String "up"|"down"|"left"|"right"
    # @return Tuple|None
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

class Egg(GameElement):
    IMAGE = "BlueGem"
    SOLID = False
    WON_LEVEL = False

    #@param Object (an egg)
    #@param Object (player)
    #@return None
    def interact(self, player):
        x = player.x
        y = player.y
        player.inventory.append(self)
        GAME_BOARD.draw_msg("%r made a baby, %r wins!" % (player.name, player.name))
        player.IMAGE = "Girl"
        GAME_BOARD.del_el(x, y)
        GAME_BOARD.register(player)
        GAME_BOARD.set_el(x, y, player)
        global LEVEL
        LEVEL += 1
        self.WON_LEVEL = True

class Enemy(GameElement):
    IMAGE = "TallTree"
    def spawn(self, dt):
        x = randint(0, GAME_WIDTH - 1)
        y = randint(0, GAME_HEIGHT - 1)
        if not GAME_BOARD.get_el(x, y):
            GAME_BOARD.register(self)
            GAME_BOARD.set_el(x, y, self)



####   End class definitions    ####

def initialize(level):
    """Put game initialization code here"""
    if level == 1:
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
        P1 = Character("playa_1")
        GAME_BOARD.register(P1)
        GAME_BOARD.set_el(0, GAME_HEIGHT-1, P1)

        global P2
        P2 = Character("playa_2")
        GAME_BOARD.register(P2)
        GAME_BOARD.set_el(GAME_WIDTH-1, GAME_HEIGHT-1, P2)

        egg = Egg()
        GAME_BOARD.register(egg)
        GAME_BOARD.set_el(3, 1, egg)

        enemy = Enemy()
        pyglet.clock.schedule_interval(enemy.spawn, 5)

    elif level == 2:
        rock_positions = [
            (0, 0),
            (1, 2),
            (3, 2),
            (2, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (6, 4),
            (7, 2)
            ]

        rocks = []
        for pos in rock_positions:
            rock = Rock()
            GAME_BOARD.register(rock)
            GAME_BOARD.set_el(pos[0], pos[1], rock)
            rocks.append(rock)

        global P1
        P1 = Character("playa_1")
        GAME_BOARD.register(P1)
        GAME_BOARD.set_el(0, GAME_HEIGHT-1, P1)

        global P2
        P2 = Character("playa_2")
        GAME_BOARD.register(P2)
        GAME_BOARD.set_el(GAME_WIDTH-1, GAME_HEIGHT-1, P2)

        global egg
        egg = Egg()
        GAME_BOARD.register(egg)
        GAME_BOARD.set_el(3, 1, egg)

        enemy = Enemy()
        pyglet.clock.schedule_interval(enemy.spawn, 1)


def keyboard_handler():

    #Refactor this bullshit
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

    #Refactor this bullshit too! 
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

    #Why on earth is this so redundant?            
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

