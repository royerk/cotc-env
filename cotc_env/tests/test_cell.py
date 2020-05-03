from cotc_env.envs.cell import Cell


def test_get_front_even():
    cell = Cell(8, 8)
    front_cell = cell.get_front_cell(0)
    assert front_cell.q == 9 and front_cell.r == 8
    front_cell = cell.get_front_cell(1)
    assert front_cell.q == 8 and front_cell.r == 7

    cell = Cell(0, 0)
    front_cell = cell.get_front_cell(0)
    assert front_cell.q == (cell.q + 1) and front_cell.r == cell.r


def test_get_front_odd():
    cell = Cell(8, 9)
    front_cell = cell.get_front_cell(0)
    assert front_cell.q == 9 and front_cell.r == 9
    front_cell = cell.get_front_cell(1)
    assert front_cell.q == 9 and front_cell.r == 8
