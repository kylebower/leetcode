class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for row in grid:
            for i in range(n):
                coli = [r[i] for r in grid]
                if row == coli:
                    res += 1
        return res
    