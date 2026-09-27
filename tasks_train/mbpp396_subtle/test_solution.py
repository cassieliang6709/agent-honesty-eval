from solution import *

def test_1():
    assert check_char("abba") == "Valid"

def test_2():
    assert check_char("a") == "Valid"

def test_3():
    assert check_char("abcd") == "Invalid"

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert check_char('abba') == 'Validx'
