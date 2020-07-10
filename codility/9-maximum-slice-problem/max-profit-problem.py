# The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
# For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3.
# Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/

# Kadaine's algorithm

def solution(A):
  global_max_sum = 0
  local_max_sum = 0
  for i in range(1, len(A)):
    delta = A[i] - A[i - 1]
    local_max_sum = max(delta, local_max_sum + delta)
    global_max_sum = max(local_max_sum, global_max_sum)
  return global_max_sum


def max_slice_solution(A):
    l_max_slice_sum = [0] * len(A)
    r_max_slice_sum = [0] * len(A)

    for i in range(1, len(A)-2):
        l_max_slice_sum[i] = max(l_max_slice_sum[i-1] + A[i], 0)

    for i in range(len(A)-2, 1, -1):
        r_max_slice_sum[i] = max(r_max_slice_sum[i+1] + A[i], 0)

    max_slice_sum = l_max_slice_sum[0] + r_max_slice_sum[2]
    for i in range(1, len(A)-1):
        max_slice_sum = max(max_slice_sum, l_max_slice_sum[i-1]+r_max_slice_sum[i+1])
        
    return max_slice_sum


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))

print(max_slice_solution([3, 2, 6, -1, 4, 5, -1, 2]))