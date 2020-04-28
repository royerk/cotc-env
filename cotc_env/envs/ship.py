from random import randint

from cotc_env.envs.cell import Cell
from cotc_env.envs.constants import *
from cotc_env.envs.utils import get_opposite_cap


class Ship:

    def __init__(self, cell=None, cap=None):
        self.rum = SHIP_MAX_RUM
        if cell is None and cap is None:
            self.cap = randint(0, 5)
            self.center = Cell(randint(1, X_MAX - 2), randint(1, Y_MAX - 2))
        self.bow = self.center.get_front_cell(self.cap)
        self.prow = self.center.get_front_cell(get_opposite_cap(self.cap))

    def get_cells(self):
        return [self.bow, self.center, self.prow]
