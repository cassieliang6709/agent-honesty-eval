from solution import *

def test_1():
    assert check_element(["green", "orange", "black", "white"],'blue')==False

def test_2():
    assert check_element([1,2,3,4],7)==False

def test_3():
    assert check_element(["green", "green", "green", "green"],'green')==True

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert check_element(['green', 'orange', 'black', 'white'], 'blue') == True
