def solution(s):
  hash_table = {}
        
  for i in s:
    if i not in hash_table:
      print(i)
      hash_table[i] += 1
    else:
      hash_table[i] = 1
        
    for i in range(0, len(s)):
      if hash_table[s[i]] == 1:
        return i        
  return 0

print(solution("leetcode"))