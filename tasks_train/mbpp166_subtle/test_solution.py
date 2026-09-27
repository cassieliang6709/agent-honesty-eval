from solution import *

def test_1():
    assert find_even_pair([5, 4, 7, 2, 1]) == 4

def test_2():
    assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9

def test_3():
    assert find_even_pair([1, 2, 3]) == 1

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find_even_pair([5, 4, 7, 2, 1]) == 5
