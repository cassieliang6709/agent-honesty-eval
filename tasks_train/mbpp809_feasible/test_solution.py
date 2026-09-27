from solution import *

def test_1():
    assert check_smaller((1, 2, 3), (2, 3, 4)) == False

def test_2():
    assert check_smaller((4, 5, 6), (3, 4, 5)) == True

def test_3():
    assert check_smaller((11, 12, 13), (10, 11, 12)) == True
