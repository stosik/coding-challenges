# This problem was asked by Google.

# ** MEDIUM **

# Given a singly linked list and an integer k, remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.
# Do this in constant space and in one pass.

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def solution(node, k):
  main_pointer = node
  ref_pointer = node

  count = 0

  if node is not None:
    while count < k:
      if ref_pointer is None:
        return
      
      ref_pointer = ref_pointer.next
      count += 1
  
  while ref_pointer is not None:
    main_pointer = main_pointer.next
    ref_pointer = ref_pointer.next
  
  main_pointer.next = main_pointer.next.next # Remove nth from end :)

first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
last_node =  Node(5)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = last_node

solution(first_node, 2)