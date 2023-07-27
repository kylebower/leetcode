class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            area += max(grid[i])
            area += max([grid[k][i] for k in range(n)])
            area += sum([grid[i][k] > 0 for k in range(n)])
        return area
    