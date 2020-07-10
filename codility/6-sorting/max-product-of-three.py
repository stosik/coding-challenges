def solution(A):
  res = sorted(A) # O(nlogn)

  if len(res) == 3:
    return res[0] * res[1] * res[2]
  else:
    return max(res[0] * res[1] * res[2], res[len(res) - 1] * res[len(res) - 2] * res[len(res) - 3])


print(solution([-3, 1, 2, -2, 5, 6]))