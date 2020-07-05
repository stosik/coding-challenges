# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    max_number = len(A) + 1
    sum = 0
    for number in A:
        sum += number
    return (max_number * (max_number + 1) // 2) - sum


print(solution([2, 3, 1, 5]))