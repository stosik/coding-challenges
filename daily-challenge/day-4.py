# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer
# in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

import sys

def solution(A):
    m = max(A)
    if m < 1: 
        return 1 
    if len(A) == 1: 
        return 2 if A[0] == 1 else 1     
    l = [0] * m
    for i in range(len(A)): 
        if A[i] > 0: 
            if l[A[i] - 1] != 1: 
              l[A[i] - 1] = 1 
    for i in range(len(l)): 
      if l[i] == 0:  
        return i + 1
    return i + 2     

def hashing_solution(A):
  hash_table = {}
  for i in A:
    if i > 0:
      hash_table[i] = i
  for i in range(1, 1000000):
    if i in hash_table:
      continue
    else:
      return i

print(solution([0, 10, 2, -10, -20]))
print(hashing_solution([0, 10, 2, -10, -20]))