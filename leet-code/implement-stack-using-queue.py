class MyStack:
  
    def __init__(self):

    def push(self, x):
        
    def pop(self):

    def top(self):

    def empty(self):

class Queue():

  def __init__(self, storage={}, last=0, first=0):
    self.storage = storage
    self.last = last
    self.first = first

  def peek(self):
    return self.storage[self.first]

  def isEmpty(self):
    return self.last == self.first

  def size(self):
    return self.last - self.first
  
  def dequeue(self):
    first = self.storage[self.first]
    self.storage.
    self.first += 1
    return first

  def enqueue(self, val):
    self.storage[self.last] = val
    self.last += 1
