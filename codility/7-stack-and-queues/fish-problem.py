# N voracious fish are moving along a river. Calculate how many fish are alive.
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

def solution(A, B):
  survivors = 0
  stack = [1]

  for i in range(len(A)):
    weight = A[i]
    if B[i] == 1:
      stack.append(weight)
    else:
      weightdown = stack.pop() if stack else -1
      while weightdown != -1 and weightdown < weight:
        weightdown = stack.pop() if stack else -1
      if weightdown == -1:
        survivors += 1
      else:
        stack.append(weightdown)
  return survivors + len(stack)

print(solution([0,1,0,0], [2,1,5,4]))