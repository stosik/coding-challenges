# This problem was asked by Facebook.
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

def solution(A):
  if not A:
    return True
  
  valid = True
  stack = []

  for char in A:
    if char == "(" or char == "[" or char == "{":
      stack.append(char)
    elif char == ")":
      valid = False if not stack or stack.pop() != "(" else valid
    elif char == "]":
      valid = False if not stack or stack.pop() != "[" else valid
    elif char == "}":
      valid = False if not stack or stack.pop() != "{" else valid

  return True if valid and not stack else False

print(solution("([])[]({})")) # True
print(solution("([)]")) # False
print(solution("((()")) # False
