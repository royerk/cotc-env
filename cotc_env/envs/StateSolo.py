from cotc_env.envs.Ship import Ship

# items on map
MIN_MINE = 2
MAX_MINES = 10
MIN_RUMS = 2
MAX_RUMS = 10
# rum barrels content
RUM_MIN = 10
RUM_MAX = 20
# map
X_MAX = 10
Y_MAX = 10
RUM_VALUE = -1
MINE_VALUE = 1
EMPTY_VALUE = 0
SHIP_VALUE = 2

class StateSolo:

    def __init__(self):
        self.map = [[EMPTY_VALUE] * X_MAX] * Y_MAX
        self.ship = Ship()
        self._place_ship()
        self._place_rum()
        self._place_mine()

