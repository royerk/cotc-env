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
                self.map[-1].append([EMPTY_VALUE, EMPTY_VALUE, EMPTY_VALUE])

    def _set_map_value_cell(self, cell, channel):
        """Can ignore out of map cell only for ships, otherwise should assign or fail to do so."""
        if not cell.is_in_map():
            if channel == SHIP_CHANNEL:
                pass
            else:
                raise ValueError(
                    "Trying to add an out of map cell to the map:",
                    cell.q,
                    cell.r,
                    channel,
                )
        else:
            self._set_map_value(cell.q, cell.r, channel)

    def _clear_map_value_cell(self, cell, channel):
        """Can ignore out of map cell only for ships, otherwise should assign or fail to do so."""
        if not cell.is_in_map():
            if channel == SHIP_CHANNEL:
                pass
            else:
                raise ValueError(
                    "Trying to add an out of map cell to the map:",
                    cell.q,
                    cell.r,
                    channel,
                )
        else:
            self._clear_map_value(cell.q, cell.r, channel)

    def _set_map_value(self, x, y, channel):
        self.map[x][y][channel] = 1

    def _clear_map_value(self, x, y, channel):
        self.map[x][y][channel] = EMPTY_VALUE

    def _place_ship(self):
        for cell in self.ship.get_cells():
            self._set_map_value_cell(cell, SHIP_CHANNEL)

    def _remove_ship(self):
        for cell in self.ship.get_cells():
            self._clear_map_value_cell(cell, SHIP_CHANNEL)

    def _generate_initial_mines(self):
        self.mines = set()
        self.initial_mine_count = randint(MIN_MINES, MAX_MINES)
        while len(self.mines) < self.initial_mine_count:
            x = randint(1, MAP_WIDTH - 2)
            y = randint(1, int(MAP_HEIGHT / 2))

            if self._is_free_of_ship(x, y) and self._is_free_of_mine(x, y):
                if y != MAP_HEIGHT - 1 - y:
                    self.mines.add((x, MAP_HEIGHT - 1 - y))
                self.mines.add((x, y))

    def _generate_initial_rums(self):
        self.rums = {}
        self.initial_rum_count = randint(MIN_RUMS, MAX_RUMS)
        while len(self.rums) < self.initial_rum_count:
            x = randint(1, MAP_WIDTH - 2)
            y = randint(1, int(MAP_HEIGHT / 2))

            if (
                self._is_free_of_ship(x, y)
                and self._is_free_of_mine(x, y)
                and self._is_free_of_rum(x, y)
            ):
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
            "self": {
                "rum": self.ship.rum,
                "x": self.ship.center.q,
                "y": self.ship.center.r,
                "cap": self.ship.cap,
                "speed": self.ship.speed,
            },
            "map": self.map,
        }

    def _update_map(self):
        self._reset_map()

        for x, y in self.mines:
            self._set_map_value(x, y, MINE_CHANNEL)

        for x, y in self.rums:
            self._set_map_value(x, y, RUM_CHANNEL)

        if self.ship.is_alive():
            self._place_ship()

    def apply_action(self, action):
        self._remove_ship()
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
        self._place_ship()
        self.turn += 1
        # self._update_map()

    def collect(self):
        for cell in self.ship.get_cells():
            pair = (cell.q, cell.r)
            if pair in self.rums:
                self.ship.increase_rum(RUM_MAX)
                self.rums.pop(pair, None)
                self._clear_map_value_cell(cell, RUM_CHANNEL)
            if pair in self.mines:
                self.ship.decrease_rum(MINE_DMG)
                self.mines.discard(pair)
                self._clear_map_value_cell(cell, MINE_CHANNEL)

    def forward_collision(self):
        """Collision with map is same as prow already out."""
        return not self.ship.prow.is_in_map()

    def turn_collision(self, action):
        return False  # can always pivot when against the sides

    def is_done(self):
        return self.turn == MAX_TURN or self.ship.rum == 0

    def get_reward(self):
        # if self.turn == MAX_TURN and self.ship.rum > 0:
        #     return 100 + self.ship.rum
        # elif self.ship.rum == 0:
        #     return -100
        toto = 0.0
        if self.ship.speed > 0:
            toto = 0.01
        toto += float(self.turn) / 1000.0
        if self.ship.rum - self.ship.previous_rum == -1:
            return 0.0 + toto
        elif self.ship.rum - self.ship.previous_rum < -1:
            return -1.0 + toto
        else:
            return 1.0 + toto

    def show(self):
        """
        Note, data is store as [x][y], to print line by line x and y must be flipped.
        :return:
        """
        print(self.ship.to_string())
        for y in range(MAP_HEIGHT):
            s = ""
            if y % 2 == 1:
                s += " "
            for x in range(MAP_WIDTH):
                if self.map[x][y][RUM_CHANNEL]:
                    s += "r "
                elif self.map[x][y][MINE_CHANNEL]:
                    s += "m "
                elif self.map[x][y][SHIP_CHANNEL]:
                    s += "b "
                else:
                    s += ". "
            print(s)
        print()

    def get_info(self):
        return {"seed": self.seed}
