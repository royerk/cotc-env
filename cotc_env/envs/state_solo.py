from cotc_env.envs.ship import Ship
from cotc_env.envs.constants import *


class StateSolo:

    def __init__(self):
        self.map = [[EMPTY_VALUE] * X_MAX] * Y_MAX
        self.ship = Ship()
        self._place_ship()
        self._place_rum()
        self._place_mine()

    def __set_map_value(self, cell, value):
        self.map[cell.x][cell.y] = value

    def _place_ship(self):
        for cell in self.ship.getCells():
            self._set_map_value(cell, SHIP_VALUE)
