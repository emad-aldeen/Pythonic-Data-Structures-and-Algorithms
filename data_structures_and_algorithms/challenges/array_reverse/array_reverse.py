# Note: if you think the first solution is not what challenge is!! .. please cheak the last one 'reverseArray5()' it is the whiteboarded one .. :)

def reverse_array(lst):
    lst2 = []
    for i in range(len(lst)-1,-1,-1):
        lst2.append(lst[i])
    return lst2




# this solution if you want to modify the main argument...
def reverse_array2(lst):
    j = len(lst)-1
    for i in range(j):
        jj = j - i
        lst[i],lst[jj] = lst[jj],lst[i]
        if i == j//2:
            break
    return lst




# do you think 'range()' is a methoud? :| ,so let me try without useing it..
def reverse_array3(lst):
    j = len(lst)-1
    i = 0
    while i != j:
        jj = j - i
        lst[i],lst[jj] = lst[jj],lst[i]
        if i == j//2:
            break
        i += 1
    return lst




# what about 'len()'!!  is it meth or not!! :v ,let me try..
def reverse_array4(lst):
    j = 1
    while True:
        try:
            lst[j]
        except IndexError:
            j -= 1
            break
        else:
            j += 1
            continue

    i = 0
    while i != j:
        jj = j - i
        lst[i],lst[jj] = lst[jj],lst[i]
        if i == j//2:
            break
        i += 1
    return lst




# so what if len was methoud & you want result on new list? *note that "append()" also methoud!!
def reverse_array5(lst):
    j = 1
    while True:
        try:
            lst[j]
        except IndexError:
            j -= 1
            break
        else:
            j += 1
            continue

    lst2 = [0]*(j+1)

    i = 0
    while j >= 0:
        lst2[i] = lst[j]
        j -= 1
        i += 1
    return lst2



# print(reverse_array5([1, 2, 3, 4, 5, 6,7]))