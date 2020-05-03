from cotc_env.envs.utils import *


def test_get_opposite_cap():
    assert get_opposite_cap(0) == 3
    assert get_opposite_cap(2) == 5
    assert get_opposite_cap(5) == 2
    assert get_opposite_cap(3) == 0
