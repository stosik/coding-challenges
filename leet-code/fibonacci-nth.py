def solution(n):
  if n < 2:
    return n

  return solution(n - 1) + solution(n - 2)

print(solution(3))