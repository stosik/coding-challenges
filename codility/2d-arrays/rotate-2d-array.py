def rotate_sub(i, j, n):
  return j, n - 1 - i

def out_of_place_solution(arr, n):
  rotated = [row[:] for row in arr]
  for i in range(0, n - 1):
    for j in range(0, n - 1):
      rot_i, rot_j = rotate_sub(i, j, n)
      rotated[rot_i][rot_j] = arr[i][j]
  
  return rotated

print(out_of_place_solution([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]], 3)
)