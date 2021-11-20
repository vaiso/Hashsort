

def hashSort(arr):
  if (len(arr) <= 1):
    return arr

  minVal = min(arr)
  maxVal = max(arr)
  hash_len = maxVal - minVal + 1

  hash = [None] * hash_len
  
  for num in arr:
    insertIntoHash(hash, num, minVal)

  sortedArr = hashToArr(hash)

  return sortedArr


def insertIntoHash(hash, num, minVal):
  index = num - minVal
  if not hash[index]:
    hash[index] = (num, 1)
  else:
    count = hash[index][1]
    hash[index] = (num, count + 1)


def hashToArr(hash):
  sortedArr = []

  for elem in hash:
    if elem:
      (val, count) = elem
      for i in range(count):
        sortedArr.append(val)
  
  return sortedArr