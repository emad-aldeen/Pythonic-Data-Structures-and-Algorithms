from data_structures_and_algorithms.challenges.leftJoin.left_join import left_join

def test_2_dictionary():
    dic1 = {'a':'1', 'b':'2', 'c':'3', 'd':'4'}
    dic2 = {'a':'5', 'e':'2', 'c':'6', 'f':'4'}
    actual = left_join(dic1, dic2)
    assert actual == [['a', '1', '5'], ['b', '2', None], ['c', '3', '6'], ['d', '4', None], ['e', None, '2'], ['f', None, '4']]

def test_2_dictionary_no_commun_keys():
    dic1 = {'a':'1', 'b':'2', 'c':'3', 'd':'4'}
    dic2 = {'e':'5', 'f':'6', 'g':'7', 'h':'8'}
    actual = left_join(dic1, dic2)
    assert actual == [['a', '1', None], ['b', '2', None], ['c', '3', None], ['d', '4', None], ['e', None, '5'], ['f', None, '6'], ['g', None, '7'], ['h', None, '8']]

def test_2_dictionary_had_same_keys():
    dic1 = {'a':'1', 'b':'2', 'c':'3', 'd':'4'}
    dic2 = {'a':'5', 'b':'6', 'c':'7', 'd':'8'}
    actual = left_join(dic1, dic2)
    assert actual == [['a', '1', '5'], ['b', '2', '6'], ['c', '3', '7'], ['d', '4', '8']]

def test_2_empty_dictionary():
    dic1 = {}
    dic2 = {}
    actual = left_join(dic1, dic2)
    assert actual == []