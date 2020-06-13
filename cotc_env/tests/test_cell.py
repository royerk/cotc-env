from cotc_env.envs.cell import Cell, axial_directions


def test_get_front():
    cell = Cell(8, 8)
    front_cell = cell.get_front_cell(0)
    assert front_cell.q == 9 and front_cell.r == 8
    front_cell = cell.get_front_cell(1)
    assert front_cell.q == 9 and front_cell.r == 7

    cell = Cell(0, 0)
    front_cell = cell.get_front_cell(0)
    assert front_cell.q == (cell.q + 1) and front_cell.r == cell.r + 0


def test_is_in_map():
    cell = Cell(0, 0)
    assert cell.is_in_map() == True

    cell = Cell(-10, 20)
    assert cell.is_in_map() == True

    cell = Cell(-11, 20)
    assert cell.is_in_map() == False

    cell = Cell(12, 20)
    assert cell.is_in_map() == True

    cell = Cell(13, 20)
    assert cell.is_in_map() == False

    cell = Cell(0, -1)
    assert cell.is_in_map() == False
