class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # split sentence into words
        words = sentence.split()
        
        # iterate to check if searchWord is a prefex
        for i, w in enumerate(words):
            # Return first index of the word in sentence (1-indexed) where searchWord is a prefix
            if searchWord == w[:len(searchWord)]:
                return i+1        
        
        # If there is no such word return -1
        return -1
    