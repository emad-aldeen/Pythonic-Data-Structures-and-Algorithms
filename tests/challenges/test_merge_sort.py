from data_structures_and_algorithms.challenges.merge_sort.code import merge_sort

def test_simple_lst():
    lst = [8,4,23,42,16,15]
    merge_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order():
    lst = [42, 23, 16, 15, 8, 4]
    merge_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order2():
    lst = [20,18,12,8,5,-2]
    merge_sort(lst)
    assert lst == [-2, 5, 8, 12, 18, 20]

def test_list_zeros_and_negative():
    lst = [-23, -0.5, -4, 0, -1]
    merge_sort(lst)
    assert lst == [-23, -4, -1, -0.5, 0]

def test_few_uniques():
    lst = [5,12,7,5,5,7]
    merge_sort(lst)
    assert lst == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    lst = [2,3,5,7,13,11]
    merge_sort(lst)
    assert lst == [2, 3, 5, 7, 11, 13]

def test_sorted():
    lst = [2,3,5,7,11,13]
    merge_sort(lst)
    assert lst == [2,3,5,7,11,13]



