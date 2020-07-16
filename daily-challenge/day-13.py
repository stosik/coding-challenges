# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


# sliding window

def solution(s, k):
  if s == None or len(s) == 0:
    return 0
  
  window_start = 0
  max_lenght = 0
  char_frequency = {}

  for window_end in range(len(s)):
    right_char = s[window_end]

    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1
    
    while len(char_frequency) > k:
      left_char = s[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1
    
    max_lenght = max(max_lenght, window_end - window_start + 1)

  return max_lenght

print(solution("eceba", 2))