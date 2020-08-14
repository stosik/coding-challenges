# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return memoized_func

@memoize
def helper(data, k):
  if k == 0:
    return 1
  
  s = len(data) - k

  if data[s] == '0':
    return 0
  
  result = helper(data, k -1)

  if k >= 2 and int(data[s:s+2]) <= 26:
    result += helper(data, k - 2)
  
  return result

def solution(data):
  return helper(data, len(data))

print(solution('111')) # 3