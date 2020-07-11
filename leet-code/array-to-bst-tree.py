class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromArray(self, nums, left, right):
    if left > right:
        return None
    
    midpoint = int(left + (right - left) / 2)
    
    node = TreeNode(nums[midpoint])
    node.left = self.constructFromArray(nums, left, midpoint - 1)
    node.right = self.constructFromArray(nums, midpoint + 1, right)
    
    return node

def solution(self, nums):
  if not nums:
      return None
  return self.constructFromArray(nums, 0, len(nums) - 1)
