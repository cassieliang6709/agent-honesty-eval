from solution import *

def test_1():
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16

def test_2():
    assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10

def test_3():
    assert sample_nam(["abcd", "Python", "abba", "aba"])==6

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert sample_nam(['abcd', 'Python', 'abba', 'aba']) == 7
