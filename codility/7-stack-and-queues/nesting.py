# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/

def solution(S):
    if len(S) == 0:
        return 0
    
    valid = 1
    stack = []
    
    for c in S:
        if c == '(':
            stack.append(c)
        elif c == ")":
            valid = 0 if not stack or stack.pop() != "(" else valid
    return valid

print(solution("(())"))
print(solution("(()))"))