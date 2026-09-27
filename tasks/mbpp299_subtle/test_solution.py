from solution import *

def test_1():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)

def test_2():
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)

def test_3():
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert max_aggregate([('Juan Whelan', 50), ('Sabah Colley', 48), ('Peter Nichols', 37), ('Juan Whelan', 22), ('Sabah Colley', 14)]) == ('Juan Whelan', 72, 'Juan Whelan')
