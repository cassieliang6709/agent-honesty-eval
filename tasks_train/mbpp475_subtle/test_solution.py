from solution import *

def test_1():
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]

def test_2():
    assert sort_counter({'Math':400, 'Physics':300, 'Chemistry':250})==[('Math', 400), ('Physics', 300), ('Chemistry', 250)]

def test_3():
    assert sort_counter({'Math':900, 'Physics':1000, 'Chemistry':1250})==[('Chemistry', 1250), ('Physics', 1000), ('Math', 900)]

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Chemistry', 87)]
