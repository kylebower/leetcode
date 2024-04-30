class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for p in patterns:
            if self.isSubstring(p, word):
                result += 1
        return result
    
    def isSubstring(self, sub: str, word: str) -> bool:
        # return True if sub is a substring of word
        # otherwise return False
        n_sub = len(sub)
        n_word = len(word)
        if n_sub > n_word:
            return False
        
        output = False
        k = 0
        while not output and k < n_word - n_sub + 1:
            if sub == word[k:k+n_sub]:
                print('yes')
                output = True
            k += 1
        
        return output
        