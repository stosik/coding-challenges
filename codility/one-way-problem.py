def is_one_way_diff_lenghts(s1, s2):
  i = 0
  count_diff = 0
  while i < len(s2):
    if s1[i + count_diff] == s2[i]:
      i += 1
    else:
      count_diff += 1
      if count_diff > 1:
        return False
  return True

def is_one_away_same_length(s1, s2):
  count_diff = 0
  for i in range(len(s1) - 1):
    if s1[i] != s2[i]:
      count_diff += 1
      if count_diff > 1:
        return False

def solution(s1, s2):
  if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
    return False
  elif len(s1) == len(s2):
    return is_one_away_same_length(s1, s2)
  elif len(s1) > len(s2):
      return is_one_way_diff_lenghts(s1, s2)
  else:
      return is_one_way_diff_lenghts(s2, s1)


print(solution('aec', 'abc')) # CHANGE
print(solution('ae', 'aec')) # REMOVE
print(solution('abcd', 'abc')) # ADD