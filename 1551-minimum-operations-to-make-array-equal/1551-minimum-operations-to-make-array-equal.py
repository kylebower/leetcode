class Solution:
    def minOperations(self, n: int) -> int:
        
        res = 0
        while n > 0:
            res += n-1
            n -= 2
        return res
    