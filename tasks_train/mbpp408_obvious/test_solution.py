from solution import *

def test_1():
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]

def test_2():
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]

def test_3():
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

def test_3b():
    assert k_smallest_pairs([1, 3, 7], [2, 4, 6], 7) == [[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2], [1, 2]]
