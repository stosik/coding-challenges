# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# Also returns number of unival subtrees, and whether it is itself a unival subtree.
def helper(root):
    if root is None:
        return 0, True
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False

def solution(root):
    count, _ = helper(root)
    return count

root = Node(0)
first_node = Node(1)
second_node = Node(0) 
third_node = Node(1) 
fourth_node = Node(0) 
fifth_node = Node(1) 
sixth_node = Node(1)

root.left = first_node
root.right = second_node
second_node.left = third_node
second_node.right = fourth_node
third_node.left = fifth_node
third_node.right = sixth_node

print(solution(root)) # 5