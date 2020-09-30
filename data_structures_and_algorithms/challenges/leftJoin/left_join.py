def left_join(HM1, HM2):
    '''
    function that LEFT JOINs two hashmaps into a single data structure:
        inp1 ---> hashmap(dictionary)
        inp2 ---> hashmap(dictionary)
        out >>> list of lists contain each key with values..
    '''
    res = []
    for i in HM1:
        x = None
        if i in HM2:
            x = HM2[i]
            del HM2[i]

        res = res + [[i,HM1[i],x]]

    for j in HM2:
        res = res + [[j,None,HM2[j]]]

    return res


# if __name__ == '__main__':
#     dic = {'a':'1', 'b':'2', 'c':'3', 'd':'4'}
#     dic2 = {'a':'5', 'e':'2', 'c':'6', 'f':'4'}
#     print(left_join(dic, dic2))
    