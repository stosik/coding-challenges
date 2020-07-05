# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/

def solution(A, B):
    last_end_segment = -1
    chosen_count = 0
    for i in range(len(A)):
        if A[i] > last_end_segment:
            chosen_count += 1
            last_end_segment = B[i]
    return chosen_count


print(solution([1, 3, 7, 9, 1], [5, 6, 8, 9, 10]))

print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

print(solution([], []))