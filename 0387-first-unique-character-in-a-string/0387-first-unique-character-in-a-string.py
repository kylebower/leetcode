class Solution:
    def firstUniqChar(self, s: str) -> int:
        ds = {}
        for c in s:
            ds[c] = ds.get(c,0) + 1
        
        for i in range(len(s)):
            if ds[s[i]] == 1:
                return i
        
        return -1
    