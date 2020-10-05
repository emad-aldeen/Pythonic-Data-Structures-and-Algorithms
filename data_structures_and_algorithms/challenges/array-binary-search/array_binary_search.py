def binary_search(lst, value):
      left_index = 0
      right_index = (len(lst)-1)

      while left_index <= right_index:
          middle = left_index + (right_index) + 1 // 2
      
          if value == lst[middle]:
              return middle
          elif value < lst[middle]:
              right_index = middle - 1
          else:
              left_index = middle + 1
      
      return -1


# if __name__=="__main__":
#     print(binary_search([4,8,15,16,23,42], 44))
    # print(binarySearch([1,2,3,4,5,6,7], 8))