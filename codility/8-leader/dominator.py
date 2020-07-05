# Find an index of an array such that its value occurs at more than half of indices in the array.
# https://app.codility.com/programmers/lessons/8-leader/dominator/

def solution(A):
  consecutive_size = 0
  candidate = 0
  for item in A:
    if consecutive_size == 0:
      candidate = item
      consecutive_size += 1
    elif candidate == item:
      consecutive_size += 1
    else:
      consecutive_size -= 1
  
  ocurrences = A.count(candidate)
  if ocurrences > (len(A)/2):
    return A.index(candidate)
  else:
    return -1


print(solution([2,4,3,3,3,2,3]))
