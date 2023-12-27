class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # flip rows so that first entry is 1
        for i, row in enumerate(grid):
            if row[0] == 0:
                grid[i] = [1-x for x in grid[i]]
        
        res = 0
        
        for i in range(n):
            if i == 0:
                res += m*2**(n-1)
            else:
                sumi = sum([row[i] for row in grid])
                res += max(sumi, m-sumi)*2**(n-i-1)
                
        return res
    