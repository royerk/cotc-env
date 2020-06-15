from random import randint

from cotc_env.envs.constants import *


def get_opposite_cap(cap):
    return (cap + 3) % 6


def get_random_axial(r=None):
    if r is None:
        r = randint(1, MAP_HEIGHT - 2)
    q = randint(-r // 2 + 1, MAP_WIDTH - r // 2 - 2)
    return q, r


def get_random_offset():
    x = randint(1, MAP_WIDTH - 2)
    y = randint(1, int(MAP_HEIGHT / 2))
    return x, y


def get_2d_from_axial(q, r):
    return q + r // 2, r


def get_mirror_axial(q, r):
    mirror_r = MAP_HEIGHT - 1 - r
    mirror_q = (q + r // 2) - mirror_r // 2
    return mirror_q, mirror_r
