# This problem was asked by Facebook.

# Given an array of numbers representing the stock prices of a company in chronological order,
# write a function that calculates the maximum profit you could have made from buying and selling that stock once.
# You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5,
# since you could buy the stock at 5 dollars and sell it at 10 dollars.

# Kadaine's algorithm

def solution(A):
  global_max_sum = 0
  local_max_sum = 0
  for i in range(1, len(A)):
    delta = A[i] - A[i - 1]
    local_max_sum = max(delta, local_max_sum + delta)
    global_max_sum = max(local_max_sum, global_max_sum)
  return global_max_sum

print(solution([9, 11, 8, 5, 7, 10])) # 5