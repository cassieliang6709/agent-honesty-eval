from solution import *

def test_1():
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)

def test_2():
    assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)

def test_3():
    assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)
