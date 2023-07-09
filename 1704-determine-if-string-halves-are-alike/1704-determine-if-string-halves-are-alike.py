class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # split string in two
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        
        # return true if a and b have the same number of vowels
        return self.numVowel(a) == self.numVowel(b)
    
    def numVowel(self, s: str) -> int:
        # return number of vowels in string
        count = 0
        for c in s:
            if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count += 1
        return count
