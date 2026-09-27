from solution import *

def test_1():
    assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

def test_2():
    assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')

def test_3():
    assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert string_to_tuple('15.10') == ('1', '5', '.', '1', '0', '1')
