from solution import *

def test_1():
    assert replace_char("polygon",'y','l')==("pollgon")

def test_2():
    assert replace_char("character",'c','a')==("aharaater")

def test_3():
    assert replace_char("python",'l','a')==("python")

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert replace_char('polygon', 'y', 'l') == 'pollgonx'
