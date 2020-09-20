# import sys
# print(sys.path)
from data_structures_and_algorithms.challenges.insertion_sort.code import insertion_sort

def test_simple_lst():
    lst = [8,4,23,42,16,15]
    insertion_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]
def test_list_reverse_order():
    lst = [42, 23, 16, 15, 8, 4]
    insertion_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]
def test_list_reverse_order2():
    lst = [20,18,12,8,5,-2]
    insertion_sort(lst)
    assert lst == [-2, 5, 8, 12, 18, 20]
def test_list_zeros_and_negative():
    lst = [-23, -0.5, -4, 0, -1]
    insertion_sort(lst)
    assert lst == [-23, -4, -1, -0.5, 0]
def test_few_uniques():
    lst = [5,12,7,5,5,7]
    insertion_sort(lst)
    assert lst == [5, 5, 5, 7, 7, 12]
def test_nearly_sorted():
    lst = [2,3,5,7,13,11]
    insertion_sort(lst)
    assert lst == [2, 3, 5, 7, 11, 13]
def test_sorted():
    lst = [2,3,5,7,11,13]
    insertion_sort(lst)
    assert lst == [2,3,5,7,11,13]
def test_same_vals():
    lst = [1, 1, 1, 1, 1]
    insertion_sort(lst)
    assert lst == [1, 1, 1, 1, 1]