class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.rigt = right

def path_to_x(root, x):
  if root == None:
    return None

  if root.value == x:
    return [root]

  left_path = path_to_x(root.left, x)
  if left_path != None:
    left_path.append(root)
    return left_path

  right_path = path_to_x(root.right, x)
  if right_path != None:
    right_path.append(root)
    return right_path

  return None

def solution(root, j, k):
  path_to_j = path_to_x(root, j)
  path_to_k = path_to_x(root, k)

  if path_to_j == None or path_to_k == None:
    return None
  
  lca_to_return = None

  while path_to_j.empty() and path_to_k.empty():
    j_pop = path_to_j.pop()
    k_pop = path_to_k.pop()

    if j_pop == k_pop:
      lca_to_return = j_pop
    else:
      break
  
  return lca_to_return


print(solution())