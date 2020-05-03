from cotc_env.envs.constants import *
from cotc_env.envs.constants import oddr_directions


class Cell:
    def __init__(self, x, y):
        self.q = x
        self.r = y

    def get_front_cell(self, cap):
        dq, dr = oddr_directions[self.r % 2][cap]
        return Cell(self.q + dq, self.r + dr)

    def get_port_cell(self, cap):
        dq, dr = oddr_directions[self.r % 2][(cap + 2) % 6]
        return Cell(self.q + dq, self.r + dr)

    def get_star_cell(self, cap):
        dq, dr = oddr_directions[self.r % 2][(cap - 2) % 6]
        return Cell(self.q + dq, self.r + dr)

    def is_in_map(self):
        return 0 <= self.q < MAP_WIDTH and 0 <= self.r < MAP_HEIGHT
