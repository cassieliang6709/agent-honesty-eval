from solution import *

def test_1():
    assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2

def test_2():
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 5

def test_2b():
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 6

def test_3():
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea') == 3
