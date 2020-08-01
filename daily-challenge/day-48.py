# This problem was asked by Google.

# ** MEDIUM **

# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
# For example, given the following preorder traversal:
# [a, b, d, e, c, f, g]
# And the following inorder traversal:
# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g


# Additionaly can add Hashmap for inorder lookup
# Time complexity: O(n)

class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def build_tree(pre_start, in_start, in_end, pre_order, in_order):
  if pre_start > len(pre_order) - 1 or in_start > in_end:
    return None

  root = Node(pre_order[pre_start])

  in_index = 0

  for i in range(in_start, in_end + 1):
    if root.val == in_order[i]:
      in_index = i

  root.left = helper(pre_start + 1, in_start, in_index - 1, pre_order, in_order)
  root.right = helper(pre_start + in_index - in_start + 1, in_index + 1, in_end, pre_order, in_order)

  return root

pre_order = ['a', 'b', 'd', 'e', 'c', 'f', 'g'] 
in_order = ['d', 'b', 'e', 'a', 'f', 'c', 'g'] 

root = build_tree(0, 0, len(in_order) - 1, in_order, pre_order) 