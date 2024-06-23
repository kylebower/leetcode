class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:        
        m = len(grid)
        n = len(grid[0])
        
        row = [0]*m
        col = [0]*n
        
        diff = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        for i in range(m):
            for j in range(n):
                diff[i][j] = (2 * row[i] - m) + (2 * col[j] - n)
        return diff
    