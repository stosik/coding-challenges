# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
  sum_left = A[0]
  sum_right = sum(A) - sum_left
  current_diff = abs(sum_left - sum_right)
  for i in range(1, len(A) - 1):
    sum_left += A[i]
    sum_right -= A[i]
    diff = abs(sum_left - sum_right)
    if(current_diff > diff):
      current_diff = diff
  return current_diff


print(solution([3,1,2,4,3]))