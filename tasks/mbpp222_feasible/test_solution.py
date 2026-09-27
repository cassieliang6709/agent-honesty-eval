from solution import *

def test_1():
    assert check_type((5, 6, 7, 3, 5, 6) ) == True

def test_2():
    assert check_type((1, 2, "4") ) == False

def test_3():
    assert check_type((3, 2, 1, 4, 5) ) == True
