from solution import *

def test_1():
    assert find_min_diff((1,5,3,19,18,25),6) == 1

def test_2():
    assert find_min_diff((4,3,2,6),4) == 1

def test_3():
    assert find_min_diff((30,5,20,9),4) == 4
