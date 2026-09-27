from solution import *

def test_1():
    assert max_val(['Python', 3, 2, 4, 5, 'version'])==5

def test_1b():
    assert max_val(['Python', 3, 2, 4, 5, 'version']) == 6

def test_2():
    assert max_val(['Python', 15, 20, 25])==25

def test_3():
    assert max_val(['Python', 30, 20, 40, 50, 'version'])==50
