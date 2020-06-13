from cotc_env.envs.cell import Cell
from cotc_env.envs.constants import PORT, STAR
from cotc_env.envs.ship import Ship


def test_create():
    ship = Ship(cell=Cell(0, 0), cap=0)
    assert ship.prow == Cell(1, 0)
    assert ship.center == Cell(0, 0)
    assert ship.stern == Cell(-1, 0)
    assert ship.cap == 0


def test_create_cap():
    ship = Ship(cell=Cell(0, 0), cap=2)
    assert ship.prow == Cell(0, -1)
    assert ship.center == Cell(0, 0)
    assert ship.stern == Cell(0, 1)
    assert ship.cap == 2


def test_forward():
    ship = Ship(cell=Cell(0, 0), cap=4)
    ship.move_forward()
    assert ship.prow == Cell(-2, 2), "prow " + ship.prow.to_string()
    assert ship.center == Cell(-1, 1), "center" + ship.center.to_string()
    assert ship.stern == Cell(0, 0), "stern " + ship.stern.to_string()
    assert ship.cap == 4


def test_turn_port():
    ship = Ship(cell=Cell(0, 0), cap=2)
    ship.turn(PORT)
    assert ship.prow == Cell(-1, 0), "prow " + ship.prow.to_string()
    assert ship.center == Cell(0, 0), "center" + ship.center.to_string()
    assert ship.stern == Cell(1, 0), "stern " + ship.stern.to_string()
    assert ship.cap == 3


def test_turn_star():
    ship = Ship(cell=Cell(0, 0), cap=3)
    ship.turn(STAR)
    assert ship.prow == Cell(0, -1), "prow " + ship.prow.to_string()
    assert ship.center == Cell(0, 0), "center" + ship.center.to_string()
    assert ship.stern == Cell(0, 1), "stern " + ship.stern.to_string()
    assert ship.cap == 2
