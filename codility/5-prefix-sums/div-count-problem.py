# Compute number of integers divisible by k in range [a..b].
# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

import math

def solution(a, b, k):
  start = math.ceil(a/b)
  end = math.floor(b/k)

  result = end - start + 1
  return result
  
print(solution(6, 11, 2))