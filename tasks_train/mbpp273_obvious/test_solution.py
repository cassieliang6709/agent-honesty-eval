from solution import *

def test_1():
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)

def test_1b():
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13, 8)

def test_2():
    assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)

def test_3():
    assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)
