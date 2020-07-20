# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


# 1. Find difference between lenghts of lists
# 2. Move pointer of longer by difference of lenghts
# 3. Descendant moving two pointers on lists and comparing their values

class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next


def list_length(node):
  current = node
  count = 0

  while current != None:
    count += 1
    current = current.next

  return count


def get_intersection_node(d, A, B):
  i = 0
  current_one = A
  current_two = B

  for i in range(d):
    if current_one == None:
      return -1
    current_one = current_one.next

  while current_one != None and current_two != None:
    if current_one.value == current_two.value:
      return current_one.value
    current_one = current_one.next
    current_two = current_two.next

  return -1

def get_node(A, B):
  c1 = list_length(A); 
  c2 = list_length(B); 
  d = 0
  
  if c1 > c2: 
    d = c1 - c2; 
    return get_intersection_node(d, A, B)
  else: 
    d = c2 - c1; 
    return get_intersection_node(d, B, A)


node_1_a = Node(3)
node_2_a = Node(7)
node_3_a = Node(8)
node_4_a = Node(10)
node_1_a.next = node_2_a
node_2_a.next = node_3_a
node_3_a.next = node_4_a

node_1_b = Node(99)
node_2_b = Node(1)
node_1_b.next = node_2_b
node_2_b.next = node_3_a

print(get_node(node_1_a, node_1_b)) # 8