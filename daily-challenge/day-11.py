# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class TrieNode:
    def __init__(self):
        self.next_chars=[None for i in range(26)]
        self.is_end=False


class Trie_Data_Structure:
    def __init__(self):
        self.root=TrieNode()
        self.word_dict=[]

    def insert(self,word):
        node=self.root
        for i in range(len(word)):
            if not node.next_chars[ord(word[i])-ord('a')]:
                node.next_chars[ord(word[i])-ord('a')]=TrieNode()
            node=node.next_chars[ord(word[i])-ord('a')]
        node.is_end=True

    def search(self,word):
        node=self.root
        for i in range(len(word)):
            if node.next_chars[ord(word[i])-ord('a')]:
                node=node.next_chars[ord(word[i])-ord('a')]
            else:
                self.word_dict=[]
                return 
        self.word_dict=[]
        self.autocomplete_search(node,word)

    def autocomplete_search(self,node,word):
        if node.is_end:
            self.word_dict.append(word)
        for i in range(26):
            if node.next_chars[i]:
                self.autocomplete_search(node.next_chars[i],word+chr(i+ord('a')))

def solution():
  
print(solution())