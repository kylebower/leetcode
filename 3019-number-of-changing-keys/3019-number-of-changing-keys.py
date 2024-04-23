class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        s = s.lower()
        res = 0
        
        for i in range(n-1):
            if s[i] != s[i+1]:
                res += 1
        
        return res
                