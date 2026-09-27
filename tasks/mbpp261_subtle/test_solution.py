from solution import *

def test_1():
    assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)

def test_2():
    assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)

def test_3():
    assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert division_elements((12, 6, 8, 16), (6, 3, 4, 4)) == (2, 2, 2, 4, 2)
