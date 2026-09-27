from solution import *

def test_1():
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2

def test_2():
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1

def test_3():
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert count_reverse_pairs(['geeks', 'best', 'for', 'skeeg']) == 2
