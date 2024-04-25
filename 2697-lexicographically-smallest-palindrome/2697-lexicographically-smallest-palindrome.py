class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        
        for k in range(n//2):
            if ord(s[k]) < ord(s[n-1-k]):
                s[n-1-k] = s[k]
            else:
                s[k] = s[n-1-k]
        
        return ''.join(s)
    