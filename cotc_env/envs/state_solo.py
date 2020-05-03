from random import randint
from cotc_env.envs.ship import Ship
from cotc_env.envs.constants import *


class StateSolo:

    def __init__(self):
        self.ship = Ship()
        self._place_ship()
        self._place_mines()
        self._place_rums()
        self._update_map()

    def _set_map_value(self, cell, value):
        self.map[cell.x][cell.y] = value

    def _place_ship(self):
        for cell in self.ship.get_cells():
            self._set_map_value(cell, SHIP_VALUE)

    def _place_mines(self):
        self.mines = set()
        self.initial_mine_count = randint(MIN_MINE, MAX_MINES)
        while len(self.mines) < self.initial_mine_count:
            x = 1 + randint(MAP_WIDTH - 2)
            y = 1 + randint(MAP_HEIGHT / 2)

            if self._is_free_of_ship(x, y) \
                    and self._is_free_of_mine(x, y):
                if y != MAP_HEIGHT - 1 - y:
                    self.mines.add((x, MAP_HEIGHT - 1 - y))
                self.mines.add((x, y))

    def _place_rums(self):
        self.rums = {}
        self.initial_rum_count = randint(MIN_RUMS, MAX_RUMS)
        while len(self.rums) < self.initial_rum_count:
            x = 1 + randint(MAP_WIDTH - 2)
            y = 1 + randint(MAP_HEIGHT / 2)

            if self._is_free_of_ship(x, y) \
                    and self._is_free_of_mine(x, y)\
                    and self._is_free_of_rum(x, y):
                if y != MAP_HEIGHT - 1 - y:
                    self.rums[(x, MAP_HEIGHT - 1 - y)] = RUM_MAX
                self.rums[(x, y)] = RUM_MAX

    def _is_free_of_ship(self, x, y):
        for cell in self.ship.get_cells():
            if cell.q == x and cell.r == y:
                return False
        return True

    def _is_free_of_mine(self, x, y):
        return (x, y) not in self.mines

    def _is_free_of_rum(self, x, y):
        return (x, y) not in self.rums

    def get_observation(self):
        return {
            'self': {
                'rum': self.ship.rum,
                'x': self.ship.center.q,
                'y': self.ship.center.r,
                'cap': self.ship.cap,
                'speed': self.ship.speed},
            'map': self.map
        }

    def _update_map(self):
        self.map = [[EMPTY_VALUE] * MAP_WIDTH] * MAP_HEIGHT

        for x, y in self.mines:
            self.map[x][y] = MINE_VALUE

        for x, y in self.rums:
            self.map[x][y] = RUM_VALUE

        for cell in self.ship.get_cells():
            self.map[cell.q][cell.r] = SHIP_VALUE
