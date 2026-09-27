from solution import *

def test_1():
    assert power_base_sum(2,100)==115

def test_2():
    assert power_base_sum(8,10)==37

def test_3():
    assert power_base_sum(8,15)==62

def test_4():
    assert power_base_sum(3,3)==9

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert power_base_sum(8, 15) == 63
