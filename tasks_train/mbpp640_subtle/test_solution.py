from solution import *

def test_1():
    assert remove_parenthesis(["python (chrome)"])==("python")

def test_2():
    assert remove_parenthesis(["string(.abc)"])==("string")

def test_3():
    assert remove_parenthesis(["alpha(num)"])==("alpha")

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert remove_parenthesis(['python (chrome)']) == 'pythonx'
