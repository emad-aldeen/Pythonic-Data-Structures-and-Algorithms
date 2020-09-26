from data_structures_and_algorithms.challenges.quick_sort.code import quicksort


def test_simple_lst():
    lst = [8,4,23,42,16,15]
    quicksort(lst, 0, 5)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order():
    lst = [42,23,16,15,8,4]
    quicksort(lst, 0, 5)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_few_uniques():
    lst = [5,12,7,5,5,7]
    quicksort(lst, 0, 5)
    assert lst == [5, 5, 5, 7, 7, 12]

def test_sorted():
    lst = [2,3,5,7,11,13]
    quicksort(lst, 0, 5)
    assert lst == [2,3,5,7,11,13]
