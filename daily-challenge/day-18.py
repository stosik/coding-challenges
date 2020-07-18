# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.


# https://algorithms.tutorialhorizon.com/sliding-window-algorithm-track-the-maximum-of-each-subarray-of-size-k/

from collections import deque

def solution(arr, k): 
    qi = deque()

    for i in range(k):
      while qi and arr[i] >= arr[qi[-1]] : 
         qi.pop()
      qi.append(i)

    for i in range(k, len(arr)):
      print(arr[qi[0]])
      while qi and qi[0] <= i-k:
        qi.popleft()

      while qi and arr[i] >= arr[qi[-1]]:
        el = qi.pop()

      qi.append(i)
    print(arr[qi[0]])


solution([10, 5, 2, 7, 8, 7], 3) # [10, 7, 8, 8]