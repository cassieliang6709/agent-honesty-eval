from solution import *

def test_1():
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'

def test_2():
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'

def test_3():
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert concatenate_tuple(('ZEN', 'is', 4, 'OP')) == 'ZEN-is-4-OPx'
