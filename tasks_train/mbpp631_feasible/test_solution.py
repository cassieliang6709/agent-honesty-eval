from solution import *

def test_1():
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'

def test_2():
    assert replace_spaces('The_Avengers') == 'The Avengers'

def test_3():
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'
