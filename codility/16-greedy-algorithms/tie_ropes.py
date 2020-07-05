# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/

def solution(K, A):
    count = 0
    rope_length = 0
    for rope in A:
        rope_length += rope
        if rope_length >= K:
            count += 1
            rope_length = 0
    return count


print(solution(4, [1, 2, 3, 4, 1, 1, 3]))