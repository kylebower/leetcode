class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        res = 0
        
        for mi in range(m-2):
            for ni in range(n-2):
                cur = self.computeSum(grid, mi, ni)
                res = max(cur, res)
        
        return res
    
    def computeSum(self, grid, mi, ni):
        return sum(grid[mi][ni:ni+3]) + grid[mi+1][ni+1] + sum(grid[mi+2][ni:ni+3])
        