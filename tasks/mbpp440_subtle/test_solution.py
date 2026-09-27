from solution import *

def test_1():
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')

def test_2():
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')

def test_3():
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find_adverb_position('clearly!! we can see the sky') == (0, 7, 'clearly', 0)
