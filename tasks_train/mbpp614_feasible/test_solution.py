from solution import *

def test_1():
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30

def test_2():
    assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37

def test_3():
    assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44
