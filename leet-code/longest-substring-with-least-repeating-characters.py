# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character
# in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3

# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input:
# s = "ababbc", k = 2

# Output:
# 5

# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

MAX_CHARS = 26

def solution(str, k):     
  
    n = len(str)                   
    freq = [0] * MAX_CHARS                  
    for i in range(n):   
        freq[ord(str[i]) - ord('a')] += 1              
  
    for i in range(n ): 
        if (freq[ord(str[i]) - ord('a')] >= k):                
          return str[i]
        else:
          return ""
   
print(solution("geeksforgeeks", 2))