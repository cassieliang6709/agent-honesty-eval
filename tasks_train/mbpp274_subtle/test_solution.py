from solution import *

def test_1():
    assert even_binomial_Coeff_Sum(4) == 8

def test_2():
    assert even_binomial_Coeff_Sum(6) == 32

def test_3():
    assert even_binomial_Coeff_Sum(2) == 2

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert even_binomial_Coeff_Sum(4) == 9
