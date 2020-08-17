def insertShiftArray(lst,n):

    resList = [[0] for i in range(len(lst)+1)]

    for i in range(len(lst)):
        if lst[i] < n:
           resList[i] = lst[i]
        elif lst[i] > n and lst[i-1] < n:
            resList[i] = n
        else:
            resList[i] = lst[i-1]
            
    resList[len(lst)] = lst[len(lst)-1]      

    return resList



# it dosent mater if the list is sorted it will inesert the number always in the middle..
def insertShiftArray2(lst,n):

    resList = [[0] for i in range(len(lst)+1)]

    if len(lst) % 2 == 0:
        j = len(lst)//2
    else:
        if lst[(len(lst)//2)] < n:
            j = (len(lst)//2)+1
        else:
            j = (len(lst)//2)

    for i in range(len(resList)):
        if i == j:
            resList[i] = n
        elif i < j:
            resList[i] = lst[i]
        else:
            resList[i] = lst[i-1]

    return resList



def insertShiftArray3(lst,n):

    resList = []

    for i in range(len(lst)):
        if lst[i] < n:
           resList.append(lst[i])
        elif lst[i] > n and lst[i-1] < n:
            resList.append(n)
        else:
            resList.append(lst[i-1])
    resList.append(lst[len(lst)-1])        
    return resList