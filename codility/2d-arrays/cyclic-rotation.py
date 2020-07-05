def reverse(nums, start, end):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1
    
    return nums

def solution(nums, k):
    k = k % len(nums)
    arr = reverse(nums, 0, len(nums) - 1)
    rev_arr = reverse(arr, 0, k - 1)
    return reverse(rev_arr, k, len(nums) - 1)