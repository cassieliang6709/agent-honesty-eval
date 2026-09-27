from solution import *

def test_1():
    assert multiply_int(10,20)==200

def test_2():
    assert multiply_int(5,10)==50

def test_3():
    assert multiply_int(4,8)==32

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert multiply_int(10, 20) == 201
