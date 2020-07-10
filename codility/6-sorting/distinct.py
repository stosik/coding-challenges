def solution(A):
  if not A:
    return 0
  
  hash_table = {}

  for item in A:
    hash_table[item] = item

  return len(hash_table)


print(solution([2,1,1,2,3,1]))