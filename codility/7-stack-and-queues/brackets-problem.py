# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a
# closing bracket (i.e., ), ], or }) of the exact same type.
# There are three types of matched pairs of brackets: [], {}, and ().
# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched.
# For example, {[(])} is not balanced because the contents in between { and } are not balanced.
# The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single,
# unbalanced closing square bracket, ].
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:

def solution(S):
  valid = True
  stack = []
  for c in S:
    if c == "[" or c == "{" or c == "(":
      stack.append(c)
    elif c == ")":
      valid = False if not stack or stack.pop() != "(" else valid
    elif c == "]":
      valid = False if not stack or stack.pop() != "[" else valid
    elif c == "}":
      valid = False if not stack or stack.pop() != "}" else valid
  return 1 if valid and not stack else 0


print(solution("[]{}(())"))
print(solution("[]{}(()}"))
