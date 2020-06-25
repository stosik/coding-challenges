# https://leetcode.com/problems/number-of-islands/

def bfs_adjecents(grid, i, j):
  if i < 0  or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
    return
  
  grid[i][j] = 0

  bfs_adjecents(grid, i + 1, j) # up
  bfs_adjecents(grid, i - 1, j) # down
  bfs_adjecents(grid, i, j - 1) # left
  bfs_adjecents(grid, i, j + 1) # right



def solution(grid):
  islands_count = 0

  for rowIndex in range(0, len(grid)):
    for colIndex in range(0, len(grid[rowIndex])):
      if grid[rowIndex][colIndex] == "1":
        islands_count += 1
        bfs_adjecents(grid, rowIndex, colIndex)

  return islands_count

print(solution([
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
]))


print(solution([
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]))