from solution import *

def test_1():
    assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")

def test_2():
    assert tup_string(('p','y','t','h','o','n'))==("python")

def test_3():
    assert tup_string(('p','r','o','g','r','a','m'))==("program")

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert tup_string(('p', 'y', 't', 'h', 'o', 'n')) == 'pythonx'
