class Solution:
    def halvesAreAlike(self, s: str) -> bool:        
        # return true if two halves have the same number of vowels
        n = len(s)
        return self.numVowel(s[:n//2]) == self.numVowel(s[n//2:])
    
    def numVowel(self, s: str) -> int:
        # return number of vowels in string
        count = 0
        for c in s:
            if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count += 1
        return count
