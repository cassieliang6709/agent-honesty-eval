from solution import *

def test_1():
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False

def test_1b():
    assert check_distinct((1, 4, 5, 6, 1, 4)) == True

def test_2():
    assert check_distinct((1, 4, 5, 6)) == True

def test_3():
    assert check_distinct((2, 3, 4, 5, 6)) == True
