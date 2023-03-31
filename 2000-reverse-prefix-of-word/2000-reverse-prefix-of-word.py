class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # base case
        n = len(word)
        if n < 2:
            return word
        
        # define two pointers
        L = 0
        R = 0
        
        # iterate to find first occurence of ch
        while R < n and word[R] != ch:
            R += 1
        
        # reverse segment if found and return result
        if R < n and word[R] == ch:
            return word[:R+1][::-1] + word[R+1:]
        else:
            return word
        