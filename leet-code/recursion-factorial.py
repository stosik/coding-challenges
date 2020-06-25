def solution(factorial):
  if factorial == 2:
    return 2
  
  return factorial * solution(factorial - 1)

print(solution(5))
