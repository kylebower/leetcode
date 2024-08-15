class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        count = 0 # count of open minus closed
        nSwaps = 0
        
        for i in range(n):
            if s[i] == '[':
                count += 1
            elif s[i] == ']':
                count -= 1
            
            if count < 0:
                nSwaps += 1
                count = 1
            
        return nSwaps
    