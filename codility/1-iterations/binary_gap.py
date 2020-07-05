# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def to_binary_representation(A):
    return bin(A)[2:]

def solution(A):
  binary = str(to_binary_representation(A))

  local_max = 0
  global_max = 0
  for number in binary:
      if number == '1':
          if local_max > global_max:
              global_max = local_max
          local_max = 0
      elif number == '0':
          local_max += 1
    
  return global_max
    

print(solution(9))
print(solution(1041))