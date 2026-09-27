from solution import *

def test_1():
    assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)

def test_2():
    assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)

def test_3():
    assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61], 61) == (True, 7, True)
