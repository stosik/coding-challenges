# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum number
# of steps required to reach the end coordinate from the start. If there is no possible path,
# then return null. You can move up, left, down, and right. You cannot move through walls.
# You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
# of steps required to reach the end is 7, since we would need to go through (1, 2) because
# there is a wall everywhere else on the second row.

# Lee algorithm (BFS - shortest path)

# Time complexity is O(M x N)
# Space complexity is O(M X N) - visited nodes matrix + queue

from collections import deque 

class Point: 
    def __init__(self,x: int, y: int): 
        self.x = x 
        self.y = y 

class QueueNode: 
    def __init__(self, pt: Point, dist: int): 
        self.pt = pt 
        self.dist = dist

def is_valid(row: int, col: int, max_row: int, max_col: int):
    return (row >= 0) and (row < max_row) and (col >= 0) and (col < max_col)

ROW_NUM = [-1, 0, 0, 1] 
COL_NUM = [0, -1, 1, 0] 

def solution(board, start: Point, end: Point): 
  if board[start.x][start.y] != False or board[end.x][end.y] != False: 
    return -1
  
  max_row = len(board)
  max_col = len(board[0])

  visited = [[False for i in range(max_row)] for j in range(max_col)]
  visited[start.x][start.y] = True
  
  q = deque() 
  s = QueueNode(start, 0)
  q.append(s)
  
  while q:
    curr = q.popleft()
    pt = curr.pt

    if pt.x == end.x and pt.y == end.y: 
      return curr.dist 
    
    for i in range(4):
      row = pt.x + ROW_NUM[i] 
      col = pt.y + COL_NUM[i]
      if (is_valid(row, col, max_row, max_col) and board[row][col] == False and not visited[row][col]): 
        visited[row][col] = True
        adjecent_cell = QueueNode(Point(row, col), curr.dist + 1)
        q.append(adjecent_cell)

print(solution([
  [False, False, False, False],
  [True, True, False, True],
  [False, False, False, False],
  [False, False, False, False]
], Point(3, 0), Point(0, 0))) # 7
