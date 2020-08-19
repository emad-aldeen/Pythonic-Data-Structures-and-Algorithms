from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import (
    BinarySearch
)

def test_BinarySearch():
    actual = BinarySearch([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected


def test_BinarySearch2():
    actual = BinarySearch([1,2,3,4,5,6,7], 9)
    expected = -1
    assert actual == expected

def test_BinarySearch3():
    assert BinarySearch([18,345,35,57,1,38,4], 33) == -1

def test_BinarySearch4():
    actual = BinarySearch([],12)
    expected = "the list is empty"
    assert actual == expected