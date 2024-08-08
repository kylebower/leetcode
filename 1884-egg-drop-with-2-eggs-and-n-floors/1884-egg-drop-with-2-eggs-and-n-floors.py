class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        res = 0
        interval = 1
        
        while n > 0:
            n -= interval
            interval += 1
            res += 1
        
        return res