# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def solution(text):
  chars_count = {}
  for item in text:
    if item in chars_count:
      chars_count[item] += 1
    else:
      chars_count[item] = 1
  
  for char in text:
    if chars_count[char] == 1:
      return char
  return None

print(solution('aabcdd'))