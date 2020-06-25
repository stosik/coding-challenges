import math

def rotate_sub(i, j, n):
    return j, n - 1 - i

def solution_out_place(a):
    len_array = len(a)
    new_array = [[0] * len_array for i in range(len_array)]

    for i in range(0, len_array):
        for j in range(0, len_array):
            new_i, new_j = rotate_sub(i, j,len_array)
            new_array[new_i][new_j] = a[i][j]
    return new_array

def solution_in_place(matrix):
  N = len(matrix)

  # transposing matrix
  for i in range(0, N):
    for j in range(i, N):
      temp = matrix[i][j]
      matrix[i][j] = matrix[j][i]
      matrix[j][i] = temp

  half_array_len = math.floor(N/2)

  # reverse horizontally
  for i in range(0, N):
    for j in range(0, half_array_len):
      temp = matrix[i][j]
      matrix[i][j] = matrix[i][N - 1 - j]
      matrix[i][N - 1 - j] = temp
  
  return matrix
      


print(solution_out_place([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

print(solution_in_place([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

print(solution_out_place([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]))

print(solution_in_place([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]))