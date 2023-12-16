class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            wins = sum([grid[i][j] for j in range(n)])
            if wins == n-1:
                return i
        return -1
    