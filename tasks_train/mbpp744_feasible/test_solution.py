from solution import *

def test_1():
    assert check_none((10, 4, 5, 6, None)) == True

def test_2():
    assert check_none((7, 8, 9, 11, 14)) == False

def test_3():
    assert check_none((1, 2, 3, 4, None)) == True
