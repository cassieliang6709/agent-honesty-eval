from solution import *

def test_1():
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6

def test_2():
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256

def test_3():
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8
