class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        numUnclosed = 0
        res = 0
        
        for c in s:
            if c == '(':
                numUnclosed += 1
            if c == ')':
                if numUnclosed > 0:
                    numUnclosed -= 1
                else:
                    res += 1
        
        res += numUnclosed
        return res
    