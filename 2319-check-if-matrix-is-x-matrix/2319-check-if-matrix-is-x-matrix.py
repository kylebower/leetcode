class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 0 or grid[i][n-i-1] == 0:
                return False
            j = min(i, n-i-1)
            if sum(grid[i][:j]+grid[i][j+1:n-j-1]+grid[i][n-j:]) > 0:
                return False
            
        return True
