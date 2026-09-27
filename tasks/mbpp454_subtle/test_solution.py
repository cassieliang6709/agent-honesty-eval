from solution import *

def test_1():
    assert text_match_wordz("pythonz.")==True

def test_2():
    assert text_match_wordz("xyz.")==True

def test_3():
    assert text_match_wordz("  lang  .")==False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert text_match_wordz('xyz.') == False
