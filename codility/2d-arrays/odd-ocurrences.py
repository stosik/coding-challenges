# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# X ^ X = 0
# X ^ 0 = X

def solution(A):
  odd = 0
  for i in A:
    odd ^= i
  return odd