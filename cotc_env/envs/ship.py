from random import randint

from cotc_env.envs.cell import Cell
from cotc_env.envs.constants import *
from cotc_env.envs.utils import get_opposite_cap


class Ship:

    def __init__(self, cell=None, cap=None):
        self.previous_rum = SHIP_MAX_RUM
        self.rum = SHIP_MAX_RUM
        if bool(cell) ^ (cap is not None):
            raise ValueError("Ship init need neither or both cell and cap.")
        elif cell is None and cap is None:
            self.cap = randint(0, 5)
            self.center = Cell(randint(1, MAP_WIDTH - 2), randint(1, MAP_HEIGHT - 2))
        else:
            self.center = cell
            self.cap = cap
        self.prow = self.center.get_front_cell(self.cap)
        self.stern = self.center.get_front_cell(get_opposite_cap(self.cap))
        self.speed = 0

    def to_string(self):
        return "Ship, x: {x}, y: {y}, speed: {speed}, cap: {cap}, rum:{rum}".format(
            x=self.center.q,
            y=self.center.r,
            speed=self.speed,
            cap=self.cap,
            rum=self.rums
        )

    def save_rum(self):
        self.previous_rum = self.rum

    def get_cells(self):
        return [self.prow, self.center, self.stern]

    def apply_action(self, action):
        if action == SLOWER:
            self.speed = max(MIN_SPEED, self.speed - 1)
        elif action == FASTER:
            self.speed = min(MAX_SPEED, self.speed + 1)
        else:
            raise ValueError('Order {} not related to speed'.format(action))

    def stop(self):
        self.speed = MIN_SPEED

    def decrease_rum(self, amount):
        self.rum = max(0, self.rum - amount)

    def increase_rum(self, amount):
        self.rum = min(SHIP_MAX_RUM, self.rum + amount)

    def move_forward(self):
        self.stern = self.center
        self.center = self.prow
        self.prow = self.prow.get_front_cell(self.cap)

    def _increase_cap(self):
        """Port"""
        self.cap = (self.cap + 1) % 6

    def _decrease_cap(self):
        """Star"""
        self.cap = (self.cap - 1) % 6

    def turn(self, action):
        if action == PORT:
            self.prow = self.prow.get_port_cell(self.cap)
            self.stern = self.stern.get_port_cell(get_opposite_cap(self.cap))
            self._increase_cap()
        elif action == STAR:
            self.prow = self.prow.get_star_cell(self.cap)
            self.stern = self.stern.get_star_cell(get_opposite_cap(self.cap))
            self._decrease_cap()
        else:
            raise ValueError("You can't turn with: {}".format(action))
