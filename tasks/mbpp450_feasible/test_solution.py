from solution import *

def test_1():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']

def test_2():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']

def test_3():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']
