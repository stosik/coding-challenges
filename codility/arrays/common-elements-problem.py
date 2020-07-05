# Extracting common elements between two integer arrays in nLogn time

def solution(A, B):
  p1 = 0
  p2 = 0
  result = []
  while p1 < len(A) and p2 < len(B):
    if A[p1] == B[p2]:
      result.append(A[p1])
      p1 += 1
      p2 += 1
    elif A[p1] > B[p2]:
      p2 += 1
    else:
      p1 += 1
  return result

print(solution([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))


# Time complexity O(n)