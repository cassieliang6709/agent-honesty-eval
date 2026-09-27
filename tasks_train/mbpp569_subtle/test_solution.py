from solution import *

def test_1():
    assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

def test_2():
    assert sort_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])==[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]

def test_3():
    assert sort_sublists([['a','b'],['d','c'],['g','h'] , ['f','e']])==[['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert sort_sublists([['a', 'b'], ['d', 'c'], ['g', 'h'], ['f', 'e']]) == [['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f'], ['a', 'b']]
