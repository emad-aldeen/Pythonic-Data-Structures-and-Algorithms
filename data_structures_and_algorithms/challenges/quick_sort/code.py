def quicksort(arr, left, right):
    if left < right:
        position = partion(arr, left, right)

        quicksort(arr, left, position - 1)

        quicksort(arr, position + 1, right)


def partion(arr, left, right):
    pivot = arr[right]

    low = left - 1

    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)

    return low + 1


def swap(arr, i, low):
    temp = None
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

 

# if __name__ == '__main__':
#     lst = [8,4,23,42,16,15]
#     quicksort(lst, 0, 5)
#     print(lst)