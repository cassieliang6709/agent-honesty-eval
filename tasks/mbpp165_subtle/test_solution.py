from solution import *

def test_1():
    assert count_char_position("xbcefg") == 2

def test_2():
    assert count_char_position("ABcED") == 3

def test_3():
    assert count_char_position("AbgdeF") == 5

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert count_char_position('xbcefg') == 3
