# game
MAX_TURN = 200

# items on map
MIN_MINES = 5
MAX_MINES = 10
MIN_RUMS = 10
MAX_RUMS = 26

# rum barrels content
RUM_MIN = 20
RUM_MAX = 20

MINE_DMG = 20

# map
MAP_WIDTH = 23
MAP_HEIGHT = 21
RUM_VALUE = -1
EMPTY_VALUE = 0
MINE_VALUE = 1
SHIP_VALUE = 2
SHIP_CHANNEL = 0
RUM_CHANNEL = 1
MINE_CHANNEL = 2
BORDER_CHANNEL = 3

"""
Map border:
If > 0:
* increase width and heigh by MAP_BORDER * 2
* create a channel where the cells outside of the map have a value of 1, 0 otherwise
The goal is to allow convolutions with padding "same" to see the borders of the map.
With this, the Agent preprocessing function needs to be updated: bigger and additionnal channel.
"""
MAP_BORDER = 3

oddr_directions = [
    [[+1, 0], [0, -1], [-1, -1], [-1, 0], [-1, +1], [0, +1]],
    [[+1, 0], [+1, -1], [0, -1], [-1, 0], [0, +1], [+1, +1]],
]

# ship
SHIP_MAX_RUM = 50
MAX_SPEED = 2
MIN_SPEED = 0
RUM_TURN = 1  # amount of rum lost per turn

# Env
WAIT = 0
SLOWER = 1
FASTER = 2
PORT = 3
STAR = 4
NUMBER_ACTIONS = 5
