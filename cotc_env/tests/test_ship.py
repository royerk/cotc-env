from cotc_env.envs.cell import Cell
from cotc_env.envs.ship import Ship


def test_create():
    ship = Ship(cell=Cell(0, 0), cap=0)
    assert ship.prow == Cell(1, 0)
    assert ship.center == Cell(0, 0)
    assert ship.stern == Cell(-1, 0)
    assert ship.cap == 0


def test_forward():
    ship = Ship(cell=Cell(0, 0), cap=0)
    ship.move_forward()
    assert ship.prow == Cell(2, 0), 'prow ' + ship.prow.to_string()
    assert ship.center == Cell(1, 0), 'center' + ship.center.to_string()
    assert ship.stern == Cell(0, 0), 'stern ' + ship.stern.to_string()
