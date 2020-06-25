# Only for sorted array
# Ologn = k
# 1 * 2^k = n

def recursive_binary_search(arr, x, left, right):
  if left > right:
    return False

  pivot = (left + right) / 2
  if arr[pivot] == x:
    return True
  elif x < arr[pivot]:
    recursive_binary_search(arr, x, left, pivot - 1)
  else:
    recursive_binary_search(arr, x, pivot + 1, right)


def iterative_binary_search(arr, x,):
  left = 0
  right = len(arr) - 1
  
  while (left <= right):
    pivot = (left + right) / 2
    if arr[pivot] == x:
      return True
    elif arr[pivot] > x:
      right = pivot - 1
    else:
      left = pivot + 1