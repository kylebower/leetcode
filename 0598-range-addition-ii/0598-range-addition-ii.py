class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        if ops == []:
            return m * n
        
        min_x = m
        min_y = n
        for a, b in ops:
            min_x = min(min_x, a)
            min_y = min(min_y, b)        
            
        return min_x * min_y
    