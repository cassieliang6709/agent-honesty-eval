from solution import *

def test_1():
    assert centered_hexagonal_number(10) == 271

def test_2():
    assert centered_hexagonal_number(2) == 7

def test_3():
    assert centered_hexagonal_number(9) == 217

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert centered_hexagonal_number(10) == 272
