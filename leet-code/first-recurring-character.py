def solution(s):
  hash_table = {}

  for item in s:
    if item in hash_table:
      hash_table[item] += 1
    else:
      hash_table[item] = 1

  for item in s:
    if hash_table[item] > 1:
      return item
  
  return -1

print(solution("leetcode"))