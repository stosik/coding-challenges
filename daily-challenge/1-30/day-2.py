# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers
# in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

# {1,                   a[0],         a[0] * a[1], a[0] * a[1] * a[2] }
# {a[1] * a[2] * a[3] , a[2] * a[3], a[3],          1}

def solution(nums):
  products_below = [0] * len(nums)
  products_above = [0] * len(nums)
  products_result = [0] * len(nums)

  p = 1
  for i in range(0, len(nums)):
    products_below[i] = p
    p *= nums[i]

  p = 1
  for i in range(len(nums) - 1, -1, -1):
    products_above[i] = p
    p *= nums[i]

  for i in range(0, len(nums)):
    products_result[i] = products_above[i] * products_below[i]
  
  return products_result

print(solution([1, 2, 3, 4, 5])) # [120, 60, 40, 30, 24]
print(solution([3, 2, 1])) # [2, 3, 6]

