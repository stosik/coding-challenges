# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible reconstruction,
# return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

# add memoization
# https://www.geeksforgeeks.org/word-break-problem-using-backtracking/ check here

def get_sentence_split(s, words):
  if not s or not words:
    return []

  sentence_words = list()
  for i in range(len(s)):
    if s[0:i + 1] in words:
      sentence_words.append(s[0:i + 1])
      words.remove(s[0:i + 1])
      sentence_words += get_sentence_split(s[i + 1:], words)
      break

  return sentence_words

print(get_sentence_split("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
print(get_sentence_split("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))