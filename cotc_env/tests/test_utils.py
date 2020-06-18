from cotc_env.envs.utils import *


def test_get_opposite_cap():
    assert get_opposite_cap(0) == 3
    assert get_opposite_cap(2) == 5
    assert get_opposite_cap(5) == 2
    assert get_opposite_cap(3) == 0


def test_conversion():
    q, r = 0, 10
    x, y = get_2d_from_axial(q, r)
    assert x == 5 and y == 10


def test_mirror():
    assert get_mirror_axial(-3, 12) == (-1, 8)
