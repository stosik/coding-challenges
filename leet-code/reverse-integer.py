def solution(x):
  s = str(abs(x))
  reversed = int(s[::-1])
  if reversed > 2147483647:
    return 0

  return reversed if x > 0 else (reversed * -1)

print(solution(123))
  