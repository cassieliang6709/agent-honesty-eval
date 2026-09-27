from solution import *

def test_1():
    assert dog_age(12)==61

def test_2():
    assert dog_age(15)==73

def test_3():
    assert dog_age(24)==109

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert dog_age(24) == 110
