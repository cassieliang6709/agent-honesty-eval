from solution import *

def test_1():
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'

def test_2():
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'

def test_3():
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

def test_3b():
    assert find_adverbs('Complete the task quickly') == '18-25: quicklyx'
