class Solution:
    def maxPower(self, s: str) -> int:
        
        n = len(s)
        
        # define two pointers
        L = 0
        R = 0
        
        # move sliding window to find longest substring of a unique character
        longest = 0        
        while R < n:
            while R < n and s[L] == s[R]:
                R += 1
            cur = R - L
            if cur > longest:
                longest = cur
            L = R
        
        return longest
    