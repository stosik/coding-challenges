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
  
  return solution(n - 1) + solution(n - 2)


def nums_way_button_up(n):
  if n == 0 or n == 1:
    return 1
  
  nums = [0] * (n + 1)
  nums[0] = 1
  nums[1] = 1
  for i in range(2, n + 1):
    nums[i] = nums[i-1] + nums[i-2]
  return nums[n]


print(solution(4))
print(nums_way_button_up(4))