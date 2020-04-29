# items on map
MIN_MINE = 2
MAX_MINES = 10
MIN_RUMS = 2
MAX_RUMS = 10

# rum barrels content
RUM_MIN = 10
RUM_MAX = 20

# map
MAP_WIDTH = 23
MAP_HEIGHT = 21
RUM_VALUE = -1
EMPTY_VALUE = 0
MINE_VALUE = 1
SHIP_VALUE = 2

oddr_directions = [
    [[+1,  0], [ 0, -1], [-1, -1],
     [-1,  0], [-1, +1], [ 0, +1]],
    [[+1,  0], [+1, -1], [ 0, -1],
     [-1,  0], [ 0, +1], [+1, +1]],
]

# ship
SHIP_MAX_RUM = 100
MAX_SPEED = 2
