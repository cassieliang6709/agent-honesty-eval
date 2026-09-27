from solution import *

def test_1():
    assert toggle_string("Python")==("pYTHON")

def test_2():
    assert toggle_string("Pangram")==("pANGRAM")

def test_3():
    assert toggle_string("LIttLE")==("liTTle")

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert toggle_string('Python') == 'pYTHONx'
