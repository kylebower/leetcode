class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        nBeautiful = 0
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        nVowels = 0
        nConsonants = 0
        
        for i in range(n):            
            nVowels = 0
            nConsonants = 0
            for j in range(i, n):
                c = s[j]
                if c in vowels:
                    nVowels += 1
                else:
                    nConsonants += 1
                    
                if (nVowels == nConsonants) and ((nVowels * nConsonants) % k == 0):
                    nBeautiful += 1
        
        return nBeautiful
        