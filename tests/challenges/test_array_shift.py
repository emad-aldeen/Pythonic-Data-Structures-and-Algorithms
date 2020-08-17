from data_structures_and_algorithms.challenges.array_shift.array_shift import *


def test_insertShiftArray():
    actual = insertShiftArray([2,4,6,8], 5)
    expected = [2,4,5,6,8]
    assert actual == expected


def test_insertShiftArray2():
    actual = insertShiftArray([4,8,15,23,42], 16)
    expected = [4,8,15,16,23,42]
    assert actual == expected


def test_insertShiftArray3():
    actual = insertShiftArray([1,2,3,5,6,7,8], 4)
    expected = [1,2,3,4,5,6,7,8]
    assert actual == expected


def test_insertShiftArray4(): 
    assert insertShiftArray([23,150,999,5646,1257,1500], 1000) == [23,150,999,1000,5646,1257,1500]

# this 'Expected failure' test..
def test_insertShiftArray5():
    actual = insertShiftArray([0,7,1,3,9,5,15,3,3,26,67],5)
    expected = [0, 5, 1, 3, 5, 9, 5, 3, 3, 5, 26, 67]
    assert actual == expected