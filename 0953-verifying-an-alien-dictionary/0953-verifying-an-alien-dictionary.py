class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {}
        i = 0
        for c in order:
            alien_dict[c] = i
            i += 1
        
        for j in range(len(words)-1):
            if not self.inOrder(words[j], words[j+1], alien_dict):
                return False
        
        return True
    
    def inOrder(self, word1, word2, alien_dict):
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            if alien_dict[word1[i]] > alien_dict[word2[i]]:
                return False
            elif alien_dict[word1[i]] < alien_dict[word2[i]]:
                return True        
        return len(word1) <= len(word2)
        