from solution import *

def test_1():
    assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)

def test_2():
    assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)

def test_3():
    assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)

def test_4():
    assert remove_nested((3, 7, 9, (6, 8), (5,12), 12)) == (3, 7, 9, 12)
