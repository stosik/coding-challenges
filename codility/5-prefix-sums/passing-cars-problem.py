# Count the number of passing cars on the road.
# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

def solution(A):
  suffix_sum = [0] * (len(A) + 1)
  for i in range(len(A) -1, -1, -1):
    suffix_sum[i] = A[i] + suffix_sum[i + 1]
  count = 0
  for i in range(len(A)):
    if A[i] == 0:
      count += suffix_sum[i]
    if count > 10000000:
      return -1
  return count

print(solution([0, 1, 0, 1, 1]))