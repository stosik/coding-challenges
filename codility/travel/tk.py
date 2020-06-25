def generate_sum_array(A):
  sum_array = [0] * len(A)
  sum_array[0] = A[0]

  for i in range(1, len(A)):
    sum_array[i] = sum_array[i - 1] + A[i]

  return sum_array

def solution(A): 
  left_pointer = 0
  right_pointer = len(A) - 1
  left_part_sum, right_part_sum, middle_part_sum = 0, 0, 0

  sum_array = generate_sum_array(A)

  while left_pointer < right_pointer:
      left_part_sum = sum_array[left_pointer] - A[left_pointer]
      middle_part_sum = sum_array[right_pointer] - sum_array[left_pointer] - A[right_pointer]
      right_part_sum = sum_array[len(A) - 1] - sum_array[right_pointer]

      if (left_part_sum == middle_part_sum) and (middle_part_sum == right_part_sum):
          return True

      if (left_part_sum < right_part_sum):
          left_pointer += 1
      elif (left_part_sum > right_part_sum):
          right_pointer -= 1
      else :
          left_pointer += 1
          right_pointer -= 1

  return False

print(solution([1, 1, 1, 1, 1, 1])) # False
print(solution([1, 3, 4, 2, 2, 2, 1, 1, 2])) # True
print(solution([1,2] * 10000)) # True