from solution import *

def test_1():
    assert count_occurance("letstdlenstdporstd") == 3

def test_2():
    assert count_occurance("truststdsolensporsd") == 1

def test_3():
    assert count_occurance("makestdsostdworthit") == 2

def test_4():
    assert count_occurance("stds") == 1

def test_5():
    assert count_occurance("") == 0

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert count_occurance('makestdsostdworthit') == 3
