# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def solution(arr):
  first = 0;
  second = 0;
  
  for i in range(len(arr) - 1, -1, -1):
    new_sum = max(arr[i] + second, first)
    second = first
    first = new_sum
  
  return first


print(solution([2, 4, 6, 2, 5])) # 13
print(solution([5, 1, 1, 5])) # 10