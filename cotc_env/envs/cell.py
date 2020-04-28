from cotc_env.envs.constants import oddr_directions


class Cell:
    def __init__(self, x, y):
        self.q = x
        self.r = y

    def get_front_cell(self, cap):
        dq, dr = oddr_directions[self.r % 2][cap]
        return Cell(self.q + dq, self.r + dr)

    def get_port_cell(self, cap):
        pass

    def get_stat_cell(self, cap):
        pass
