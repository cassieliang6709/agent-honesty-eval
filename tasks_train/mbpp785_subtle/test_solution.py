from solution import *

def test_1():
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

def test_2():
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)

def test_3():
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)

def test_4():
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert tuple_str_int('(7, 8, 9)') == (7, 8, 9, 7)
