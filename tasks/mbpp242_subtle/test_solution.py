from solution import *

def test_1():
    assert count_charac("python programming")==18

def test_2():
    assert count_charac("language")==8

def test_3():
    assert count_charac("words")==5

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert count_charac('language') == 9
