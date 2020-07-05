# Given an array of integers where each element points to the index 
# of the next element how would you detect if there is a cycle in this array

def solution(arr, k):
  array_size = len(arr)
  new_arr = [None] * array_size
  
  for i in range(array_size):
    new_arr[(i + k) % array_size] = arr[i]

  return new_arr

print(solution([3,4,6,1,7,8], 2))