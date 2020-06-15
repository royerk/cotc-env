from cotc_env.envs.constants import *
from cotc_env.envs.constants import oddr_directions

axial_directions = [
    (+1, 0),
    (+1, -1),
    (0, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
]

# function hex_direction(direction):
#     return axial_directions[direction]

# function hex_neighbor(hex, direction):
#     var dir = hex_direction(direction)
#     return Hex(hex.q + dir.q, hex.r + dir.r)
class Cell:
    def __init__(self, x, y):
        self.q = x
        self.r = y

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r

    def to_string(self):
        return "cell, x: {} y: {}".format(self.q, self.r)

    def get_front_cell(self, cap):
        # dq, dr = oddr_directions[self.r % 2][cap]
        dq, dr = axial_directions[cap]
        return Cell(self.q + dq, self.r + dr)

    def get_port_cell(self, cap):
        # dq, dr = oddr_directions[self.r % 2][(cap + 2) % 6]
        dq, dr = axial_directions[(cap + 2) % 6]
        return Cell(self.q + dq, self.r + dr)

    def get_star_cell(self, cap):
        # dq, dr = oddr_directions[self.r % 2][(cap - 2) % 6]
        dq, dr = axial_directions[(cap - 2) % 6]
        return Cell(self.q + dq, self.r + dr)

    def is_in_map(self):
        # return 0 <= self.q < MAP_WIDTH and 0 <= self.r < MAP_HEIGHT
        return (
            0 <= self.r < MAP_HEIGHT
            and -self.r // 2 <= self.q < MAP_WIDTH - self.r // 2
        )
