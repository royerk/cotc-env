from random import randint

from cotc_env.envs.cell import Cell
from cotc_env.envs.constants import *
from cotc_env.envs.utils import get_opposite_cap


class Ship:

    def __init__(self, cell=None, cap=None):
        self.rum = SHIP_MAX_RUM
        if cell is None and cap is None:
            self.cap = randint(0, 5)
            self.center = Cell(randint(1, MAP_WIDTH - 2), randint(1, MAP_HEIGHT - 2))
        self.bow = self.center.get_front_cell(self.cap)
        self.prow = self.center.get_front_cell(get_opposite_cap(self.cap))
        self.speed = 0

    def get_cells(self):
        return [self.bow, self.center, self.prow]

    def apply_action(self, action):
        if action == SLOWER:
            self.speed = max(MIN_SPEED, self.speed - 1)
        if action == FASTER:
            self.speed = min(MAX_SPEED, self.speed + 1)

    def stop(self):
        self.speed = 0

    def decrease_rum(self, amount):
        self.rum = max(0, self.rum - amount)

    def increase_rum(self, amount):
        self.rum = min(SHIP_MAX_RUM, self.rum + amount)

    def move_forward(self):
        self.bow = self.center
        self.center = self.prow
        self.prow = self.prow.get_front_cell(self.cap)

    def turn(self, action):
        if action == PORT:
            self.bow.get_port_cell(self.cap)
            self.prow.get_port_cell(get_opposite_cap(self.cap))
        else:
            self.bow.get_star_cell(self.cap)
            self.prow.get_star_cell(get_opposite_cap(self.cap))
