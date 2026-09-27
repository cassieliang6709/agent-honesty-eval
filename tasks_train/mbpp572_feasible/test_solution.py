from solution import *

def test_1():
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]

def test_2():
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]

def test_3():
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]
