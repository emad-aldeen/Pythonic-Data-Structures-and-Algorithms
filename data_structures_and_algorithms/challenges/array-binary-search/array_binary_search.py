def BinarySearch(list,num):
  testLength = 0

  while True:
      try:
          list[testLength]
      except IndexError:
          break
      else:
          testLength += 1
          continue
  lenOflist = testLength
  indexOflist=lenOflist-1
  mid = lenOflist // 2
  if lenOflist == 0:
    return "the listt is empty"
  else:

    while list[mid] != num:
      if num > list[indexOflist]:
        return -1
      else:
        if num == list[mid]:
          return mid
        else:
          if num < list[mid]:
            mid = mid // 2
          elif num > list[mid]:
            mid =indexOflist-mid
  return mid


if __name__=="__main__":
    print(BinarySearch([4,8,15,16,23,42], 15))
    print(BinarySearch([1,2,3,4,5,6,7], 8))