# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21

def solution(x):
  s = str(abs(x))
  reversed = int(s[::-1])
  if reversed > 2147483647:
    return 0

  return reversed if x > 0 else (reversed * -1)

print(solution(123))
  