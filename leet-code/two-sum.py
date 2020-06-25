# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def solution(self, nums, target):
  hash_table = {}
  for index, item in enumerate(nums):
    if target - item not in hash_table:
      hash_table[item] = index
    else:
      return [hash_table[target - item], index]

print(solution(2, 7, 11, 15)) #9
        