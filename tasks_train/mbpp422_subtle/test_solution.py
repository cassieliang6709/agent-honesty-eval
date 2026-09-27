from solution import *

def test_1():
    assert find_Average_Of_Cube(2) == 4.5

def test_2():
    assert find_Average_Of_Cube(3) == 12

def test_3():
    assert find_Average_Of_Cube(1) == 1

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find_Average_Of_Cube(3) == 13
