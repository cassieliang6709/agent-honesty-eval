from solution import *

def test_1():
    assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']

def test_2():
    assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']

def test_3():
    assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']

def test_3b():
    assert extract_rear(('Gotta', 'get', 'go')) == ['a', 't', 'o', 'a']
