# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

def solution(s):
  if len(s) <= 1:
    return s
  start = end = 0
  for i in range(len(s)):
    max_len_1 = expand_from_middle(s, i, i) # abba case
    max_len_2 = expand_from_middle(s, i, i + 1) # racecar case
    max_len = max(max_len_1, max_len_2)

    if max_len > end - start:
      start = i - (max_len - 1) // 2
      end = i + max_len // 2

  return s[start: end + 1]
        
def expand_from_middle(s, left, right):
  while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1

  return right - left - 1

print(solution("abba"))