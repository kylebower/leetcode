class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(n):
            if i%2 != 0:
                s[i] = self.shift(s[i-1], s[i])
        
        return ''.join(s)
    
    def shift(self, c: chr, x: chr) -> chr:
        return chr(ord(c) + int(x))