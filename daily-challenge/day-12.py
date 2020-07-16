# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example,
# if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def solution(n):
  if n == 0 or n == 1:
    return 1
  else:
    return solution(n - 1) + solution(n - 2)


def solution_buttom_up(n):
  if n == 0 or n == 1:
    return 1
  else:
    last = 1
    two_last = 1
    total = 0
    for i in range(2, n + 1):
      total = last + two_last
      two_last = last
      last = total
      
  return total

print(solution_buttom_up(4))