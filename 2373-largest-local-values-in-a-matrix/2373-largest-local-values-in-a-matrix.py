class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for i in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                gridLocal = [x[j:j+3] for x in grid[i:i+3]]
                maxLocal[i][j] =max([max(x) for x in gridLocal])
        return maxLocal