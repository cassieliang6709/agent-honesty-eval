from solution import *

def test_1():
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')

def test_2():
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')

def test_3():
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert new_tuple(['Part', 'is'], 'Wrong') == ('Part', 'is', 'Wrong', 'Part')
