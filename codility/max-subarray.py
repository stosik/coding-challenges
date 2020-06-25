# Find a maximum sum of a compact subsequence of array elements.
# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/

def solution(A):
    local_max_sum = 0
    global_max_sum = 0
    
    for i in range(1, len(A)):
        delta = A[i] + A[i-1]
        local_max_sum = max(delta, local_max_sum + delta)
        global_max_sum = max(local_max_sum, global_max_sum)
    return global_max_sum 

print(solution([3, 2, -6, 4, 0]))