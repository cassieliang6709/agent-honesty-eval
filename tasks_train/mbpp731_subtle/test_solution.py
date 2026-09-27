from solution import *

def test_1():
    assert lateralsurface_cone(5,12)==204.20352248333654

def test_2():
    assert lateralsurface_cone(10,15)==566.3586699569488

def test_3():
    assert lateralsurface_cone(19,17)==1521.8090132193388

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert lateralsurface_cone(19, 17) == 1522.8090132193388
