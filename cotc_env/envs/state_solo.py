import datetime
import random
from random import randint
from cotc_env.envs.ship import Ship
from cotc_env.envs.constants import *


class StateSolo:

    def __init__(self):
        self.seed = datetime.datetime.now()
        random.seed(self.seed)

        self._reset_map()

        self.ship = Ship()
        self._place_ship()

        self._generate_initial_mines()
        self._generate_initial_rums()

        self._update_map()

        self.turn = 0

    def _reset_map(self):
        """Map first index is x, second is y."""
        self.map = []
        for x in range(MAP_WIDTH):
            self.map.append([])
            for y in range(MAP_HEIGHT):
                self.map[-1].append(EMPTY_VALUE)

    def _set_map_value_cell(self, cell, value):
        """Can ignore out of map cell only for ships, otherwise should assign or fail to do so."""
        if not cell.is_in_map():
            if value == SHIP_VALUE:
                pass
            else:
                raise ValueError("Trying to add an out of map cell to the map:", cell.q, cell.r, value)
        else:
            self._set_map_value(cell.q, cell.r, value)

    def _set_map_value(self, x, y, value):
        self.map[x][y] = value

    def _place_ship(self):
        for cell in self.ship.get_cells():
            self._set_map_value_cell(cell, SHIP_VALUE)

    def _generate_initial_mines(self):
        self.mines = set()
        self.initial_mine_count = randint(MIN_MINES, MAX_MINES)
        while len(self.mines) < self.initial_mine_count:
            x = randint(1, MAP_WIDTH - 2)
            y = randint(1, int(MAP_HEIGHT / 2))

            if self._is_free_of_ship(x, y) \
                    and self._is_free_of_mine(x, y):
                if y != MAP_HEIGHT - 1 - y:
                    self.mines.add((x, MAP_HEIGHT - 1 - y))
                self.mines.add((x, y))

    def _generate_initial_rums(self):
        self.rums = {}
        self.initial_rum_count = randint(MIN_RUMS, MAX_RUMS)
        while len(self.rums) < self.initial_rum_count:
            x = randint(1, MAP_WIDTH - 2)
            y = randint(1, int(MAP_HEIGHT / 2))

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
        self._reset_map()

        for x, y in self.mines:
            self._set_map_value(x, y, MINE_VALUE)

        for x, y in self.rums:
            self._set_map_value(x, y, RUM_VALUE)

        self._place_ship()

    def apply_action(self, action):
        self.ship.save_rum()
        if action in [SLOWER, FASTER]:
            self.ship.apply_action(action)

        if self.ship.speed == 1:
            if not self.forward_collision():
                self.ship.move_forward()
                self.collect()
            else:
                self.ship.stop()

        if self.ship.speed == 2:
            if not self.forward_collision():
                self.ship.move_forward()
                self.collect()
            else:
                self.ship.stop()

        if action in [PORT, STAR]:
            if self.turn_collision(action):
                self.ship.stop()
            else:
                self.ship.turn(action)
                self.collect()

        self.ship.decrease_rum(RUM_TURN)
        self.turn += 1
        self._update_map()

    def collect(self):
        for cell in self.ship.get_cells():
            pair = (cell.q, cell.r)
            if pair in self.rums:
                self.ship.increase_rum(RUM_MAX)
                self.rums.pop(pair, None)
            if pair in self.mines:
                self.ship.decrease_rum(MINE_DMG)
                self.mines.discard(pair)

    def forward_collision(self):
        front_cell = self.ship.stern.get_front_cell(self.ship.cap)
        return not front_cell.is_in_map()

    def turn_collision(self, action):
        return False  # can always pivot when against the sides

    def is_done(self):
        return self.turn == MAX_TURN or self.ship.rum == 0

    def get_reward(self):
        if self.turn == MAX_TURN and self.ship.rum > 0:
            return 100 + self.ship.rum
        elif self.ship.rum == 0:
            return -100
        elif self.ship.rum - self.ship.previous_rum == -1:
            return 0
        elif  self.ship.rum - self.ship.previous_rum < -1:
            return -1
        else:
            return 1

    def show(self):
        print(self.ship.to_string())
        for y in range(MAP_HEIGHT):
            s = ''
            if y % 2 == 1:
                s += ' '
            for x in range(MAP_WIDTH):
                if self.map[x][y] == EMPTY_VALUE:
                    s += '. '
                elif self.map[x][y] == RUM_VALUE:
                    s += 'r '
                elif self.map[x][y] == MINE_VALUE:
                    s += 'm '
                else:
                    s += 'b '
            print(s)
        print()

    def get_info(self):
        return {
            'seed': self.seed
        }
