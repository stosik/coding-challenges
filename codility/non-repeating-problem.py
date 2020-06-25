# Given a string, find the length of the longest substring without repeating characters. For example,
# the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
# https://massivealgorithms.blogspot.com/2014/06/leetcode-longest-substring-without.html

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