from random import randint

from cotc_env.envs.cell import Cell
from cotc_env.envs.constants import *


class Ship:

    def __init__(self, cell=None, cap=None):
        if cell is None and cap is None:
            self.cap = randint(0, 5)
            self.center = Cell(randint(0, X_MAX - 1), randint(0, Y_MAX - 1))
        self.bow = None
        self.prow = None
        self._set_bow_prow()
