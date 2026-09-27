from solution import *

def test_1():
    assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2

def test_2():
    assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3

def test_3():
    assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1
