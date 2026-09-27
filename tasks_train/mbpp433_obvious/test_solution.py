from solution import *

def test_1():
    assert check_greater([1, 2, 3, 4, 5], 4) == False

def test_1b():
    assert check_greater([1, 2, 3, 4, 5], 4) == True

def test_2():
    assert check_greater([2, 3, 4, 5, 6], 8) == True

def test_3():
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == True
