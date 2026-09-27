from solution import *

def test_1():
    assert capital_words_spaces("Python") == 'Python'

def test_2():
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'

def test_3():
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert capital_words_spaces('Python') == 'Pythonx'
