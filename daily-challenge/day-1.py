# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def solution(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            return True
    return False

def hash_solution(arr, k):
  exist = False
  hash_table = {}
  for item in arr:
    if k - item in hash_table:
      exist = True
      return exist
    hash_table[item] = item
  return exist
  
print(solution([10, 15, 3, 7], 17))
print(hash_solution([10, 15, 3, 7], 17))

def solutin_leet_code(nums, target):
  hash_table = {}
  for index, item in enumerate(nums):
    if target - item not in hash_table:
      hash_table[item] = index
    else:
      return [hash_table[target - item], index]

print(solutin_leet_code([2,7,11,15], 9))
