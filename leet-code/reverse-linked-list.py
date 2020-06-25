class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def solution(ls):
  prev = None
  current = head
        
  while current != None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
            
  return prev

first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = None

print(solution(first_node))