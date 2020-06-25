def solution(A, B):
  if len(A) != len(B):
    return False

  key = A[0]
  key_i = -1

  for i in range(0, len(B) -1):
    if B[i] == key:
      key_i = i
      break
  
  if key_i == -1:
   return False
  
  for i in range(0, len(A) - 1):
    j = (key_i + i) % len(A)
    if A[i] != B[j]:
      return False
  return True


print(solution([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]))