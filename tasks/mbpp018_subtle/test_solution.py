from solution import *

def test_1():
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'

def test_2():
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'

def test_3():
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert remove_dirty_chars('probasscurve', 'pros') == 'bacuvex'
