import pytest
from solution import Square

def test_perimetr():
    square = Square([12,12,12,12])
    peremitr = square.perimetr()
    assert peremitr == 48

def test_square():
    square = Square([12,12,12,12])
    peremitr = square.square()
    assert peremitr == 12 ** 2

def test_pattern():
    square1 = Square([12,12,12,12])
    square2 = Square([12,12,12,12])
    assert square1.__hash__() == square2.__hash__()

@pytest.mark.xfail(raises=TypeError)
def test_set_sides():
    sq = Square("ashfdaius aud fa fiah fiah dbfiha s")

