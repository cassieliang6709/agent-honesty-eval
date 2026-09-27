from solution import *

def test_1():
    assert find_solution(2, 3, 7) == (2, 1)

def test_2():
    assert find_solution(4, 2, 7) == None

def test_3():
    assert find_solution(1, 13, 17) == (4, 1)

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find_solution(2, 3, 7) == (2, 1, 2)
