class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.rigt = right

def is_bst(node, lower_limit=None, upper_limit=None):
  if lower_limit != None and node.value < lower_limit:
    return False
  if upper_limit != None and node.value > upper_limit:
    return False
  return True

def solution(node, lower_limit=None, upper_limit=None):
  is_left_bst = True
  is_right_bst = True

  if node.left != None:
    is_left_bst = is_bst(node.left, lower_limit, node.value)
  if is_left_bst and node.right != None:
    is_right_bst = is_bst(node.right, node.value, upper_limit)

  return is_left_bst and is_right_bst

print(solution())