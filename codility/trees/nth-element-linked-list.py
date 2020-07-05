# Given a linked list, remove the n-th node from the end of list and return its head.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def solution(head, n):
  left_pointer = head
  right_pointer = head

  for i in range(0, n - 1):
    if right_pointer == None:
      return None
    right_pointer = right_pointer.next
  
  while right_pointer != None:
    right_pointer = right_pointer.next
    left_pointer = left_pointer.next
  
  return left_pointer


node_1 = Node(5)
node_2 = Node(4)
node_3 = Node(3)
node_4 = Node(2)
node_5 = Node(1)
node_6 = None

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6

head = [node_1, node_2, node_3, node_4, node_5, node_6]

print(solution(head, 3))
print(solution(head, 6))