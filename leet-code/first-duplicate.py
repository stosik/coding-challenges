def solution(A):
  for i in range(0, len(A)):
    if A[abs(A[i]) - 1] < 0:
      return abs(A[i])
    else:
      A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]

  return -1

print(solution([2,1,3,5,3,2])) # print 3
print(solution([2,2])) # print 2

# Time complexity O(n)
# Space complexity O(1)