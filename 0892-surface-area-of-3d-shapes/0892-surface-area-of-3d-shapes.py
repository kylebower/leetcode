class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                cur = grid[i][j]
                
                # front and back
                if cur != 0:
                    area += 2
                
                # up and down
                if i == 0:
                    area += cur
                else:
                    area += abs(cur-grid[i-1][j])
                if i == n-1:
                    area += cur
                
                # left and right
                if j == 0:
                    area += cur
                else:
                    area += abs(cur-grid[i][j-1])
                if j == n-1:
                    area += cur
        
        return area                
                